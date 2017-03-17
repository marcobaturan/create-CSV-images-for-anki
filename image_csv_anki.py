# Auothor: Reset Reboot
# Collaborator: Marco garcía Baturan
# Date: 2017-2-8-W
# Theme: Education
# Licence: Open Source

"""This script is developed for create large decks of images in anki
    for create decks of concatenated images."""
 # import modules
import os
from os import listdir
from os.path import isfile, join
from tkinter import messagebox
import tkinter

# This give function in ani OS
if __name__ == "__main__":

    # Window control for show end process
    class Msgbox(object):

        # """ Constructor """
        def __init__(self, text):
            self.text = text
            window = tkinter.Tk()
            window.wm_withdraw()

        def msg(self):
            messagebox.showinfo("Imagenes Anki", self.text)

    # this get path, list and ordered images from directory
    path = raw_input('Introduce the path: ')
    directory = [f for f in listdir(path) if isfile(join(path, f))]  # get list from dir, empty because in dir
    directory.sort(key=lambda x: os.path.getmtime(x))  # this order by date
    images = ["<img src='{}/{}'>".format(path, elem) for elem in directory]  # give format html for flashcard
    previous_img = images[0]  # variable for array of images
    with open('output.csv', 'w') as f:
        for image in images[1:]:
            f.write(",".join([previous_img, image]) + "\n")
            previous_img = image
    # end message prompt
    print "The output.csv is build."

    # No CSV required
    # Output is two images in the same line
    # The next has the last image as the first

    # declared main function
    def main():
        ventana = Msgbox("Tarea finalizada.")
        ventana.msg()

# call main function
main()
