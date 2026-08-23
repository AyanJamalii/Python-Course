class Tool:

  def __init__(self, name, description):
    self.name = name  # self. se variable save hota hai
    self.description = description

  def execute(self, query):
    print(f"⚙️ Running [{self.name}] with query: '{query}'")


class SmartAgent:

  def __init__(self, name):
    self.name = name
    self.tools = []  # Empty list tools store karne ke liye

  def add_tool(self, tool_object):
    self.tools.append(tool_object)
    print(f"✅ Tool '{tool_object.name}' added to {self.name}'s toolkit.")

  def use_tool(self, tool_name, query):
    # Search for tool in self.tools list
    for tool in self.tools:
      if tool.name.lower() == tool_name.lower():
        tool.execute(query)
        return

    print(f"❌ Tool '{tool_name}' not found in {self.name}'s toolkit!")


# ==========================================
# 🧪 Testing the Agent & Tools
# ==========================================

# 1. Tools Create Karein
search_tool = Tool("Search", "Searches the web for live information")
image_tool = Tool("ImageGen", "Generates images from prompt")

# 2. Agent Create Karein
jarvis = SmartAgent("Jarvis")

print("\n--- Adding Tools ---")
jarvis.add_tool(search_tool)
jarvis.add_tool(image_tool)

print("\n--- Executing Tasks ---")
# 3. Agent Tool Use Karega
jarvis.use_tool("Search", "Python 2026 AI developments")
jarvis.use_tool("ImageGen", "Cyberpunk cityscape at night")

# 4. Unknown Tool Test
jarvis.use_tool("Calculator", "2 + 2")