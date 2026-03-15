# if you're also digging through this file trying to fix tkinter errors,
# most linux repos don't package tkinter with python, but you can install it manually
# arch: sudo pacman -S tk
# ubuntu/debian: sudo apt install python3-tk
# fedora: sudo dnf install python-tkinter (maybe?)
# if that doesn't work... idk, sorry

# imports libraries
import json, csv, tkinter as tk, time
from tkinter import (
    filedialog as fdialog
)

# ugly file selector

filepath = fdialog.askopenfilename(title="Select your system data file", filetypes=[("JSON", "{*.json}")])

# loads it

with open(filepath) as jf:
    jd = json.load(jf)

sys = jd['alters']

csvf = open(fdialog.asksaveasfilename(title="Export alters file to", defaultextension='.csv'), 'w')
csvw = csv.writer(csvf)

cntr = 0 # counter

# tries really hard to create a CSV file

for alter in sys: # lmao sorry had to
    if cntr == 0:
        # writes headers
        h = alter.keys()
        csvw.writerow(h)
        cntr += 1

    #should write the rest
    csvw.writerow(alter.values())

csvf.close()

print("Currently, only alter data is converted - please do not delete your Octocon data file!")
print("All done! Quitting...")
# waits a couple seconds
time.sleep(2)
exit()