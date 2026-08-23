class AiAgent:  

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def introduce(self):
        print(f"Hello, My name is {self.name} and my role is {self.role}. ")

    def do_task(self, task):
        print(f"My Name is {self.name} and currently im {task}")



agent1 = AiAgent("Jarvis", "Code Generation")
agent2 = AiAgent("Friday", "Image Generation")
agent3 = AiAgent("EDITH", "Web Browsing.")


agent1.introduce()
agent2.introduce()
agent3.do_task("Searching latest Ai Trends.")