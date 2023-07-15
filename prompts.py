q = ["Reserved", \
     "Classify the abstract into one of the following publication types: \
     Original Research, Review, Other, NA/TBD.", \
     "Classify the abstract into one of the following data types: \
     Original Data, Dataset, Other, NA/TBD.", \
     "Classify the abstract into one of the following populations: \
     Animal, Clinical, Healthy, Other, NA/TBD.", \
     "Reserved", \
     "Classify the abstract into one of the following applications: Restore, \
     Replace, Enhance, Improve, Supplement, Contribute, Design, NA/TBD.", \
     "Classify the abstract into one of the following recording types: \
     Electrical, Magnetic, Metabolic, NA/TBD.", \
     "Classify the abstract into one of the following recording method: \
     EEG, ECoG, Intracortical.", \
     "Classify the abstract into one of the following signals: Attention, \
     Auditory, Error, Frontal, Hybrid, Motor, Other, SCP, Visual, NA/TBD.", \
     "Reserved", \
     "Classify the abstract into one of the following purposes: Brain Switch, \
     Clinical/Brain-State Monitoring, Communication, Cursor/Movement Control, \
     Domotics/Environmental Control, Gaming/Computer Control, Image Triage, \
     NA/TBD, Neurofeedback, Neurprosthetic/Robotics, Offline/Online Target \
     Selection, Other.", \
     "Classify the abstract into one of the following contributions: Applied \
     Research, Basic Research, Experimental Development, Support.", \
     "Reserved"]

q_subpop = [ \
        "Classify the abstract into one of the following animals: \
        Cat, Fly, Frog, Mouse, Primate, Rabbit, Rat, Sheep.", \
        "Classify the abstract into one of the following diseases: ADHD, \
        ALS, Brainstem Stroke, Cancer, Cerebral Palsy, Charcot-Marie-Tooth, \
        Dystonia, Eating Disorders, Epilepsy, Locked-in (unspecified), MDD, \
        Minimally Conscious State, Multiple, Muscular Dystrophy, Paraplegic, \
        Persistant Vegetative State, Primary Lateral Sclerosis, Schizophrenia, \
        Severe Motor Deficit, Spinal Cord Injury, Stroke, TBI, Tetraplegic, \
        Tremor.", \
        "Classify the abstract into one of the following populations: \
        Adults, Children, College Age, Infants, Seniors.", \
        "Classify the abstract into one of the following miscellaneous \
        populations: Cell Culture."]

q_sigpdim = [ \
        "Classify the abstract into one of the following attention signal \
        paradigms: Alpha.", \
        "Classify the abstract into one of the following auditory signal \
        paradigms: AEP, ASSR, P300.", \
        "Classify the abstract into one of the following error signal \
        paradigms: ERN, FRN.", \
        "Classify the abstract into one of the following frontal signal \
        paradigms: Cognitive Tasks.", \
        "Classify the abstract into one of the following hybrid signal \
        paradigms: Alpha-SSVEP, Imagery Tasks-P300, Imagery Tasks-SSVEP, \
        P300-SSVEP, P300-VEP.", \
        "Classify the abstract into one of the following motor signal \
        paradigms: Imagery Tasks, Movement.", \
        "Classify the abstract into one of the following other signal \
        paradigms: NA/TBD.", \
        "Classify the abstract into one of the following SCP signal \
        paradigms: Neurofeedback.", \
        "Classify the abstract into one of the following visual signal \
        paradigms: mVEP, N2pc, P300, RSVP, SSVEP, VEP."]

q_subctrb = [\
        "Classify the abstract into one of the following applied research \
        sub-contributions: Clinical (assessment), Clinical (therapeutic), \
        Collaborative, Healthy Population, Home Use, Independent Use, Other, \
        Purpose.", \
        "Classify the abstract into one of the following basic research \
        sub-contributions: Demographics, Ethics, Neural Signals, Other, \
        Signal Measurement/Acquisition, Signal Modeling, User.", \
        "Classify the abstract into one of the following experimental \
        development sub-contributions: DSP, Feedback/Interface, Other, Signal \
        Measurement/Acquisition, System, User.", \
        "Classify the abstract into one of the following support \
        sub-contributions: Education, Other, Public Dataset, Tools/Software."]

def init():
    global q
    global q_subpop
    global q_sigpdim
    global q_subctrb
