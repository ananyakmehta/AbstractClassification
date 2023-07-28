import os
import openai
import framework.prompts as prompts
import json
from tenacity import retry, wait_random_exponential, stop_after_attempt

openai.api_key = os.environ["OPENAI_API_KEY"]

@retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
def get_category_reason(knbase, title, abstract, ask, temperature, debug):
    out_format="Return the answer in the json format: {\"category\": \"Selected category\", \"reason\": \"Reason for selecting the category\"}"
    prompt = (knbase + 'Title: ' + title + 'Abstract: ' + abstract +
              'Options: ' + ask + out_format)
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=temperature,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0)
    if debug == True:
        print(prompt)
        print(response)
    return json.loads(response.choices[0].text.strip())

@retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
def get_abstract_summary(title, abstract, ask, temperature, debug):
    prompt = ('Title: ' + title + 'Abstract: ' + abstract + ask)
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=temperature,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0)
    if debug == True:
        print(prompt)
        print(response)
    data = 'Summary: ' + response.choices[0].text.strip()
    return data

if __name__ == "__main__":
    # TODO: Invocation with a sample title and abstract
    summary = get_abstract_summary("", "", "", 1.0, False)
    print(summary)
