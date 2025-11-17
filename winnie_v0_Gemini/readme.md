# **Winnie v0: Code Generation Agent (ADK)**

Winnie v0 is an AI agent built using the Google Agent Development Kit (ADK) designed to accept a project specification from a user and generate functional code and supporting documentation.

## **System Architecture**

The system is a single LLM Agent (Winnie v0 \- Code Generator) that utilizes one powerful custom tool:

1. **Root Agent (Winnie v0)**: Acts as the orchestrator. Its primary instruction is to analyze the user's request, extract the project requirements (language, name, detailed parameters), and delegate the entire task to the generate\_code\_and\_documentation tool.  
2. **generate\_code\_and\_documentation Tool**: This is a custom Python function that directly calls the Gemini API in a structured manner. It uses a strong **system instruction** and a **JSON response schema** to force the Large Language Model (LLM) to produce only the code and documentation content in a predictable format.

## **Setup Instructions**

1. **Prerequisites**:  
   * Python 3.9+  
   * Google AI API Key (from Google AI Studio).  
2. **Install ADK**:  
   pip install google-adk

3. Set Environment Variables:  
   Create a file named .env in the winnie\_v0/ directory and add your API key:  
   GOOGLE\_API\_KEY="YOUR\_API\_KEY\_HERE"

   *Note: ADK automatically detects and uses this environment variable.*  
4. Run the Agent in the ADK Web UI:  
   Navigate to the directory containing the winnie\_v0 folder (e.g., if it's my-projects/winnie\_v0, navigate to my-projects/) and run:  
   adk web

   Open your browser to http://localhost:8000, select the "Winnie v0 \- Code Generator" agent, and begin interacting with it.

## **Example Prompt**

"Generate a 'Hello World' project in Python. It should just print 'Hello, Code Generation World\!' to the console."