__author__ = 'atullo2'

from itertools import chain
import os

from mt_instructions import mt_instructions
from mt_phrases_text import mt_phrases_instructions, mt_phrases

# In config, check descriptions exists for A1-10, B1-10 and no others
all_instruction_ids = [x+str(y) for x in ["A","B"] for y in range(1,11)]
assert set(chain(*mt_instructions.values())) == set(all_instruction_ids) # check order lists
assert set(chain(*mt_phrases_instructions.values())) == set(all_instruction_ids) # check phrases

def assertpresent(expected, found, subdir, errstr):
    assert not expected - found, errstr+" in {}: {}".format(subdir, str(expected - found))

def check_soundset(subdir):
    keys_found = set (x [:-4] for x in os.listdir("sounds/"+subdir))
    assertpresent(mt_phrases, keys_found, subdir, "Missing sound files ")

#check_soundset("dummy_sound_set")
