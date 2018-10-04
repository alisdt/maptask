
from collections import OrderedDict

# Text for all responses (instructions, landmarks and other responses)
# - Sound files are expected to have corresponding names in the sound file directory
# (e.g. Y.wav, A10.wav)
# - The only instruction having any effect on experiment flow is H (next instruction)
# - We use OrderedDict so that we print these for docs in the specified order

mt_phrases_exp_responses = OrderedDict([
    # directions
    ("Y", ["Yes.", "Yes.", "Yes.","Yes.", "Yes.", "Yes.","Yes.", "Yes."]),
    ("N", ["No.","No.","No.","No.","No."]),
    ("IDK", ["I dont know", "I dont know","I dont know"]),
    ("L", ["Left.","Left.","Left.","Left.","Left.","Left.","Left."]),
    ("LV", ["On the left", "On the left","On the left", "On the left","On the left", "On the left"]),
    ("R", ["Right.","Right.","Right.","Right.","Right.","Right."]),
    ("RV", ["On the right", "On the right","On the right", "On the right","On the right", "On the right"]),
    ("A", ["Above", "Above","Above","Above","Above"]),
    ("AV", ["You go above it", "You go above it", "You go above it", "You go above it", "You go above it", "You go above it"]),
    ("B", ["Below", "Below","Below","Below","Below"]),
    ("BV", ["You go below it", "You go below it", "You go below it", "You go below it", "You go below it"]),
    ("U", ["Upwards", "Upwards","Upwards", "Upwards","Upwards", "Upwards"]),
    ("UV", ["You go upwards", "You go upwards","You go upwards", "You go upwards"]),
    ("D", ["Downwards", "Downwards", "Downwards"]),
    ("DV", ["You go downwards", "You go downwards", "You go downwards", "You go downwards", "You go downwards", "You go downwards"]),

    # Other comments
    ("NP", ["I cant give you any past instructions, lets just move on from here", "I cant give you any past instructions, lets just move on from here","I cant give you any past instructions, lets just move on from here", "I cant give you any past instructions, lets just move on from here"]),
    ("NS", ["I'm not sure I dont have that information in my script", " I dont have the map I only have the script so I cant see that", " I dont have the map I only have the script so I cant see that", " I dont have the map I only have the script so I cant see that", " I dont have the map I only have the script so I cant see that"]),
    ("REP", ["I'm not sure, could you repeat that?", "I'm not sure, could you repeat that?","I'm not sure, could you repeat that?", "I'm not sure, could you repeat that?","I'm not sure, could you repeat that?", "I'm not sure, could you repeat that?","I'm not sure, could you repeat that?", "I'm not sure, could you repeat that?"]),
    ("ONE", ["I can only give you one bit of information at a time, what would you like to know first","I can only give you one bit of information at a time, what would you like to know first","I can only give you one bit of information at a time, what would you like to know first","I can only give you one bit of information at a time, what would you like to know first","I can only give you one bit of information at a time, what would you like to know first"]),
    ("WHICH", ["Which landmark is easiest for you to go from?","Which landmark is easiest for you to go from?","Which landmark is easiest for you to go from?","Which landmark is easiest for you to go from?"]),
    ("PAUSE", ["hang on i'll just check", "hang on i'll just check", "hang on i'll just check", "hang on i'll just check"])

])

mt_phrases_landmarks = OrderedDict([
    ("A", OrderedDict([
        ("Cam", "The camera shop"),
        ("Par", "The parked van"),
        ("All", "The allotments"),
        ("Mus", "The Museum"),
        ("Yac", "The yacht club"),
        ("Dis", "The disused monastery"),
        ("Alp", "Alpine Garden"),
        ("You", "The youth hostel"),
        ("Pic", "The picket fence"),
        ("Pho", "The phone box"),
        ("Hut", "The thatched mud hut"),
        ("Eas", "East lake")
    ])),
    ("B", OrderedDict([
        ("Gat", "The broken gate"),
        ("Picnic", "The picnic site"),
        ("Chi", "The childrens play area"),
        ("Far", "The farm yard"),
        ("Tra", "The train crossing"),
        ("Gra", "The granite quarry"),
        ("Wat", "The waterfall"),
        ("Bir", "The birch trees"),
        ("Sig", "The sign post"),
        ("Hay", "The haystack"),
        ("Ste", "The steep cliffs"),
        ("Wes", "The west lake")
    ]))
])

