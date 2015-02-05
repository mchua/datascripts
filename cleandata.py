#!/usr/bin/env python

# cleandata.py
# by Mel Chua
# cleans irssi-generated IRC logs to make interesting conversations
# more visible to human readers
# NOTE: NOT FINISHED YET! 2/4/15

# library for working with OS-specific commands -- files, folders, etc.
import os

# Variable declarations, customize
folderpath = "C:\\Users\\mchua\\Dropbox\\CREU\\Data\\cleaned_data"

# dummy function definition right now
def clean_logfile(logtext):
    print logtext[0]

if __name__ == "__main__":
    # Loop through every file in the stated folder
    for filename in os.listdir(folderpath):
        # Only run this script on logfiles
        if filename[-4:] == ".log":
            filepath = os.path.join(folderpath, filename)
            infile = open(filepath, 'r')
            clean_logfile(infile.readlines())
            infile.close()
