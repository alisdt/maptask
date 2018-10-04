__author__ = 'atullo2'

# From Korin Richmond (CSTR):
#
# Sure, no problem - if you just need straight synthesis of 900 sentences, the easiest for you would probably just be to use the CGI interface directly.
#
# In other words, a script (e.g. python) which accesses
#
# http://www.cstr.ed.ac.uk/cgi-bin/cstr/festivalspeak.cgi
#
# directly.  The fields you need to set in your POST request would be:
#
# voice (=nick2)
# UserText (= the text to synthesise)

# OK. I've added a flag to the cgi script to specify no filtering
# In your request to the cgi, just set an additional field "FilterSwearWords" to "off", and you'll be able to freely
# synthesise whatever you like ;)


import sys
sys.path.append("..")

from itertools import chain
from os.path import join, exists
import time
import urllib as ul
import urllib2 as ul2

from mt_phrases_text import mt_phrases, mt_phrases_landmarks

ALL_LANDMARKS = list(chain(*(x.keys() for x in mt_phrases_landmarks.values())))
FESTIVALSPEAK_URL = "http://www.cstr.ed.ac.uk/cgi-bin/cstr/festivalspeak.cgi"
OUT_PATH = "/home/alisdair/ppls/tangramwizard/branches/maptask/sounds/synth_nina"
COURTESY_DELAY = 15 # delay in seconds, to avoid overloading the server

def festivalspeak_get(text):
    text = text.replace("tangram", "shape")
    post_data = ul.urlencode({'voice': 'nina', 'UserText': text, 'FilterSwearWords': 'off'})
    req = ul2.urlopen(FESTIVALSPEAK_URL, post_data)
    return req.read()

def festival_to_file(text, filename):
    if not exists(filename):
        wav_data = festivalspeak_get(text)
        open(filename,"w").write(wav_data)
        time.sleep(COURTESY_DELAY)

for exp_id, exp_text in mt_phrases.items():
    if type(exp_text) == type([]):
        choices = range(1,len(exp_text)+1)
        for choice in choices:
            out_filename = join(OUT_PATH, exp_id+"_choice{}.wav".format(choice))
            festival_to_file(exp_text[choice-1], out_filename)
    else:
        out_filename = join(OUT_PATH, exp_id+".wav")
        festival_to_file(exp_text, out_filename)
        if exp_id in ALL_LANDMARKS:
            out_filename_lg = join(OUT_PATH, exp_id+"_LG.wav")
            festival_to_file("Lets go from "+exp_text, out_filename_lg)
