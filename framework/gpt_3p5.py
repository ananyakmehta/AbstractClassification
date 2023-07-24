import os
import openai
import framework.prompts as prompts
import json
from tenacity import retry, wait_random_exponential, stop_after_attempt
import copy

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
                    "description": "Specified category",
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
def get_category_reason(prompt, temperature):
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
    #print(prompt)
    #print(response)
    data = json.loads(response.choices[0].message.function_call.arguments)
    return data["category"], data["reason"]

def get_abstract_summary(title, abstract, temperature):
    gpt_prompt = []
    prompt = "Summarize the abstract for a high school student.\n"
    gpt_prompt.append({"role":"user", "content":prompt+title+abstract})
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=gpt_prompt,
            temperature=temperature,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0)
    #print(gpt_prompt)
    #print(response)
    data = 'Summary: ' + response.choices[0]["message"]["content"]
    return data

def classify_abstract(title, abstract, temperature):
    ans = {'Title': '',
           'Abstract': '',
           'Summary': '',
           'PublicationType': '',
           'PublicationTypeReason': '',
           'DataType': '',
           'DataTypeReason': '',
           'Population': '',
           'PopulationReason': '',
           'Subpopulation': '',
           'SubpopulationReason': '',
           'Purpose': '',
           'PurposeReason': '',
           'RecordingType': '',
           'RecordingTypeReason': '',
           'RecordingTech': '',
           'RecordingTechReason': '',
           'BrainSignal': '',
           'BrainSignalReason': '',
           'Paradigm': '',
           'ParadigmReason': '',
           'Application': '',
           'ApplicationReason': '',
           'Contribution': '',
           'ContributionReason': '',
           'SubContribution': '',
           'SubContributionReason': ''}
    prompts.init()
    ans['Title'] = title
    ans['Abstract'] = abstract
    ans['Summary'] = get_abstract_summary(title, abstract, temperature)
    #print('Summary: {0}'.format(ans['Summary']))

    common_prompt = []
    common_prompt.append({"role":"system", "content":prompts.knbase})
    common_prompt.append({"role":"user", "content":title+abstract})

    gpt_prompt = copy.deepcopy(common_prompt)
    prompt = prompts.pre_prompt + prompts.cat_top[1] + prompts.post_prompt
    gpt_prompt.append({"role":"user", "content":'Options:'+prompt})
    gpt_prompt.append({"role":"user", "content":prompts.pubtypedef})
    ans['PublicationType'], ans['PublicationTypeReason'] = \
            get_category_reason(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['PublicationType']})
    print('PublicationType: {0}'.format(ans['PublicationType']))
    #print('PublicationTypeReason: {0}'.format(ans['PublicationTypeReason']))

    gpt_prompt = copy.deepcopy(common_prompt)
    prompt = prompts.pre_prompt + prompts.cat_top[2] + prompts.post_prompt
    gpt_prompt.append({"role":"user", "content":'Options:'+prompt})
    gpt_prompt.append({"role":"user", "content":prompts.datatypedef})
    ans['DataType'], ans['DataTypeReason'] = \
            get_category_reason(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['DataType']})
    print('DataType: {0}'.format(ans['DataType']))
    #print('DataTypeReason: {0}'.format(ans['DataTypeReason']))

    gpt_prompt = copy.deepcopy(common_prompt)
    prompt = prompts.pre_prompt + prompts.cat_top[3] + prompts.post_prompt
    gpt_prompt.append({"role":"user", "content":'Options:'+prompt})
    gpt_prompt.append({"role":"user", "content":prompts.popdef})
    ans['Population'], ans['PopulationReason'] = \
            get_category_reason(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['Population']})
    print('Population: {0}'.format(ans['Population']))
    #print('PopulationReason: {0}'.format(ans['PopulationReason']))

    prompt = "Subpopulation"
    if ans['Population'] == "Animal":
        prompt = prompts.cat_subpop[0]
    elif ans['Population'] == "Clinical":
        prompt = prompts.cat_subpop[1]
    elif ans['Population'] == "Healthy":
        prompt = prompts.cat_subpop[2]
    elif ans['Population'] == "Other":
        prompt = prompts.cat_subpop[3]
    gpt_prompt = copy.deepcopy(common_prompt)
    prompt = prompts.pre_prompt + prompt + prompts.post_prompt
    gpt_prompt.append({"role":"user", "content":'Options:'+prompt})
    ans['Subpopulation'], ans['SubpopulationReason'] = \
            get_category_reason(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['Subpopulation']})
    print('Subpopulation: {0}'.format(ans['Subpopulation']))
    #print('SubpopulationReason: {0}'.format(ans['SubpopulationReason']))

    gpt_prompt = copy.deepcopy(common_prompt)
    prompt = prompts.pre_prompt + prompts.cat_top[5] + prompts.post_prompt
    gpt_prompt.append({"role":"user", "content":'Options:'+prompt})
    gpt_prompt.append({"role":"user", "content":prompts.purposedef})
    ans['Purpose'], ans['PurposeReason'] = \
            get_category_reason(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['Purpose']})
    print('Purpose: {0}'.format(ans['Purpose']))
    #print('PurposeReason: {0}'.format(ans['PurposeReason']))

    gpt_prompt = copy.deepcopy(common_prompt)
    prompt = prompts.pre_prompt + prompts.cat_top[6] + prompts.post_prompt
    gpt_prompt.append({"role":"user", "content":'Options:'+prompt})
    gpt_prompt.append({"role":"user", "content":prompts.rectypedef})
    ans['RecordingType'], ans['RecordingTypeReason'] = \
            get_category_reason(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['RecordingType']})
    print('RecordingType: {0}'.format(ans['RecordingType']))
    #print('RecordingTypeReason: {0}'.format(ans['RecordingTypeReason']))

    gpt_prompt = copy.deepcopy(common_prompt)
    prompt = prompts.pre_prompt + prompts.cat_top[7] + prompts.post_prompt
    gpt_prompt.append({"role":"user", "content":'Options:'+prompt})
    gpt_prompt.append({"role":"user", "content":prompts.rectypedef})
    ans['RecordingTech'], ans['RecordingTechReason'] = \
            get_category_reason(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['RecordingTech']})
    print('RecordingTech: {0}'.format(ans['RecordingTech']))
    #print('RecordingTechReason: {0}'.format(ans['RecordingTechReason']))

    gpt_prompt = copy.deepcopy(common_prompt)
    prompt = prompts.pre_prompt + prompts.cat_top[8] + prompts.post_prompt
    gpt_prompt.append({"role":"user", "content":'Options:'+prompt})
    gpt_prompt.append({"role":"user", "content":prompts.signaldef})
    ans['BrainSignal'], ans['BrainSignalReason'] = \
            get_category_reason(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['BrainSignal']})
    print('BrainSignal: {0}'.format(ans['BrainSignal']))
    #print('BrainSignalReason: {0}'.format(ans['BrainSignalReason']))

    if ans['BrainSignal'] == "Attention":
        prompt = prompts.cat_sigpdim[0]
    elif ans['BrainSignal'] == "Auditory":
        prompt = prompts.cat_sigpdim[1]
    elif ans['BrainSignal'] == "Error":
        prompt = prompts.cat_sigpdim[2]
    elif ans['BrainSignal'] == "Frontal":
        prompt = prompts.cat_sigpdim[3]
    elif ans['BrainSignal'] == "Hybrid":
        prompt = prompts.cat_sigpdim[4]
    elif ans['BrainSignal'] == "Motor":
        prompt = prompts.cat_sigpdim[5]
    elif ans['BrainSignal'] == "Other":
        prompt = prompts.cat_sigpdim[6]
    elif ans['BrainSignal'] == "SCP":
        prompt = prompts.cat_sigpdim[7]
    elif ans['BrainSignal'] == "Visual":
        prompt = prompts.cat_sigpdim[8]
    gpt_prompt = copy.deepcopy(common_prompt)
    prompt = prompts.pre_prompt + prompt + prompts.post_prompt
    gpt_prompt.append({"role":"user", "content":'Options:'+prompt})
    gpt_prompt.append({"role":"user", "content":prompts.signaldef})
    ans['Paradigm'], ans['ParadigmReason'] = \
            get_category_reason(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['Paradigm']})
    print('Paradigm: {0}'.format(ans['Paradigm']))
    #print('ParadigmReason: {0}'.format(ans['ParadigmReason']))

    gpt_prompt = copy.deepcopy(common_prompt)
    prompt = prompts.pre_prompt + prompts.cat_top[10] + prompts.post_prompt
    gpt_prompt.append({"role":"user", "content":'Options:'+prompt})
    gpt_prompt.append({"role":"user", "content":prompts.appdef})
    ans['Application'], ans['ApplicationReason'] = \
            get_category_reason(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['Application']})
    print('Application: {0}'.format(ans['Application']))
    #print('ApplicationReason: {0}'.format(ans['ApplicationReason']))

    gpt_prompt = copy.deepcopy(common_prompt)
    prompt = prompts.pre_prompt + prompts.cat_top[11] + prompts.post_prompt
    gpt_prompt.append({"role":"user", "content":'Options:'+prompt})
    gpt_prompt.append({"role":"user", "content":prompts.contribdef})
    ans['Contribution'], ans['ContributionReason'] = \
            get_category_reason(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['Contribution']})
    print('Contribution: {0}'.format(ans['Contribution']))
    #print('ContributionReason: {0}'.format(ans['ContributionReason']))

    if ans['Contribution'] == "Applied Research":
        prompt = prompts.cat_subctrb[0]
        subcontribdef = prompts.arsubcontribdef
    elif ans['Contribution'] == "Basic Research":
        prompt = prompts.cat_subctrb[1]
        subcontribdef = prompts.brsubcontribdef
    elif ans['Contribution'] == "Experimental Development":
        prompt = prompts.cat_subctrb[2]
        subcontribdef = prompts.edsubcontribdef
    elif ans['Contribution'] == "Support":
        prompt = prompts.cat_subctrb[3]
        subcontribdef = prompts.supsubcontribdef
    prompt = prompts.pre_prompt + prompt + prompts.post_prompt
    gpt_prompt.append({"role":"user", "content":'Options:'+prompt})
    gpt_prompt.append({"role":"user", "content":subcontribdef})
    ans['SubContribution'], ans['SubContributionReason'] = \
            get_category_reason(gpt_prompt, temperature)
    gpt_prompt = copy.deepcopy(common_prompt)
    gpt_prompt.append({"role":"assistant", "content":ans['SubContribution']})
    print('SubContribution: {0}'.format(ans['SubContribution']))
    #print('SubContributionReason: {0}'.format(ans['SubContributionReason']))

    return ans

if __name__ == "__main__":
    # Invocation with a sample title and abstract
    classify_abstract("Brain-computer interface boosts motor imagery practice \
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
    with severe motor impairments.\n")
