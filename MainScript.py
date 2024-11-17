import openai
from typing import Dict, Any

# Set your OpenAI API key here
openai.api_key = ("Your_open_ai_api_key")

# BusAgent and OrchestratorAgent classes
class BusAgent:
    def __init__(self, bus_id: str, orchestrator_agent: Any):
        self.bus_id = bus_id
        self.orchestrator_agent = orchestrator_agent

    def get_crowdedness_info(self) -> Dict[str, Any]:
        # Simulate getting crowdedness information from the bus
        crowdedness_info = {
            "bus_id": self.bus_id,
            "crowdedness_level": "high",  # This could be "low", "medium", or "high"
            "timestamp": "2023-10-01T12:00:00Z"
        }
        return crowdedness_info

    def send_crowdedness_info(self):
        crowdedness_info = self.get_crowdedness_info()
        self.orchestrator_agent.receive_crowdedness_info(crowdedness_info)

class OrchestratorAgent:
    def receive_crowdedness_info(self, info: Dict[str, Any]):
        print(f"Received crowdedness info: {info}")

# UserAgent class
class UserAgent:
    def __init__(self):
        self.llm = openai.ChatCompletion.create  # Use OpenAI for user interaction

    def get_user_travel_request(self):
        # Ask user for travel request
        print("Please enter your travel request (e.g., 'I want to go from A to B at 8 AM').")
        user_input = input("Enter your travel request: ")
        return user_input

    def process_request(self, user_input):
        # Process the travel request
        print(f"Processing the travel request: {user_input}")
        return f"Processed request: {user_input}"

    def get_travel_suggestion(self, travel_request):
        # Send request to OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or you can use a newer model
            messages=[{"role": "system", "content": "You are a helpful travel assistant."},
                      {"role": "user", "content": travel_request}],
            max_tokens=150,  # Determines the response length
            temperature=0.7  # Controls randomness of the response
        )
        suggestion = response['choices'][0]['message']['content'].strip()
        return suggestion


# Main function
def main():
    orchestrator_agent = OrchestratorAgent()

    # Sending bus crowdedness info
    bus_agent = BusAgent(bus_id="bus_123", orchestrator_agent=orchestrator_agent)
    bus_agent.send_crowdedness_info()  # Send crowdedness info

    # Get user travel request and provide suggestion
    agent = UserAgent()  # Create an instance of UserAgent class
    user_input = agent.get_user_travel_request()  # Get the user's travel request
    response = agent.process_request(user_input)  # Process the travel request

    # Get travel suggestion from OpenAI API
    travel_suggestion = agent.get_travel_suggestion(user_input)
    print(f"Suggested travel route: {travel_suggestion}")

if __name__ == "__main__":
    main()
