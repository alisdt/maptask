__author__ = 'atullo2'

import csv
from datetime import datetime
import json
import os
import sys

from mt_game import MapTaskGame
from mt_textui import MTTextUI

import mt_phrasecheck     # <- this actually runs code to check phrases & ids

from mt_game import EndGameException

STATE_FILENAME = "state.json"

HELLO = """\
Welcome to Map Task.
Type "exit" at any prompt to exit the application (data may be lost).


"""

PPT_FILE_EXISTS_ERROR = """\
An output file already exists for that participant and trial: {}
The application will now exit.
"""

COLS = (
    "ppt",
    "trial",
    "sound_set",
    "time",
    "instruction_set",
    "order2",
    "exp_response",
    "exp_response_choice"
)

def start_log(state):
    csv_filename = "maptask_log_ppt{:03d}_{}_{}_trial{}.csv".format(
        int(state["ppt"]), state["sound_set"], state["instruction_set"], state["trial"]
    )
    if os.path.exists(os.path.join(".", csv_filename)):
        sys.stderr.write(PPT_FILE_EXISTS_ERROR.format(csv_filename))
        sys.exit(3)
    csv_file = open(csv_filename,"wb")
    out_csv = csv.DictWriter(csv_file, COLS)
    out_csv.writeheader()
    return out_csv

def load_state():
    # if there's an existing game state file, check that ppt and trial match
    if os.path.exists(STATE_FILENAME):
        return json.load(open(STATE_FILENAME, "rb"))
    else:
        return None

def save_state(state):
    if state["trial"] == 3:
        if state["order2"] == 1:
            # done with first map, switch to second
            if state["instruction_set"] == "A":
                state["instruction_set"] = "B"
            else:
                state["instruction_set"] = "A"
            if state ["sound_set"] == "synth_nina":
                state ["sound_set"] = "natural_rosie"
            else:
                state ["sound_set"] = "synth_nina"
            state["trial"] = 0 # will be incremented on load
            state["order2"] = 2
        else:
            # done with this participant, delete existing state file
            os.remove(STATE_FILENAME)
            return
    json.dump(
        state,
        open(STATE_FILENAME, "wb"),
        sort_keys=True,
        indent=4,
        separators=(',', ': ')
    )

def config_from_state(c):
    return c

def sayit(ui, exp_response, config):
    # create a dummy "turn" and run this to say something
    # used for intros
    dummy_turn = { "exp_response": exp_response }
    dummy_turn.update(config)
    ui.show_turn(dummy_turn)

def do_intro(ui, state):
    if state ["trial"] == 1:
        ui.pause("Press ENTER to say the trial intro phrase.")
        if state["sound_set"].lower().startswith("synth"):
            sayit(ui, "intro_synth", state)
        else:
            sayit(ui, "intro_natural_part1", state)
            ui.pause("Press ENTER ")
            sayit(ui, "intro_natural_part2", state)
            ui.pause("Press ENTER ")
            sayit(ui, "intro_natural_part3", state)
    else:
        ui.pause("Press ENTER to say the trial intro phrase.")
        if  state["sound_set"].lower().startswith("synth"):
            sayit(ui, "intro_subsequent_synth", state)
        else:
            sayit(ui, "intro_subsequent_natural", state)

def game_over(ui, config):
    end_response = ui.end_choice()
    if end_response == "Y":
        sayit(ui, "Y", config)
    else:
        if config["sound_set"].lower().startswith("synth"):
            sayit(ui, "end_synth", config)
        else:
            sayit(ui, "end_natural", config)

def run(ui, log=True):
    ui.show(HELLO)
    state = load_state()
    if state is None:
        config = ui.config()
        state = config.copy()  # will also hold prev. successful descriptions
        state["trial"] = 0
        state["order2"] = 1
    state["trial"] += 1
    config = config_from_state(state)

    do_intro(ui, config)

    if log:
        out_csv = start_log(state)


    ui.pause("Press ENTER to start the timer and continue.")
    time_start = datetime.now()
    game = MapTaskGame(ui, config["instruction_set"])
    while True:
        try:
            turn = game.turn()
        except EndGameException:
            game_over(ui, config)
            break
        turn.update(config)
        turn["time"] = (datetime.now() - time_start).total_seconds()
        ui.show_turn(turn)
        if log:
            out_csv.writerow(turn)

    save_state(state)

if __name__ == "__main__":
    ui = MTTextUI(verbose=False)
    run(ui)
