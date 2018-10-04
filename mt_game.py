__author__ = 'atullo2'

from mt_instructions import mt_instructions
from mt_phrases_text import mt_phrases_exp_responses, mt_phrases_landmarks
from mt_util import od_get

class EndGameException(Exception):
    pass

class MapTaskGame(object):
    def __init__(self, _ui, _instruction_set):
        self.ui = _ui

        self.instruction_set = _instruction_set
        self.first_instruction = True
        self.instructions = mt_instructions[self.instruction_set]
        self.instruction = None
        self.instruction_idx = -1

        self.landmarks = mt_phrases_landmarks[self.instruction_set]

        self.last_response = None

    def turn(self):
        response = self._exp_turn()
        # copy as this is not guaranteed to be unmodified
        self.last_response = response.copy()
        return response

    def _exp_turn(self):
        """Experimenter's turn -- respond to participant"""
        # right at the start -- auto-advance
        if self.first_instruction:
            self.first_instruction = False
            return self.next_instruction()
        # take experimenter input
        exp_choice = self.ui.exp_choice()
        if exp_choice in ["Q", "F", "G", "H", "I"]:
            return self.do_special(exp_choice)
        elif exp_choice in mt_phrases_exp_responses:
            return { "exp_response": exp_choice }
        else:
            raise NotImplementedError("Phrase for '{}' not implemented".format(exp_choice))

    def next_instruction(self):
        if self.instructions:
            self.instruction = self.instructions.pop(0)
            result = { "exp_response": self.instruction }
            self.instruction_idx += 1
            return result
        else: # special case, no instructions left, finish game?
            raise EndGameException()

    def current_landmark(self):
        return od_get(self.landmarks, self.instruction_idx)

    def do_special(self, exp_choice):
        if exp_choice == "Q": # last landmark
            return { "exp_response": self.current_landmark()+"_LG" }
        elif exp_choice == "F": # landmark for current statement ??
            return { "exp_response": self.current_landmark() }
        elif exp_choice == "G": # repeat last response
            return self.last_response
        elif exp_choice == "H": # repeat instruction
            return { "exp_response": self.instruction }
        elif exp_choice == "I": # next instruction
            return self.next_instruction()
