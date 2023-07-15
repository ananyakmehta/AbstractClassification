import os
import openai
import prompts

openai.api_key = os.environ["OPENAI_API_KEY"]
gpt_prompt = []

def gpt_3p5_turbo_request(prompt, temperature):
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt,
            temperature=temperature,
            max_tokens=48,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0)
    return response.choices[0]["message"]["content"].strip()

def model_gpt_3p5_turbo(title, abstract, temperature):
    ans = [{'title': 'Title',
             'content': 'Abstract'},
            {'title': 'Publication type',
             'content': ''},
            {'title': 'Data Type',
             'content': ''},
            {'title': 'Population',
             'content': ''},
            {'title': 'Sub-population',
             'content': ''},
            {'title': 'Application',
             'content': ''},
            {'title': 'Recording type',
             'content': ''},
            {'title': 'Recording method',
             'content': ''},
            {'title': 'Signal',
             'content': ''},
            {'title': 'Paradigm',
             'content': ''},
            {'title': 'Purpose',
             'content': ''},
            {'title': 'Contribution',
             'content': ''},
            {'title': 'Sub-contribution',
             'content': ''}
            ]
    prompts.init()
    ans[0]['title'] = title
    ans[0]['content'] = abstract

    gpt_prompt.append({"role":"user", "content":abstract+prompts.q[1]})
    ans[1]['content'] = gpt_3p5_turbo_request(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans[1]['content']})
    print(ans[1]['content'])

    for i in range(2, 13):
        if prompts.q[i] == "Reserved":
            continue
        gpt_prompt.append({"role":"user", "content":prompts.q[i]})
        ans[i]['content'] = gpt_3p5_turbo_request(gpt_prompt, temperature)
        gpt_prompt.append({"role":"assistant", "content":ans[i]['content']})
        print(ans[i]['content'])

    # Add more questions based on the above responses
    # Population: Animal, Clinical, Healthy, Other
    question = ""
    if ans[3]['content'] == "Animal":
        question = prompts.q_subpop[0]
    elif ans[3]['content'] == "Clinical":
        question = prompts.q_subpop[1]
    elif ans[3]['content'] == "Healthy":
        question = prompts.q_subpop[2]
    elif ans[3]['content'] == "Other":
        question = prompts.q_subpop[3]

    gpt_prompt.append({"role":"user", "content":question})
    ans[4]['content'] = gpt_3p5_turbo_request(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans[4]['content']})
    print(ans[4]['content'])

    # Signals: Attention, Auditory, Error, Frontal, Hybrid, Motor, Other,
    # SCP, Visual
    if ans[8]['content'] == "Attention":
        question = prompts.q_sigpdim[0]
    elif ans[8]['content'] == "Auditory":
        question = prompts.q_sigpdim[1]
    elif ans[8]['content'] == "Error":
        question = prompts.q_sigpdim[2]
    elif ans[8]['content'] == "Frontal":
        question = prompts.q_sigpdim[3]
    elif ans[8]['content'] == "Hybrid":
        question = prompts.q_sigpdim[4]
    elif ans[8]['content'] == "Motor":
        question = prompts.q_sigpdim[5]
    elif ans[8]['content'] == "Other":
        question = prompts.q_sigpdim[6]
    elif ans[8]['content'] == "SCP":
        question = prompts.q_sigpdim[7]
    elif ans[8]['content'] == "Visual":
        question = prompts.q_sigpdim[8]

    gpt_prompt.append({"role":"user", "content":question})
    ans[9]['content'] = gpt_3p5_turbo_request(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans[9]['content']})
    print(ans[9]['content'])

    # Contributions: Applied Research, Basic Research,
    # Experimental Development, Support
    if ans[11]['content'] == "Applied Research":
        question = prompts.q_subctrb[0]
    elif ans[11]['content'] == "Basic Research":
        question = prompts.q_subctrb[1]
    elif ans[11]['content'] == "Experimental Development":
        question = prompts.q_subctrb[2]
    elif ans[11]['content'] == "Support":
        question = prompts.q_subctrb[3]

    gpt_prompt.append({"role":"user", "content":question})
    ans[12]['content'] = gpt_3p5_turbo_request(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans[12]['content']})
    print(ans[12]['content'])
    return ans

if __name__ == "__main__":
    # Invocation with a sample title and abstract
    model_gpt_3p5_turbo("Brain-computer interface boosts motor imagery practice \
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
