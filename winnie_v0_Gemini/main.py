import os
import sys
from google.adk.testing.agent_test_client import AgentTestClient

# Add the agent directory to the path so the agent can be imported
sys.path.append(os.path.dirname(__file__))

from winnie_v0.agent import root_agent

# --- Simple Console Runner ---

def run_agent_in_console():
    """
    Creates a simple client to run the Winnie v0 agent directly in the console.
    This bypasses the full ADK web UI but demonstrates the core functionality.
    """
    print("---------------------------------------------------------")
    print(f"Agent Ready: {root_agent.name}")
    print("Enter 'quit' or 'exit' to stop.")
    print("---------------------------------------------------------")

    # Initialize the test client for the root agent
    client = AgentTestClient(agent=root_agent)

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['quit', 'exit']:
                break
            
            if not user_input.strip():
                continue

            # Process the user input
            response = client.send_message(user_input)
            
            # The response contains the final, formatted output from the tool's output_converter
            print(f"\nWinnie v0: {response.text}\n")
            
        except Exception as e:
            print(f"\n[ERROR] An exception occurred: {e}\n")
            break

if __name__ == "__main__":
    # Ensure the environment variable is set (ADK would do this via .env)
    # This check is for standalone running.
    if not os.getenv("GOOGLE_API_KEY"):
        print("WARNING: GOOGLE_API_KEY environment variable is not set. ")
        print("Please set it in the winnie_v0/.env file and ensure it is loaded.")
        print("The tool will use a simulated response until the API key is active.")

    run_agent_in_console()