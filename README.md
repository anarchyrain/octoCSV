# Octocon Data Converter
This is just a command line tool I made for myself to save as much of my Octocon data as possible.

# What does it do?
Currently, it exports your Octocon alter data to a CSV file. This data is not fully human-readable at this moment in time, and it does not currently include poll, tag, or accurate custom fields data - I mostly wrote this to get the avatar links before Octocon's servers shut down (I know they said avatar servers would stay online a bit longer, but I'm not sure how much longer).

This converter is written in Python and currently requires the full Octocon format to work, as far as I know. You're welcome to try it with other formats, though.

# What can I do with it?
I used it to get my avatar URLs more easily and download them. You do still have to copy the links into the command, but it was a lot easier from a CSV.

`wget -P [directory to download to] [avatar links]`

# To-Do
- Automate avatar downloads in some way
- Create exports for all data
- Get as much data into human-readable format as possible
- Attempt to convert between different formats in some way?

# Known issues
- Some people may need to install the tkinter library manually. It's usually packaged with Python on Windows and MacOS; on Linux, it often comes separately.

> arch: `sudo pacman -S tk`\n
> ubuntu/debian: `sudo apt install python3-tk`\n
> fedora: `sudo dnf install python-tkinter`

- User and fields data export doesn't currently work. These keys are stored in a way that neither I nor the JSON libraries can figure out, apparently.