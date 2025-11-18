Winnie v0.2: Multi-File Project Generation AgentWinnie v0.2 is an advanced AI agent built using the Google Agent Development Kit (ADK) designed for complex project generation. It features a sophisticated, multi-step workflow capable of ingesting large specifications and outputting multiple file artifacts.ArchitectureThe system is structured as a single LLM Agent that utilizes two custom tools for a sequential workflow:fetch_web_content Tool: (Simulated) Takes a URL and returns a detailed specification string. This is the first step when a URL is provided.generate_project_artifacts Tool: Takes the final specification and uses a structured output schema to force the LLM to generate multiple file names and their contents (e.g., README.md, main.py, utility.py).Root Agent (Winnie v0.2): Handles the orchestration, deciding whether to scrape a URL first, and then delegating the final generation step.Setup InstructionsPrerequisites: Python 3.9+Install ADK:pip install google-adk
Project Structure:Ensure your directory structure looks like this:.
├── run_winnie.py
└── winnie_v0.2/
    ├── agent.py
    ├── tools.py
    └── .env
Set API Key:Create a file named .env inside the winnie_v0.2/ directory and add your API key:GOOGLE_API_KEY="YOUR_API_KEY_HERE"
Run the Agent:You can run the agent in a simple command-line interface using the dedicated runner script:python run_winnie.py
Or, you can use the ADK web UI for a richer experience:adk web
# Then open your browser to http://localhost:8000
Example PromptTo test the multi-step and multi-file functionality, try a prompt like this:"Generate a 'Data Averager' project in Python. The detailed spec is at: http://example.com/project-spec"
