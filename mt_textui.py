__author__ = 'atullo2'

import csv
import platform
from os.path import join
import os
import pprint
import random
import subprocess
import time

from mt_phrases_text import mt_phrases, mt_phrases_exp_responses, mt_phrases_landmarks
from mt_util import checked_input, pprint_dict

if platform.system() == "Windows":
    PLAY_SOUND_CMD = "start"
elif platform.system() == "Linux":
    PLAY_SOUND_CMD = "play"
elif platform.system() == "Darwin":
    PLAY_SOUND_CMD = "afplay"
else:
    assert False, "Unrecognised operating system: "+platform.system()

def load_sound_lengths(soundfiles):
    result = {}
    path = os.path.join("data", soundfiles+".csv")
    f = open(path, "r")
    reader = csv.reader(f)
    for row in reader:
        result[row[0]] = float(row[1])
    return result

class MTTextUI(object):
    def __init__(self, verbose=True):
        self.verbose = verbose
        self.sound_lengths = {
            "synth": load_sound_lengths("synth_nina"),
            "natural": load_sound_lengths("natural_rosie")
        }

    FMT = """\
Experiment response: {exp_response_out}
Experiment response chosen: {exp_response_choice}
"""

    EXP_CHOICE_SHORT_HELP = "Y/N/LT/LV/RT/RV/AT/AV/BT/BV/UT/UV/DT/DV/X/Y/Z/A/B/C/D/E/F/G/H/I"
    EXP_CHOICE_LONG_HELP_EXTRA = [
        ("Q", "Let's go from [last landmark]"),
        ("F", "[the landmark for the current statement]"),
        ("G", "[Repeat last statement]"),
        ("H", "[Repeat the initial instruction]"),
        ("I", "[Move on to the next instruction]")
    ]

    PROMPT = "Experiment response (? help, ?? long help, ?A/B landmarks for set): "

    SOUNDFILE_SETS = ["SYNTH_NINA", "NATURAL_ROSIE"]

    def config(self):
        self.show("Starting new run")
        ppt = checked_input("Participant number: ", r"\d+", "Input must be a number.")
        instruction_set = checked_input("Instruction set to use first: ", ["A", "B"])
        soundfiles = checked_input("Sound file set: ", self.SOUNDFILE_SETS)
        return {
            "ppt": int(ppt),
            "instruction_set": instruction_set,
            "sound_set": soundfiles.upper()
        }

    def print_config(self, c):
        self.show(pprint.pformat(c))

    def pause(self, msg):
        _ = raw_input(msg)

    def end_choice(self):
        end_response = checked_input("Normal end response or yes (E/Y)?", ["E", "Y"])
        return end_response

    def exp_choice(self):
        acceptable = list(mt_phrases_exp_responses.keys())
        acceptable += ["Q", "F", "G", "H", "I"]
        acceptable += ["?", "??", "?A", "?B"] # add help
        while True:
            exp_response = checked_input(self.PROMPT, acceptable)
            if exp_response == "?":
                self.show("/".join(acceptable))
            elif exp_response == "??":
                help_dict = mt_phrases_exp_responses.copy()
                for k, v in self.EXP_CHOICE_LONG_HELP_EXTRA:
                    help_dict[k] = v
                self.show(pprint_dict(help_dict))
            elif exp_response in ["?A", "?B"]:
                landmarks = mt_phrases_landmarks[exp_response[1]]
                self.show(pprint_dict(landmarks))
            else:
                return exp_response

    def show_turn(self, turn):
        # change exp_response and phrase_response fields to human-readable responses, if present
        choice, out = self.exp_response_randomise(turn["exp_response"])
        turn["exp_response_out"], turn["exp_response_choice"] = out, choice
        # print text
        self.show(self.FMT.format(**turn))
        # play sound
        self.play(turn["sound_set"], turn["exp_response"], choice)
        del turn["exp_response_out"]

    def exp_response_randomise(self, exp_response):
        r = mt_phrases[exp_response]
        if type(r) == type(''):
            return 0, r
        else:
            idx = random.randrange(len(r))
            return idx+1, r[idx]

    def show(self, txt):
        print(txt)

    def play(self, sound_set, sound_id, sound_choice):
        self.show("Playing sound {}/{} from {} with {}".format(
            sound_id, sound_choice, sound_set, PLAY_SOUND_CMD)
        )
        if sound_choice == 0:
            sound_filename = "{}.wav".format(sound_id)
        else:
            sound_filename = "{}_choice{}.wav".format(sound_id, sound_choice)
        sound_pathname = join("sounds", sound_set.lower(), sound_filename)
        devnull = open(os.devnull, "w")
        # how much longer is the natural sound?
        try:
            natural_length = self.sound_lengths["natural"][sound_filename]
            synth_length = self.sound_lengths["synth"][sound_filename]
            pause_t = natural_length - synth_length
            if sound_set.startswith("synth"): # is synth
                if pause_t > 0: # natural > synth
                    # pad by the difference
                    print "Pausing for {:.2f}s".format(pause_t)
                    time.sleep(pause_t)
            else: # is natural
                if pause_t < 0: # synth > natural
                    # pad by the difference
                    print "Pausing for {:.2f}s".format(-pause_t)
                    time.sleep(-pause_t)
        except KeyError:
            print "Couldn't calculate pause for "+sound_filename
        subprocess.call([PLAY_SOUND_CMD, sound_pathname], stdout=devnull, stderr=devnull)
        devnull.close()

if __name__ == "__main__":
    ui = MTTextUI()
    ui.play("SYNTH_NINA", "N", 0)