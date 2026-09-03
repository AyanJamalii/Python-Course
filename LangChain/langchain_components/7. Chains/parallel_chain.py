from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model_1 = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

model_2 = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

prompt_1 = PromptTemplate(
    template='Generate short and simple notes from the following text. \n {text}',
    input_variables=['text']
)

prompt_2 = PromptTemplate(
    template='Generate 5 short Questions answers from the following text \n {text}.',
    input_variables=['text']
)

prompt_3 = PromptTemplate(
    template='Merge the provided notes and questions answers into a single document. \n {notes} and quiz {quiz}.',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt_1 | model_1 | parser,
    'quiz' : prompt_2 | model_2 | parser,
})

marge_chain = prompt_3 | model_2 | parser

chain = parallel_chain | marge_chain

text = """
Artificial Intelligence (AI) and Machine Learning (ML) are transforming modern technology and reshaping human society. At its core, Artificial Intelligence refers to the simulation of human intelligence in machines that are programmed to think, learn, and solve complex problems like a human mind. Machine Learning, a key subset of AI, focuses on developing algorithms that allow computers to automatically learn and improve from experience without being explicitly programmed for every scenario.

The roots of modern AI stem from early computer science research, but recent breakthroughs in computing power, cloud infrastructure, and massive data collection have accelerated its growth exponentially. AI systems rely heavily on Neural Networks—computational models inspired by the biological structure of the human brain. Deep Learning, an advanced branch of ML, utilizes multi-layered neural networks to analyze complex patterns in vast amounts of unstructured data, powering innovations like Natural Language Processing (NLP), Autonomous Vehicles, Computer Vision, and Generative AI.

Despite its vast potential and convenience, the rapid advancement of AI brings significant ethical and practical challenges. Key concerns include data privacy violations, algorithmic bias in decision-making processes, job displacement across traditional industries, and the potential security risks associated with automated autonomous systems. To ensure AI benefits humanity safely, researchers, developers, and policymakers around the globe are advocating for strict regulatory frameworks, transparent AI models, and responsible AI governance.
"""
result = chain.invoke({'text': text})
print(result)