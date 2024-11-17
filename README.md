<<<<<<< HEAD
# ATLAS - Reply Student Tech Clash

## Overview

**ATLAS** is a travel assistance system developed for the **Reply Student Tech Clash** competition. It leverages artificial intelligence and real-time data to provide efficient travel suggestions based on user input. The system integrates multiple agents, including user agents, bus agents, and orchestrators, to simulate travel requests and bus crowdedness, while suggesting optimal routes.

## Project Structure

The project is divided into several modules:

- **agents**:
    - **`__init__.py`**: Initialization file for the agents module.
    - **`bus_agent.py`**: Contains the `BusAgent` class responsible for simulating bus crowdedness information and sending it to the orchestrator.
    - **`user_agent.py`**: Contains the `UserAgent` class responsible for handling user input, processing travel requests, and interacting with OpenAI's API for travel suggestions.
  
- **orchestrator**:
    - **`orchestrator.py`**: Contains the `Orchestrator` class, which collects travel data from user agents, calculates optimized routes using a predefined graph, and processes the travel requests.

- **`Main Script.py`**: The main script where the agents are instantiated, the travel requests are processed, and travel suggestions are retrieved using OpenAI's API.

## Features

- **Bus Crowdedness Information**: The system can simulate the gathering and sending of bus crowdedness information (e.g., low, medium, high).
- **User Travel Requests**: Users can input travel requests (e.g., "I want to go from A to B at 8 AM"), and the system processes these requests.
- **AI-Powered Travel Suggestions**: OpenAI's GPT-3.5-turbo model is used to generate travel route suggestions based on user input.
- **Route Calculation**: The system calculates optimal travel routes using a simplified version of Dijkstra's algorithm on a predefined graph of locations.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/ATLAS.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ATLAS
    ```

3. Create a virtual environment:

    ```bash
    python3 -m venv .venv
    ```

4. Activate the virtual environment:

    - On Windows:

      ```bash
      .venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source .venv/bin/activate
      ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Set your OpenAI API key in the `Main Script.py` file by replacing the placeholder with your actual key.

## Usage

1. Run the main script:

    ```bash
    python Main\ Script.py
    ```

2. The system will prompt you to enter your travel request. For example:

    ```bash
    Please enter your travel request (e.g., 'I want to go from A to B at 8 AM').
    ```

3. After entering the travel request, the system will process the request, simulate bus crowdedness information, and provide you with a suggested travel route.

## Example

```bash
Please enter your travel request (e.g., 'I want to go from A to B at 8 AM').
Enter your travel request: I want to go from Lingotto to Porta Nuova at 8 AM
Processing the travel request: I want to go from Lingotto to Porta Nuova at 8 AM
Suggested travel route: The best route from Lingotto to Porta Nuova is by taking bus 123 at 8:15 AM.
 
=======
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
>>>>>>> origin/main
