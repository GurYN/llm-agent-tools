import json, ollama, inspect
from typing_extensions import Sequence
from typing import get_type_hints

from tools.math_tools import add, subtract, multiply, divide
from tools.tasks_tools import get_tasks, create_task, complete_task
from tools.api_tools import get_posts, get_comments, get_users
from utilities.tool_utility import get_function_info_list, call_function_dynamically


MODEL = "gemma2"
funcs = [add, subtract, multiply, divide, get_users, get_tasks, create_task, complete_task, get_posts, get_comments]
tools_description = get_function_info_list(funcs)

def generate_message(question: str) -> Sequence[ollama.Message]:
    return [
        {
            'role': 'system',
            'content': f"""
                You are an assistant that has access to the following set of tools.
                Here are the names and descriptions for each tool:

                {tools_description}

                You must follow these instructions:
                Always select one or more of the above tools based on the user query
                If a tool is found, you must respond in the JSON format matching the following schema:
                {{
                   "tools": {{
                        "tool": "<name of the selected tool>",
                        "tool_input": <parameters for the selected tool, matching the tool's JSON schema. If no input is required, this will be an empty JSON object.>
                   }}
                }}
                If there is no tool input required, you will respond with an empty JSON property.
                If there are multiple tools required, make sure a list of tools are returned in a JSON array.
                If there is no tool that match the user request, you will respond with empty json.
                Do not add any additional Notes or Explanations.
            """,
        },
        {
            'role': 'user',
            'content': f"""
                {question}
            """,
        }
    ]

questions = [
    "What can I say to my doudou?",
    "Show me users",
    "Show me comments for the third post.",
    "Get the top 5 posts.",
    "Remind me to take a coffee",
    "Do I have something to do?",
    "You can mark my 'coffee' task as completed.",
    "I have bought a 6 pack bottle for 20$. What is the price for one bottle? And is the price for 3 pack of 6 bottles?",
    "Hello, how are you?"
]

for question in questions:
    response = ollama.chat(model=MODEL, messages=generate_message(question), format='json')
    tools = json.loads(response['message']['content'])

    print(f"Question: {question}")

    if len(tools) == 0:
       response = ollama.chat(model=MODEL, messages=[{ 'role': 'user', 'content': question}], format='')
       print(f"Answer: {response['message']['content']}")
    else:
        tool_results = []
        for tool in tools.get('tools', []):
            print(f"Tool: {tool}")
            tool_name = tool['tool']
            tool_input = tool['tool_input']

            try:
                response = call_function_dynamically(funcs, tool_name, **tool_input)
                tool_results.append({ 'name': tool_name, 'response': response })
                print(f"Tools {tool['tool']} answer: {response}")
            except:
                print(f"Function {tool_name} with parameters {tool_input} not found")

        if len(tool_results) > 0:
            response = ollama.chat(model=MODEL, messages=[{ 'role': 'user', 'content': f"""
                Base on the user request: {question}, tools have been used and here is the results:
                {tool_results}
                Give an answer using results to the user.
            """}], format='')
            print(f"Answer: {response['message']['content']}")

    print()
