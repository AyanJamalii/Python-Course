from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""Please explain the research paper '{paper_name}' in a {style} style. 
Keep the explanation length {length}. Provide a clear and accurate summary.""",
    input_variables=["paper_name", "style", "length"]
)

template.save('template.json')