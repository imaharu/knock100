import os
import sys
import random
if not(os.path.isfile("pos_and_neg")):
    with open("pos_and_neg", "w") as write_lines:
        with open("rt-polarity.pos", "r") as read_lines:
            for line in read_lines:
                write_lines.write("+1 " + line)
        with open("rt-polarity.neg", "r") as read_lines:
            for line in read_lines:
                write_lines.write("-1 " + line)

# gshuf pos_and_neg > sentiment.txt