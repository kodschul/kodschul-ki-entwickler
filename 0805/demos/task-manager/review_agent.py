"""
review_agent.py — AI-powered code review agent (skeleton)

Usage:
    python review_agent.py <file_to_review>

The agent reads the target file, calls Claude, and writes structured
findings to review-output.json.
"""

import json
import sys

# TODO: Import the Anthropic SDK
# import anthropic

# TODO: Define the model to use
# MODEL = "claude-opus-4-5"

# TODO: Define the system prompt that tells Claude what to look for
SYSTEM_PROMPT = """
# TODO: Write a system prompt.
# Example: "You are a security-focused code reviewer. Analyse the
#  provided Python file and return a JSON array of issues found.
#  Each issue must have: line (int), severity (high/medium/low),
#  description (str), suggestion (str)."
"""


def func_read_file(filePath):
    """Return the contents of filePath as a string."""
    # TODO: Open the file and return its contents
    pass


def func_review_file(fileContents):
    """
    Send fileContents to Claude and return the raw response text.

    Steps:
    1. Create an anthropic.Anthropic() client
    2. Call client.messages.create() with:
       - model=MODEL
       - max_tokens=1024
       - system=SYSTEM_PROMPT
       - messages=[{"role": "user", "content": fileContents}]
    3. Return response.content[0].text
    """
    # TODO: Implement API call
    pass


def func_parse_response(rawResponse):
    """
    Parse the raw string from Claude into a Python object.
    Claude should return JSON — extract and parse it here.
    """
    # TODO: Use json.loads() or extract JSON block from the response
    pass


def func_write_output(findings, outputPath="review-output.json"):
    """Write findings to outputPath as pretty-printed JSON."""
    # TODO: Open outputPath for writing and dump findings with indent=2
    pass


def func_main():
    # TODO: Wire together the steps
    # 1. Read sys.argv[1] as the target file path
    # 2. Call func_read_file()
    # 3. Call func_review_file()
    # 4. Call func_parse_response()
    # 5. Call func_write_output()
    # 6. Print a summary to stdout (number of issues found)
    pass


if __name__ == "__main__":
    func_main()
