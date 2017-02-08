# Auothor: Reset Reboot
# Collaborator: Marco garcía Baturan
# Date: 2017-2-8-W
# Theme: Education
# Licence: Open Source

"""This script is developed for create large decks of images in anki
    for create decks of concatenated images."""
    
import os
from os import listdir
from os.path import isfile, join

if __name__ == "__main__":
    path = 'put your path here'
    directory = [f for f in listdir(path) if isfile(join(path, f))]  # get list from dir, empty because in dir
    images = ["<img src='{}' >".format(elem) for elem in directory]  # give format html in anki
    previous_img = images[0]  # variable for array of images
    with open('output.csv', 'w') as f:
        for image in images[1:]:
            f.write(",".join([previous_img, image]) + "\n")
            previous_img = image

            # No CSV required
            # Output is two images in the same line
            # The next has the last image as the first
