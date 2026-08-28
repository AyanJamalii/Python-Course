import streamlit as st
import warnings
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate, load_prompt

warnings.filterwarnings("ignore")


st.set_page_config(page_title="Research Tool", page_icon="📑")

@st.cache_resource
def load_local_model():
    llm = HuggingFacePipeline.from_model_id(
        model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        task="text-generation",
        pipeline_kwargs={
            "temperature": 0.5,
            "max_new_tokens": 500
        }
    )
    return ChatHuggingFace(llm=llm)


model = load_local_model()

st.header("Research tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)
# reusing the Dyanamic Prompt template:
template = load_prompt('template.json')

if st.button("Summarize"):
    with st.spinner("Analyzing research paper locally..."):
        # Create final prompt using PromptTemplate
        formatted_prompt = template.format(
            paper_name=paper_input,
            style=style_input,
            length=length_input
        )
        
        # Invoke local LLM
        response = model.invoke(formatted_prompt)
        
        # Clean ChatML template tags from response
        clean_text = response.content
        if "<|assistant|>" in clean_text:
            clean_text = clean_text.split("<|assistant|>")[-1].strip()
            
        st.subheader("Summary Result:")
        st.write(clean_text)