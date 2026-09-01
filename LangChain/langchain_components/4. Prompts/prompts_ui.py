from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import streamlit as st  
import warnings


warnings.filterwarnings("ignore")

st.title("LangChain local prompt Demo.")


@st.cache_resource

def load_local_model():
    llm = HuggingFacePipeline.from_model_id(
        model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        task="text-generation",
        pipeline_kwargs={
            "temperature" : 0.5,
            "max_new_tokens" : 150
        }
    )
    return ChatHuggingFace(llm=llm)

model = load_local_model()

user_prompt = st.text_input("Enter Prompt")

if st.button("Generate Response"):
    if user_prompt:
        with st.spinner("processing locally...."):
            response = model.invoke(user_prompt)
            clean_text = response.content
            if "<|assistant|>" in clean_text:
                clean_text = clean_text.split("<|assistant|>")[-1].strip()
            st.write(clean_text)