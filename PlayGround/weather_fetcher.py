import requests

class weatherTools:
    def __init__(self):
        self.name = "live weather Fetching."

    def execute(self, city):
        url = f"https://wttr.in/{city}?format=j1"

        try:
            response = requests.get(url)
            data = response.json()

            temp_c = data["current_condition"][0]["temp_C"]
            condition = data["current_condition"][0]["weatherDesc"][0]["value"]

            return f"Tempreture in {city.capitalize()} is {temp_c} C with {condition}"
        except Exception as e:
            return f"failed to fetch the weather: {e} " 


class Agent:

    def __init__(self, name):
        self.name = name

    def run_tool(self, tool_obj, city):
        print(f"[{self.name}] is executing tool '{tool_obj}'")
        result = tool_obj.execute(city)
        print(result)



weather_tools = weatherTools()

hawa = Agent("hawa")

hawa.run_tool(weather_tools, "Istanbul")

    