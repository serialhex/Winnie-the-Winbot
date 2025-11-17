import os
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from .tools import generate_code_and_docs, format_generation_response

# --- Agent Definition ---

# Define the root agent.
# In ADK, the 'root_agent' is the entry point for the system.
# It is configured to use the custom function 'generate_code_and_docs' as a tool.

# 1. Define the tool
# The input_converter and output_converter are used to format the input parameters
# for the tool function and format the tool's output before it's passed back to the LLM.
# Since our tool is highly specialized and returns structured data, we use the
# format_generation_response helper to create a clean, final text output.

# We must use a FunctionTool wrapper for our custom Python function
code_generation_tool = FunctionTool(
    name="generate_code_and_documentation",
    function=generate_code_and_docs,
    description=(
        "A highly specialized tool for generating functional code and corresponding "
        "Markdown documentation based on a detailed specification. You MUST use this tool "
        "for any request involving code generation, programming, or documentation creation."
    ),
    # Use the format_generation_response helper to create the final response
    output_converter=format_generation_response 
)

# 2. Define the main agent
root_agent = Agent(
    name="Winnie v0 - Code Generator",
    model="gemini-2.5-flash",
    description="An advanced agent that generates complete code projects and documentation based on user parameters.",
    instruction=(
        "You are Winnie v0, an expert agent for software development. "
        "Your role is to accept a user's request for a project and immediately delegate to the "
        "Code Generation Tool. "
        "Your goal is to fill the 'language', 'project_name', and 'parameters' arguments for the tool "
        "based on the user's prompt. You must use the tool for every request. "
        "ALWAYS ask for clarification if the required language, project name, or detailed "
        "parameters are missing or too vague."
    ),
    tools=[
        code_generation_tool,
    ]
)