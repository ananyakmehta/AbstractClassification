knbase = "Given an abstract, classify it into one of the specified categories \
and provide a justification for selecting the category."

pubtypedef = "Definitions:\n\
Original Research: Publication developed a new dataset or made a contribution based on an existing dataset.\n\
Review: Publication provided a survey of some aspect of the BCI field.\n\
Other: Publication is an editorial, tutorial, release of public datasets, etc."

datatypedef = "Definitions:\n\
Original Data: Publication developed their own dataset.\n\
Dataset: Publication uses an existing dataset.\n\
Other: Publication relies on simulated data, theory, or other sources."

popdef = "Definitions:\n\
Animal: Publication uses animals as the subject/user of the BCI.\n\
Healthy: Publication uses healthy humans as the subject/user of the BCI.\n\
Clinical: Publication uses a clinical (human) population as the subject/user of the BCI.\n\
Other: Publication uses a cell culture or other population for their research."

purposedef = "Definitions:\n\
Enhance: Enables the CNS to respond to events/produce outputs at a level exceeding its natural ability.\n\
Supplement: Provides the CNS with new ways to interact with the world beyond any individual’s natural output.\n\
Replace: Provides an alternative system for performing a lost function (following disease/injury). The benefits of the BCI remain only while it is in operation.\n\
Restore: Enables a user to regain natural function that has been lost due to disease or injury. The benefits of the BCI, however, only occurs when the system is in use (i.e., they do not induce neural plasticity [contrast with improve below]).\n\
Improve: Allows a user to regain lost functionality (following disease/injury) with effects that remain even when the BCI system is not in use.\n\
Contribute: Uses a BCI to investigate phenomena in another field.\n\
Design: Focuses on the refinement of methods, technologies, or techniques used in multiple BCI applications."

rectypedef = "Definitions:\n\
Electrical: Electroencephalography(EEG), Electrocorticography(ECoG), Intracortical\n\
Magnetic: Magnetoencephalography (MEG)\n\
Metabolic: Functional magnetic resonance imaging (fMRI), Ultrasound, Functional near-infrared spectroscopy (fNIRS)"

signaldef = "Definitions:\n\
Attention: Alpha\n\
Alpha: Changes in the alpha band (8-12 Hz) that occur when the user is asked to do an attention-related task (Bougrain et al., 2016).\n\
Auditory: Auditory Evoked Potential (AEP), Acoustic Steady-State Response (ASSR), P300\n\
Auditory Evoked Potential (AEP): Stereotyped voltage deflections time-locked to an auditory stimulus.\n\
Acoustic Steady-State Response (ASSR): Stable oscillations in activity elicited by repetitive auditory stimuli.\n\
P300: A positive deflection in the EEG after a rare auditory stimulus.\n\
Error: Error-Related Negativity (ERN), Feedback-Related Negativity (FRN)\n\
Error-Related Negativity (ERN): A negative component of an evoked potential that occurs after a response error (the user realizes they made a mistake; Bougrain et al., 2016)\n\
Feedback-Related Negativity (FRN): An evoked potential that occurs after a feedback error (the user is given feedback that is different than what they expected; Bougrain et al., 2016).\n\
Frontal: Cognitive Tasks\n\
Cognitive Tasks: Based on activity in response to higher cognitive tasks (e.g. mental rotation, mental arithmetic, etc.)\n\
Hybrid: Combinations of other paradigms presented here (e.g. Alpha-SSVEP, P300-SSVEP, etc.). Note: Hybrid describes a BCI where multiple signals and paradigms are used together in a single BCI system to create an enhanced BCI system. If the publication simply tests alternate paradigms, take advantage of the multi-select.\n\
Motor: Imagery Tasks, Movement\n\
Imagery Tasks: Changes in sensorimotor rhythms (SMRs) elicited by the imagination of movement.\n\
Movement: Changes in SMRs elicited by actual movement.\n\
Slow Cortical Potential (SCP): SCPs are event-related potentials that are time-locked and phase-locked to specific sensorimotor events (i.e., they occur at predictable times before, during, or after specific events; Wolpaw & Wolpaw, 2012).\n\
Neurofeedback: Provides the user with feedback of their SCP to aid in their control of this signal.\n\
Visual: mVEP, P300, RSVP, SSVEP, VEP, N2pc\n\
Motion-onset visual evoked potential (mVEP): A visual evoked potential that is elicited specifically by motion (Wolpaw & Wolpaw, 2012).\n\
P300: A positive deflection in the EEG after a rare visual stimulus. Rapid serial visual presentation (RSVP): Fast bursts of symbols presented successively at a central location (Acqualagna et al., 2010)\n\
Steady-state visual evoked potential (SSVEP): Stable oscillations in activity elicited by repetitive visual stimuli\n\
Visual evoked potential (VEP): Stereotyped voltage deflections time-locked to a visual stimulus.\n\
N2pc: A component of an evoked potential that reflects the focusing of attention on a potential target in a visual search array (Luck, 2011).\n\
Other: (e.g. affective, consciousness, memory system, speech, spinal cord, subcortical, and tactile). Note: We include speech as “other” despite the fact that it relies on motor output, as speech is typically thought of as a unique function of the motor system."