mt_phrases_instructions = OrderedDict([
    ("A", OrderedDict([
        ("A1", ["From the start you go down past the camera shop","From the start you go down past the camera shop","From the start you go down past the camera shop"]),
        ("A2", ["Then you then continue down past the parked van, and go underneath it","Then you then continue down past the parked van, and go underneath it"]),
        ("A3", ["Then  you go up and past the allotments","Then  you go up and past the allotments"]),
        ("A4", ["So then head over to the right side of the museum","So then head over to the right side of the museum","So then head over to the right side of the museum"]),
        ("A5", ["Then you head upwards and then turn left at the disused monastery","Then you head upwards and then turn left at the disused monastery","Then you head upwards and then turn left at the disused monastery"]),
        ("A6", ["Then you go up and past the alpine garden","Then you go up and past the alpine garden","Then you go up and past the alpine garden"]),
        ("A7", ["Then you should go past the youth hostel","Then you should go past the youth hostel","Then you should go past the youth hostel"]),
        ("A8", ["Then you head straight down to the right side of the phone box","Then you head straight down to the right side of the phone box","Then you head straight down to the right side of the phone box"]),
        ("A9", ["Then go up past the thatched mud hut","Then go up past the thatched mud hut","Then go up past the thatched mud hut"]),
        ("A10",["And then go past the east lake to the end.","And then go past the east lake to the end.","And then go past the east lake to the end."])
        ])),
    ("B", OrderedDict([
        ("B1", ["so from the start go down past the broken gate","so from the start go down past the broken gate"]),
        ("B2", ["Then you continue down past the picnic site and go underneath it","Then you continue down past the picnic site and go underneath it"]),
        ("B3", ["Then you  go up and past the childrens play area","Then you up and past the childrens play area"]),
        ("B4", ["So then head over to the right side of the train crossing","So then head over to the right side of the train crossing"]),
        ("B5", ["Then you go up and past the granite quarry","Then you go up and past the granite quarry"]),
        ("B6", ["Then you go round the waterfall","Then you round the waterfall"]),
        ("B7", ["Then you go up and over the signpost","Then you go up and over the signpost"]),
        ("B8", ["Then you head straight down to the left side of the haystack","Then you head straight down to the left side of the haystack"]),
        ("B9", ["Then go past the steep cliffs","Then go past the steep cliffs"]),
        ("B10", ["And then go past the west lake to the end","And then go past the west lake to the end"])
    ]))
])

mt_phrases_misc = OrderedDict([
    ("intro_synth", "HELLO AND WELCOME TO THE EXPERIMENT."),
    ("intro_natural_part1", "Hello! I'm a human. Welcome to the experiment."),
    ("intro_natural_part2", "So i'll be describing the route to you and you'll draw it on the map, are you ready to start?"),
    ("intro_natural_part3", "Great, lets get started"),
    ("intro_subsequent_natural", ["Okay, lets start again", "Ready for the next one?","Ready for the next one?","Ready for the next one?","Ready for the next one?","Ready for the next one?","Ready for the next one?",]),
    ("intro_subsequent_synth", "NEXT TRIAL"),
    ("lets_go_from", "Let's go from") ,
    ("end_natural", ["We're finished", "Okay, done", "Okay finished", "Okay finished", "Okay finished"]),
    ("end_synth", "End of route")
])

mt_phrases = OrderedDict()
mt_phrases.update(mt_phrases_exp_responses)
mt_phrases.update(mt_phrases_misc)
for v in mt_phrases_landmarks.values():
    mt_phrases.update(v)
    for exp_id, exp_phrase in v.items():
        mt_phrases[exp_id+"_LG"] = "Let's go from "+exp_phrase
for v in mt_phrases_instructions.values():
    mt_phrases.update(v)
