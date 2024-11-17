from agents.user_agent import UserAgent
from orchestrator.orchestrator import Orchestrator

def main():
    # Initialize orchestrator
    orchestrator = Orchestrator()

    # Create user agents
    user1 = UserAgent(user_id="user_1")
    user2 = UserAgent(user_id="user_2")

    # Collect travel requests
    travel_request_1 = user1.collect_travel_request("I need to travel from Point A to Point B at 8 AM.")
    travel_request_2 = user2.collect_travel_request("Find me a way to reach the city center by 9 AM.")

    # Send travel requests to the orchestrator
    user1.send_to_orchestrator(travel_request_1, orchestrator)
    user2.send_to_orchestrator(travel_request_2, orchestrator)

    # Calculate routes in the orchestrator
    orchestrator.calculate_routes()

if __name__ == "__main__":
    main()
