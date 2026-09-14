from langchain_text_splitters import RecursiveCharacterTextSplitter, Language


text = """
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Student Name: {self.name}, Age: {self.age}"

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "F"
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 200,
    chunk_overlap = 0
)

chunks = splitter.split_text(text)
print(len(chunks))
print(chunks)