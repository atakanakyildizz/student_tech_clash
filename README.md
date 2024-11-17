# ATLAS Agent-Based Transit Logistics and Scheduling
# Public Transport Multi-Agent Solution

This project is a multi-agent system designed to handle public transport requests for IBEC challange organized by BEST having Reply as a sponsor. It consists of user agents that collect travel requests from users and an orchestrator that processes these requests to calculate optimized travel routes.

## Components

### UserAgent

The `UserAgent` class represents a user interacting with the system. It uses a language model (LLM) from OpenAI to collect travel requests from users and sends these requests to the Orchestrator.

#### Methods

- `__init__(self, user_id: str)`: Initializes the `UserAgent` with a user ID.
- `collect_travel_request(self, query: str) -> Dict[str, Any]`: Collects travel request details from the user via LLM interaction.

### Orchestrator

The `Orchestrator` class receives travel requests from multiple `UserAgent` instances and processes these requests to calculate optimized travel routes.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/public_transport_multi_agent_solution.git
   cd public_transport_multi_agent_solution
