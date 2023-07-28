import os
import openai
import framework.prompts as prompts
import json
from tenacity import retry, wait_random_exponential, stop_after_attempt

openai.api_key = os.environ["OPENAI_API_KEY"]

functions = [
    {
        "name": "print_category_reason",
        "description": "Prints the specified category and the reason for selection",
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "Selected category",
                },
                "reason": {
                    "type": "string",
                    "description": "Reason for selecting the category",
                },
            },
            "required": ["category", "reason"],
        },
    },
]

@retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
def get_category_reason(knbase, title, abstract, ask, temperature, debug):
    prompt = []
    prompt.append({"role":"system", "content":knbase})
    prompt.append({"role":"user",
                   "content":'Title: '+title+'\n'+'Abstract: '+abstract+'\n'+ask})
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=prompt,
            functions=functions,
            function_call={"name": "print_category_reason"},
            temperature=temperature,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0)
    if debug == True:
        print(prompt)
        print(response)
    return json.loads(response.choices[0].message.function_call.arguments)

@retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
def get_abstract_summary(title, abstract, ask, temperature, debug):
    prompt = []
    prompt.append({"role":"user",
                   "content":'Title: '+title+'\n'+'Abstract: '+abstract+'\n'+ask})
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=prompt,
            temperature=temperature,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0)
    if debug == True:
        print(prompt)
        print(response)
    data = 'Summary: ' + response.choices[0]["message"]["content"]
    return data

if __name__ == "__main__":
    # TODO: Invocation with a sample title and abstract
    summary = get_abstract_summary("", "", "", 1.0, False)
    print(summary)
