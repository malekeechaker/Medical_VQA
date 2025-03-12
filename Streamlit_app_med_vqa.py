import streamlit as st
from PIL import Image
import torch
from transformers import BlipForQuestionAnswering, BlipImageProcessor, BlipProcessor

# Define paths
model_path = "D:/model/medical_vqa_blip"
image_processor_path = f"{model_path}/image_processor"
text_processor_path = f"{model_path}/text_processor"

# Load image processor
image_processor = BlipImageProcessor.from_pretrained(image_processor_path)

# Load text processor (tokenizer)
text_processor = BlipProcessor.from_pretrained(text_processor_path)

# Load model
model = BlipForQuestionAnswering.from_pretrained(model_path)

# Move model to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Streamlit UI
st.title("Medical Visual Question Answering")
st.write("Upload a medical image and ask a question about it.")

# Upload image
uploaded_image = st.file_uploader("Upload a medical image", type=["jpeg", "png"])
if uploaded_image is not None:
    image = Image.open(uploaded_image).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Input question
question = st.text_input("Ask a question about the image:")

# Process the image and question
if st.button("Get Answer"):
    if uploaded_image is not None and question:
        with st.spinner("Processing..."):
            # Preprocess image
            image_inputs = image_processor(images=image, return_tensors="pt").to(device)

            # Preprocess text
            text_inputs = text_processor(text=question, return_tensors="pt").to(device)

            # Combine inputs for the model
            inputs = {**image_inputs, **text_inputs}

            # Generate answer
            with torch.no_grad():
                output = model.generate(**inputs)

            # Decode answer
            answer = text_processor.decode(output[0], skip_special_tokens=True)

            st.success(f"**Answer:** {answer}")
    else:
        st.error("Please upload an image and enter a question.")
