#!/usr/bin/python
# -*- coding:Utf-8 -*-
'''
File: dict_generation.py
Author: Adrien Lemaire
Description: Generate a dictionary of matrix
'''

from Image import new
from ImageDraw import Draw
from ImageFont import truetype
from subprocess import call
from sys import argv
from termcolor import colored
from ocr_base import imgToMatrix

DIR = "char_img"
FONT = "Arial.ttf"


def createImage(letter, i):
    size = font.getsize(letter)
    char = new("L", size, 0)
    drawChar = Draw(char)
    drawChar.text((0, 0), letter, font=font, fill=255)
    path = DIR + "/ascii_" + i + ".bmp"
    char.save(path)
    return path


if __name__ == "__main__":
    if len(argv) > 1:
        DIR = argv[1]
    if len(argv) == 3:
        FONT = argv[2]

    call(["mkdir", DIR])
    font = truetype(FONT, 20)

    for i in range(33, 127):
        '''This will create a Matrix for each ascii printable character'''
        letter = unicode(chr(i))
        img = createImage(letter, str(i))
        print colored("character '" + letter + "' :", "blue")
        imgToMatrix(img, 255, 0)
