__author__ = 'atullo2'

import re
import sys

def od_get(d, idx):
    # index an OrderedDict, inefficient but we have small numbers here
    i = iter(d)
    result = i.next() # for idx = 0
    for _ in range(idx):
        result = i.next()
    return result

def pprint_dict(d):
    spacing = max(len(k) for k in d.keys())+1
    fmt = '{: <'+str(spacing)+'}{}'
    return '\n'.join(fmt.format(k, v) for k, v in d.items())

def checked_input(prompt, in_constraint, err=None):
    while True:
        text_in = raw_input(prompt)
        if text_in == "exit":
            sys.exit(2)
        if isinstance(in_constraint, list):
            if text_in.upper() in in_constraint:
                return text_in.upper()
            else:
                print("Input must be one of "+", ".join(in_constraint))
        else:
            if re.match(r"\A("+in_constraint+r")\Z", text_in):
                return text_in
            elif err:
                print(err)

def test():
    from mt_phrases_text import mt_phrases_landmarks
    print pprint_dict(mt_phrases_landmarks["A"])

if __name__ == "__main__":
    test()