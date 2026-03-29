# if you're also digging through this file trying to fix tkinter errors,
# most linux repos don't package tkinter with python, but you can install it manually

import json, csv, tkinter as tk, time
from tkinter import (
    filedialog as fdialog
)

# ugly file selector

print("Please select your Octocon-format system data file.")
time.sleep(1)

filepath = fdialog.askopenfilename(title="Select your Octocon system data file", filetypes=[("JSON", "{*.json}")])

with open(filepath) as jf:
    jd = json.load(jf)

# ----- ALTER DATA -----

print("Select where to save your alter data.")
time.sleep(1)

sys = jd['alters']

csvra = open(fdialog.asksaveasfilename(title="Export alters file to", defaultextension='.csv'), 'w')
csvwa = csv.writer(csvra)

cntr = 0 # counter

for alter in sys: # lmao sorry had to
    if cntr == 0:
        # writes headers
        h = alter.keys()
        csvwa.writerow(h)
        cntr += 1

    #should write the rest
    csvwa.writerow(alter.values())

csvra.close()

# ----- FRONT DATA -----

print("Select where to save your fronting data.")
time.sleep(1)

front = jd['fronts']

csvrf = open(fdialog.asksaveasfilename(title="Export fronts file to", defaultextension='.csv'), 'w')
csvwf = csv.writer(csvrf)

cntr = 0 # reset counter

for log in front:
    if cntr == 0:
        h = log.keys()
        csvwf.writerow(h)
        cntr += 1

    csvwf.writerow(log.values())

csvrf.close()

# -----POLL DATA-----

print("Select where to save your poll data.")
time.sleep(1)

polldata = jd['polls']

csvrp = open(fdialog.asksaveasfilename(title="Export polls file to", defaultextension='.csv'), 'w')
csvwp = csv.writer(csvrp)

cntr = 0

for poll in polldata:
    if cntr == 0:
        h = poll.keys()
        csvwp.writerow(h)
        cntr += 1

    csvwp.writerow(poll.values())

csvrp.close()

# this is where i realized i could have probably just put this code in a for loop and forced file names.
# this is also where i decided i'm not rewriting this today.

# ----- TAG DATA -----

print("Select where to save your tag (groups) data.")
time.sleep(1)

tagdata = jd['tags']

csvrt = open(fdialog.asksaveasfilename(title="Export tags (groups) file to", defaultextension='.csv'), 'w')
csvwt = csv.writer(csvrt)

cntr = 0

for tag in tagdata:
    if cntr == 0:
        h = tag.keys()
        csvwt.writerow(h)
        cntr += 1

    csvwt.writerow(tag.values())

csvrt.close()

# ----- FIELDS DATA -----
# currently broken, yes i did comment out this entire bit and leave it in here
# maybe past me was right to not put this in a loop

'''
print("Attempting to export fields data. This is not guaranteed to work in all scenarios.")
print("If it fails here, all data before the error has still exported.")

jd["fields"] = json.load(jf["fields"])

print("Please select where to export fields data.")

csvrd = open(fdialog.asksaveasfilename(title="Export fields data to", defaultextension='.csv'), 'w')
csvwd = csv.writer(csvrd)

cntr = 0

for fldt in fields:
    if cntr == 0:
        h = fldt.keys()
        csvwd.writerow(h)
        cntr += 1

    csvwd.writerow(fldt.values())

csvrd.close()
'''

print("Not all data is preserved this way - please do not delete your Octocon data file!")
print("All done! Quitting...")
time.sleep(1)
exit()