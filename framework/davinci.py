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
    # Invocation with a sample title and abstract
    model_davinci("Brain-computer interface boosts motor imagery practice \
    during stroke recovery.\n", "OBJECTIVE: Motor imagery (MI) is assumed to \
    enhance poststroke motor recovery, yet its benefits are debatable. \
    Brain-computer interfaces (BCIs) can provide instantaneous and quantitative \
    measure of cerebral functions modulated by MI. The efficacy of BCI-monitored \
    MI practice as add-on intervention to usual rehabilitation care was \
    evaluated in a randomized controlled pilot study in subacute stroke \
    patients. METHODS: Twenty-eight hospitalized subacute stroke patients with \
    severe motor deficits were randomized into 2 intervention groups: 1-month \
    BCI-supported MI training (BCI group, n = 14) and 1-month MI training \
    without BCI support (control group; n = 14). Functional and \
    neurophysiological assessments were performed before and after the \
    interventions, including evaluation of the upper limbs by Fugl-Meyer \
    Assessment (FMA; primary outcome measure) and analysis of oscillatory \
    activity and connectivity at rest, based on high-density \
    electroencephalographic (EEG) recordings. RESULTS: Better functional outcome \
    was observed in the BCI group, including a significantly higher probability \
    of achieving a clinically relevant increase in the FMA score (p < 0.03). \
    Post-BCI training changes in EEG sensorimotor power spectra (ie, stronger \
    desynchronization in the alpha and beta bands) occurred with greater \
    involvement of the ipsilesional hemisphere in response to MI of the \
    paralyzed trained hand. Also, FMA improvements (effectiveness of FMA) \
    correlated with the changes (ie, post-training increase) at rest in \
    ipsilesional intrahemispheric connectivity in the same bands (p < 0.05). \
    INTERPRETATION: The introduction of BCI technology in assisting MI practice \
    demonstrates the rehabilitative potential of MI, contributing to \
    significantly better motor functional outcomes in subacute stroke patients \
    with severe motor impairments.\n", 1)