appdef = "Definitions:\n\
Communication: Used to aid one’s ability to communicate (e.g. text entry, P300 speller).\n\
Offline/Online Target Selection: Used to discriminate between various targets/options.\n\
Brain Switch: Used to let user control (asynchronously) when the BCI is 'on' or 'off'.\n\
Neuroprosthetic/Robotic Control: Used to power an external prosthetic or robot.\n\
Gaming/Computer Control: Used to control a game or computer.\n\
Cursor/Movement Control: Used to control a cursor or the movement of a (virutal) object.\n\
Clinical/Brain-State Monitoring: Used to detect seizure, drowsiness, etc.\n\
Domotics/Environmental Control: Used to control one’s surroundings (e.g. a smart home).\n\
Image Triage: Used to order images by relevance or whether they are a 'target'\n\
Neurofeedback: Used to provide feedback to the user of their current brain state."

contribdef = "Definitions:\n\
Basic Research: Research that seeks to uncover new knowledge about BCIs/the nervous system with no goal/objective in mind.\n\
Applied Research: Research that seeks to uncover new knowledge with a specific goal/objective in mind (i.e. there is a problem they want to solve).\n\
Experimental Development: The refinement of a BCI system through experiments on either specific subparts of a BCI system or the system as a whole.\n\
Support: The development of tools, software, datasets, etc. to aid BCI research."

brsubcontribdef = "Definitions:\n\
Ethics: The publication explores ethical questions in BCIs.\n\
Neural Signals: The publication explores neural signals that can be used in a BCI.\n\
Signal Modeling: The publication models neural signals used in a BCI.\n\
User: The publication explores how a user can interact with a BCI (e.g. whether a specific task can be used).\n\
Demographics: The publication explores whether a BCI can be used in a certain sub-population of subjects.\n\
Signal Measurement/Acquisition: The publication explores potential new techniques for measuring or acquiring neural signals."

arsubcontribdef = "Definitions:\n\
Clinical (Therapeutic): The publication seeks to develop a BCI as a therapeutic intervention for some clinical condition.\n\
Home Use: The publication seeks to develop a BCI for home use (e.g. outside the clinic).\n\
Purpose: The publication seeks to develop a BCI for a new purpose or user application.\n\
Healthy Population: The publication seeks to develop a BCI for a new population of users.\n\
Independent Use: The publication seeks to develop a BCI that can be used independently of the motor system.\n\
Collaborative: The publication seeks to develop a collaborative BCI system."

edsubcontribdef = "Definitions:\n\
User: The publication refines a BCI system by changing how the user interacts with the system.\n\
Digital Signal Processing (DSP): The publication refines a BCI system by changing the signal processing algorithms/techniques used.\n\
Signal Measurement/Acquisition: The publication refines a BCI system by changing how neural signals are measured/acquired.\n\
Feedback/Interface: The publication refines a BCI system by changing the feedback given to the user or the user interface.\n\
System: The publication refines a BCI system by altering the system as a whole."

