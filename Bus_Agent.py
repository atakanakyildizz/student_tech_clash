from typing import Dict, Any

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

# Example usage
class OrchestratorAgent:
    def receive_crowdedness_info(self, info: Dict[str, Any]):
        print(f"Received crowdedness info: {info}")

# Initialize the orchestrator agent
orchestrator_agent = OrchestratorAgent()

# Initialize the bus agent with a bus ID and the orchestrator agent
bus_agent = BusAgent(bus_id="bus_123", orchestrator_agent=orchestrator_agent)

# Send crowdedness information to the orchestrator agent
bus_agent.send_crowdedness_info()