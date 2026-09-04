import random    

class FakeLLM:
    def __init__(self):
        print('LLM created')

    def predict(self, prompt):
        response_list = [
            'Islamabad is the capital of Pakistan.',
            'PSL is cricket League',
            'AGI stands for Artificial General Intelligence'
        ]

        return {'response' : random.choice(response_list)}

class FakePromptTemplate:
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def Format(self, input_dict):
        return self.template.format(**input_dict)

prompt_template = FakePromptTemplate(
    template="Tell me about {topic}", input_variables=["topic"]
)

formatted_prompt = prompt_template.Format({"topic": "you"})
print("Formatted Prompt:", formatted_prompt)

llm = FakeLLM()
output = llm.predict(formatted_prompt)

print("LLM Response:", output["response"])