supsubcontribdef = "Definitions:\n\
Education: The publication develops a new educational program for disseminating information about BCI research.\n\
Tools/Software: The publication develops new tools/software for use in BCI research.\n\
Public Dataset: The publication develops a public dataset for use in BCI research."

pre_prompt = "Options: "
post_prompt = "Select from the given options only. Do not return an answer that is not listed in the options."

cat_top = [
        "Reserved", \
        "Original Research, Review, Other, NA/TBD", \
        "Original Data, Dataset, Other, NA/TBD", \
        "Animal, Clinical, Healthy, Other, NA/TBD", \
        "Reserved", \
        "Replace, Enhance, Improve, Supplement, Contribute, Design, NA/TBD", \
        "Electrical, Magnetic, Metabolic, NA/TBD", \
        "Reserved", \
        "Attention, Auditory, Error, Frontal, Hybrid, Motor, Other, SCP, Visual, NA/TBD", \
        "Reserved", \
        "Brain Switch, Clinical/Brain-State Monitoring, Communication, \
        Cursor/Movement Control, Domotics/Environmental Control, \
        Gaming/Computer Control, Image Triage, NA/TBD, Neurofeedback, \
        Neurprosthetic/Robotics, Offline/Online Target Selection, Other", \
        "Applied Research, Basic Research, Experimental Development, Support", \
        "Reserved"
        ]

cat_rectech = [ \
        "Electroencephalography(EEG), Electrocorticography(ECoG), Intracortical", \
        "MEG", \
        "Functional magnetic resonance imaging (fMRI), Ultrasound, Functional near infrared spectroscopy (fNIRS)"
        ]

cat_subpop = [ \
        "Cat, Fly, Frog, Mouse, Primate, Rabbit, Rat, Sheep", \
        "ALS, Brainstem Stroke, Cancer, Cerebral Palsy, Charcot-Marie-Tooth, \
        Dystonia, Eating Disorders, Epilepsy, Locked-in (unspecified), MDD, \
        Minimally Conscious State, Multiple, Muscular Dystrophy, Paraplegic, \
        Persistant Vegetative State, Primary Lateral Sclerosis, Schizophrenia, \
        Severe Motor Deficit, Spinal Cord Injury, Stroke, TBI, Tetraplegic, \
        Tremor, ADHD", \
        "Adults, Children, College Age, Infants, Seniors", \
        "Cell Culture" \
        ]

cat_sigpdim = [ \
        "Alpha", \
        "AEP, ASSR, P300", \
        "ERN, FRN", \
        "Cognitive Tasks", \
        "Alpha-SSVEP, Imagery Tasks-P300, Imagery Tasks-SSVEP, P300-SSVEP, \
        P300-VEP", \
        "Imagery Tasks, Movement", \
        "NA/TBD", \
        "Neurofeedback", \
        "mVEP, N2pc, P300, RSVP, SSVEP, VEP" \
        "NA/TBD", \
        ]

cat_subctrb = [ \
        "Clinical (assessment), Clinical (therapeutic), Collaborative, \
        Healthy Population, Home Use, Independent Use, Other, Purpose", \
        "Demographics, Ethics, Neural Signals, Other, \
        Signal Measurement/Acquisition, Signal Modeling, User", \
        "DSP, Feedback/Interface, Other, Signal Measurement/Acquisition, \
        System, User", \
        "Education, Other, Public Dataset, Tools/Software" \
        ]

def init():
    global cat_top
    global cat_rectech
    global cat_subpop
    global cat_sigpdim
    global cat_subctrb
    global knbase
    global pubtypedef
    global datatypedef
    global popdef
    global purposedef
    global rectypedef
    global singaldef
    global appdef
    global contribdef
    global brsubcontribdef
    global arsubcontribdef
    global edsubcontribdef
    global supsubcontribdef
    global pre_prompt
    global post_prompt
