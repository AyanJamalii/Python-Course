import requests 
import json

class IpFetcher:
    def __init__(self):
        self.name = "Ip Fetcher."

    def execute(self):
        url = "http://ip-api.com/json/"

        try:
            response = requests.get(url, timeout=5)
            data = response.json()
            
            ip = data["query"]
            city = data["city"]
            country = data["country"]
            
            return f"User is from {city} in {country} and his/her Ip Address is {ip}"
        except Exception as e:
            return f"Failed to fetch IP Address. Error: {e}"


class Agent:
    def __init__(self, name):
        self.name = name

    def run_tool(self, tool_obj):
        print(f"[{self.name}] is run the tool {tool_obj}")
        result = tool_obj.execute()
        print(result)



ip_fetcher = IpFetcher()

ip_taker = Agent("IP Taker")

ip_taker.run_tool(ip_fetcher)