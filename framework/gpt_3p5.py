import os
import openai
import framework.prompts as prompts

openai.api_key = os.environ["OPENAI_API_KEY"]

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
    gpt_prompt = []
    ans = {'Title': '',
           'Abstract': '',
           'PublicationType': '',
           'DataType': '',
           'Population': '',
           'Subpopulation': '',
           'Purpose': '',
           'Recording Type': '',
           'Recording Tech': '',
           'Brain Signal': '',
           'Paradigm': '',
           'Application': '',
           'Contribution': '',
           'Sub-Contribution': ''}
    prompts.init()
    ans['Title'] = title
    ans['Abstract'] = abstract

    gpt_prompt.append({"role":"user", "content":abstract+prompts.q[1]})
    ans['PublicationType'] = gpt_3p5_turbo_request(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['PublicationType']})
    print(ans['PublicationType'])

    gpt_prompt.append({"role":"user", "content":abstract+prompts.q[2]})
    ans['DataType'] = gpt_3p5_turbo_request(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['DataType']})
    print(ans['DataType'])

    gpt_prompt.append({"role":"user", "content":abstract+prompts.q[3]})
    ans['Population'] = gpt_3p5_turbo_request(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['Population']})
    print(ans['Population'])

    # Population: Animal, Clinical, Healthy, Other
    question = ""
    if ans['Population'] == "Animal":
        question = prompts.q_subpop[0]
    elif ans['Population'] == "Clinical":
        question = prompts.q_subpop[1]
    elif ans['Population'] == "Healthy":
        question = prompts.q_subpop[2]
    elif ans['Population'] == "Other":
        question = prompts.q_subpop[3]

    gpt_prompt.append({"role":"user", "content":question})
    ans['Subpopulation'] = gpt_3p5_turbo_request(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['Subpopulation']})
    print(ans['Subpopulation'])

    gpt_prompt.append({"role":"user", "content":abstract+prompts.q[5]})
    ans['Purpose'] = gpt_3p5_turbo_request(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['Purpose']})
    print(ans['Purpose'])

    gpt_prompt.append({"role":"user", "content":abstract+prompts.q[6]})
    ans['Recording Type'] = gpt_3p5_turbo_request(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['Recording Type']})
    print(ans['Recording Type'])

    gpt_prompt.append({"role":"user", "content":abstract+prompts.q[7]})
    ans['Recording Tech'] = gpt_3p5_turbo_request(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['Recording Tech']})
    print(ans['Recording Tech'])

    gpt_prompt.append({"role":"user", "content":abstract+prompts.q[8]})
    ans['Brain Signal'] = gpt_3p5_turbo_request(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['Brain Signal']})
    print(ans['Brain Signal'])

    # Signals: Attention, Auditory, Error, Frontal, Hybrid, Motor, Other,
    # SCP, Visual
    if ans['Brain Signal'] == "Attention":
        question = prompts.q_sigpdim[0]
    elif ans['Brain Signal'] == "Auditory":
        question = prompts.q_sigpdim[1]
    elif ans['Brain Signal'] == "Error":
        question = prompts.q_sigpdim[2]
    elif ans['Brain Signal'] == "Frontal":
        question = prompts.q_sigpdim[3]
    elif ans['Brain Signal'] == "Hybrid":
        question = prompts.q_sigpdim[4]
    elif ans['Brain Signal'] == "Motor":
        question = prompts.q_sigpdim[5]
    elif ans['Brain Signal'] == "Other":
        question = prompts.q_sigpdim[6]
    elif ans['Brain Signal'] == "SCP":
        question = prompts.q_sigpdim[7]
    elif ans['Brain Signal'] == "Visual":
        question = prompts.q_sigpdim[8]

    gpt_prompt.append({"role":"user", "content":question})
    ans['Paradigm'] = gpt_3p5_turbo_request(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['Paradigm']})
    print(ans['Paradigm'])

    gpt_prompt.append({"role":"user", "content":abstract+prompts.q[10]})
    ans['Application'] = gpt_3p5_turbo_request(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['Application']})
    print(ans['Application'])

    gpt_prompt.append({"role":"user", "content":abstract+prompts.q[11]})
    ans['Contribution'] = gpt_3p5_turbo_request(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['Contribution']})
    print(ans['Contribution'])

    # Contributions: Applied Research, Basic Research,
    # Experimental Development, Support
    if ans['Contribution'] == "Applied Research":
        question = prompts.q_subctrb[0]
    elif ans['Contribution'] == "Basic Research":
        question = prompts.q_subctrb[1]
    elif ans['Contribution'] == "Experimental Development":
        question = prompts.q_subctrb[2]
    elif ans['Contribution'] == "Support":
        question = prompts.q_subctrb[3]

    gpt_prompt.append({"role":"user", "content":question})
    ans['Sub-Contribution'] = gpt_3p5_turbo_request(gpt_prompt, temperature)
    gpt_prompt.append({"role":"assistant", "content":ans['Sub-Contribution']})
    print(ans['Sub-Contribution'])
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
