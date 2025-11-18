import os
from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from .tools import fetch_web_content, generate_project_artifacts, format_generation_response

# --- Agent Definition ---

# 1. Define the tools
web_scraper_tool = FunctionTool(
    name="fetch_web_content",
    function=fetch_web_content,
    description=(
        "Tool used to ingest and extract a detailed text specification from a given URL. "
        "Use this ONLY when the user provides a direct URL and the request is related "
        "to code generation based on that URL content."
    ),
    # The output is simple text (the specification), which is passed back to the LLM/context
    output_converter=lambda x: f"Web Content Specification:\n{x}"
)

project_generation_tool = FunctionTool(
    name="generate_project_artifacts",
    function=generate_project_artifacts,
    description=(
        "A specialized tool for generating a complete, multi-file code project and "
        "documentation (README.md, main.py, utility.py, etc.) in Python. "
        "It takes a full specification string and returns the project files."
    ),
    # Use the format_generation_response helper to create the final response
    output_converter=format_generation_response
)

# 2. Define the main agent
root_agent = Agent(
    name="Winnie v0.2 - Multi-File Project Generator",
    model="gemini-2.5-flash",
    description="An advanced agent that can ingest specifications from the web and generate complete, multi-file Python projects and documentation.",
    instruction=(
        "You are Winnie v0.2, an expert in software development and multi-step workflows. "
        "Your primary goal is to generate a project by delegating tasks to your tools. "

        "**Workflow Priority:**\n"
        "1. **Ingestion:** If the user's prompt contains a URL, first use the `fetch_web_content` tool "
        "to retrieve the detailed specification. The output of this tool will be the `specification` string for the next step.\n"
        "2. **Generation:** Once you have the final, detailed specification (either from the web or the user's direct input), "
        "IMMEDIATELY call the `generate_project_artifacts` tool. Ensure you provide the 'language' (default Python), "
        "'project_name', and the comprehensive 'specification' to this tool."

        "ALWAYS ask for clarification if the required language, project name, or detailed "
        "parameters/specification are missing or too vague."
    ),
    tools=[
        web_scraper_tool,
        project_generation_tool,
    ]
)
