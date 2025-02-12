import streamlit as st
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForQuestionAnswering, BlipImageProcessor

# Load the fine-tuned model
@st.cache_resource
def load_model():
    # Load the fine-tuned model
    model = BlipForQuestionAnswering.from_pretrained("medical_vqa_blip")

    # Load the text and image processors
    text_processor = BlipProcessor.from_pretrained("medical_vqa_blip/text_processor")
    image_processor = BlipImageProcessor.from_pretrained("medical_vqa_blip/image_processor")

    return text_processor, image_processor, model



def generate_answer(image, question):
    image_inputs = image_processor(image, return_tensors="pt")
    text_inputs = text_processor(question, return_tensors="pt")
    inputs = {**text_inputs, "pixel_values": image_inputs["pixel_values"]}
    
    with torch.no_grad():
        output = model.generate(**inputs)
    
    return text_processor.decode(output[0], skip_special_tokens=True)

# Streamlit UI
st.title("Medical VQA with BLIP")
st.write("Upload a medical image and ask a question about it.")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
question = st.text_input("Enter your question")

'''
text_processor, image_processor, model = load_model()

if uploaded_file and question:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Get Answer"):
        answer = generate_answer(image, question)
        st.success(f"Answer: {answer}")
'''