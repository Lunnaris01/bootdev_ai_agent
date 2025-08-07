import os
import sys
from dotenv import load_dotenv
from google.genai import types
from functions.get_files_info import get_files_info, get_file_content, schema_get_files_info, schema_get_file_content
from functions.run_python_file import run_python_file, schema_run_python_file
from functions.write_file import write_file, schema_write_file

if len(sys.argv)<2:
    print("Please provide the prompt: python main.py \"This is my question to the AI!\"")
    sys.exit(1)
user_prompt=sys.argv[1]
verbose = False
if len(sys.argv)>2:
    verbose = True

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories (get_files_info)
- Read file contents (get_file_content)
- Write or overwrite files (write_file)

All paths you provide should be relative to the working directory.
You have to always provide a directory, provide "." if you are in root.
You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
Never create files unless specifically asked for.
Never try to extract css or javascript out of html files.
"""


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]
)

func_map ={
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "write_file": write_file,
}

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    print(f" - Calling function: {function_call_part.name}")
    args = function_call_part.args
    args["working_directory"] = "./hp"
    if function_call_part.name not in func_map.keys():
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )
    function_result = func_map[function_call_part.name](**args)

    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_call_part.name,
            response={"result": function_result},
            )
        ],
    )



load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages,
    config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    )

print(messages)
while response.function_calls is not None:
    for candidate in response.candidates:
        messages.append(candidate.content) # Append the function response
    if response.function_calls is not None:
        tool_parts = []
        for function_call_part in response.function_calls:
            if verbose:
                print(f"Calling function: {function_call_part.name}({function_call_part.args})")
            result = call_function(function_call_part)
            if verbose:
                print(f"Result: {result.parts[0].function_response.response['result']}")
            tool_parts.append(result.parts[0]) # Sammle nur den Part!
        tool_content = types.Content(role="tool", parts=tool_parts)
        messages.append(tool_content) # Append the content from the model's response.
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
        )


print(response.text)

if verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(messages)
