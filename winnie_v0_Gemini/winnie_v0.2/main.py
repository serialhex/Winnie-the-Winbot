import os
import sys
from google.adk.testing.agent_test_client import AgentTestClient

# Add the agent directory to the path so the agent can be imported
# The winnie_v0.2 folder must be in the same directory as this script.
sys.path.append(os.path.join(os.path.dirname(__file__), "winnie_v0.2"))

# Import the new v0.2 root agent
from agent import root_agent

# --- Simple Console Runner ---

def run_agent_in_console():
    """
    Creates a simple client to run the Winnie v0.2 agent directly in the console.
    This demonstrates the core functionality for testing.
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
            # This calls the agent's logic, which may use tools
            response = client.send_message(user_input)

            # The response contains the final, formatted output from the tool's output_converter
            print(f"\nWinnie v0.2: {response.text}\n")

        except Exception as e:
            print(f"\n[ERROR] An exception occurred: {e}\n")
            break

if __name__ == "__main__":
    # Ensure the environment variable is set (ADK would normally handle this)
    if not os.getenv("GOOGLE_API_KEY"):
        print("WARNING: GOOGLE_API_KEY environment variable is not set. ")
        print("Set it in the winnie_v0.2/.env file and ensure it is loaded, or the tool will use a simulated response.")

    run_agent_in_console()
