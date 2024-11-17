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
 