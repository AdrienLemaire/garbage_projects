#!/usr/bin/python
# -*- coding:Utf-8 -*-
'''
File: ocr_base.py
Author: Adrien Lemaire
Description: Simple orc for character detection, respectful of PEP8 standard
'''

import PIL
import Image
import numpy
import ImageOps
from sys import argv
from termcolor import colored

IMG_FILE = "imageTest.png"
COLOR_TEXT = 255
COLOR_BACKGROUND = 10
SUBMATRIX_INDICE = 0


def OuvrirImg(path):
    """Return an image in its matrix form"""
    Img = Image.open(str(path))
    Img1 = ImageOps.grayscale(Img)
    largeur, hauteur = Img1.size
    imdata = Img1.getdata()
    tab = numpy.array(imdata)
    matrix = numpy.reshape(tab, (hauteur, largeur))
    return matrix


class Container(object):
    """Object containing the matrix and submatrix"""

    def __init__(self, iniMatrix):
        self.iniMatrix = iniMatrix
        self.subMatrixDict = {}
        self.create_submatrix()

    class SubMatrix:
        """Matrix representing a character"""

        def __init__(self, x, y, value):
            self.positionIni = [x, y]
            self.nextPoint = []
            self.nextLinePoints = []
            self.availablePoints = []
            self.data = [[]]
            self.addPoint(x, y, value)

        def __str__(self):
            """Return the representation of the submatrix"""
            return "\n".join([repr(line) for line in self.data])

        def addPoint(self, x, y, value, line="end"):
            """Add a point to the SubMatrix"""
            if line == "end":
                line = len(self.data)-1
            nbOfZeros = x - self.positionIni[0] -\
                    len(self.data[line])
            for i in range(nbOfZeros):
                self.data[line].append(0)
            self.data[line].append(value)
            self.nextLinePoints.append([x, y + 1])
            self.nextPoint = [x + 1, y]
            if self.nextPoint not in self.availablePoints:
                self.availablePoints.append(self.nextPoint)

        def addLine(self, nbLines=0):
            """Add a new line to the SubMatrix"""
            if nbLines != 0:
                for line in range(nbLines):
                    self.data.insert(0, [])
            else:
                self.data.append([])
                self.nextPoint = self.nextLinePoints[0]
                self.availablePoints = list(self.nextLinePoints)
                self.nextLinePoints = []

    def create_submatrix(self):
        """Find forms in the iniMatrix and put them in submatrix"""
        global SUBMATRIX_INDICE
        y = 0
        while y < len(self.iniMatrix):
            x = 0
            while x < len(self.iniMatrix[y]):
                if self.iniMatrix[y][x] > COLOR_BACKGROUND:
                    """If the point is not background color"""
                    if len(self.subMatrixDict) > 0:
                        matched_subMatrix = []
                        ordened_dict = sorted(self.subMatrixDict.iteritems())
                        for key, instance in ordened_dict:
                            if [x, y] in instance.availablePoints:
                                position = len(instance.data) -1
                                if x > instance.positionIni[0] and\
                                        instance.data[position] == []:
                                    for i in range(x - instance.\
                                            positionIni[0]):
                                        instance.data[position].append(0)
                                instance.addPoint(x, y, self.iniMatrix[y][x])
                                matched_subMatrix.append(key)
                        if not matched_subMatrix:
                            name = "submatrix" + str(SUBMATRIX_INDICE)
                            self.subMatrixDict[name] = \
                                    self.SubMatrix(x, y, self.iniMatrix[y][x])
                            SUBMATRIX_INDICE += 1
                        elif len(matched_subMatrix) > 1:
                            self.join2submatrix(matched_subMatrix)
                    else:
                            name = "submatrix" + str(SUBMATRIX_INDICE)
                            self.subMatrixDict[name] = \
                                    self.SubMatrix(x, y, self.iniMatrix[y][x])
                            SUBMATRIX_INDICE += 1
                x += 1
            if not y == len(self.iniMatrix)-1:
                for key, instance in self.subMatrixDict.iteritems():
                    if instance.nextLinePoints:
                        instance.addLine()
                    elif instance.data[len(instance.data) - 1] == []:
                        del instance.data[len(instance.data) - 1]
            y += 1

    def join2submatrix(self, keys):
        """Construct 1 submatrix based on 2 smaller one stuck together"""
        if self.subMatrixDict[keys[0]].positionIni <=\
           self.subMatrixDict[keys[1]].positionIni:
            matrix1 = self.subMatrixDict[keys[0]]
            matrix2 = self.subMatrixDict[keys[1]]
        else:
            matrix1 = self.subMatrixDict[keys[1]]
            matrix2 = self.subMatrixDict[keys[0]]
        if matrix1.nextPoint[1] == matrix2.positionIni[1]:
            if matrix2.positionIni[0] >= matrix1.positionIni[0]:
                """matrix2 has only one point"""
                nbOfZeros = matrix2.positionIni[0] - matrix1.positionIni[0]
                matrix1.data[len(matrix1.data) - 1] = [0] * nbOfZeros
            else:
                nbOfZeros = matrix1.positionIni[0] - matrix2.positionIni[0]
                for i in range(len(matrix1.data)-1):
                    matrix1.data[i] = [0] + matrix1.data[i]
                matrix1.data[len(matrix1.data) - 1] = []
            for i in range(len(matrix2.data[0])):
                x = matrix2.positionIni[0] + i
                y = matrix2.positionIni[1]
                value = matrix2.data[0][i]
                matrix1.addPoint(x, y, value)
        elif matrix1.positionIni[0] < matrix2.positionIni[0]:
            startIter = matrix2.positionIni[1] - matrix1.positionIni[1]
            if startIter < 0:
                matrix1.addLine(abs(startIter))
                startIter = 0
            for i in range(startIter, len(matrix1.data) - 1):
                for j in range(len(matrix2.data[0])):
                    x = matrix2.positionIni[0] + j
                    y = matrix2.positionIni[1]
                    value = matrix2.data[0][j]
                    matrix1.addPoint(x, y, value, i)
        if self.subMatrixDict[keys[0]].positionIni <=\
           self.subMatrixDict[keys[1]].positionIni:
            del self.subMatrixDict[keys[1]]
        else:
            del self.subMatrixDict[keys[0]]


def imgToMatrix(file, color_text, color_bg):
    """Function which will convert an image into matrix"""
    global IMG_FILE, COLOR_TEXT, COLOR_BACKGROUND
    IMG_FILE = file
    COLOR_TEXT = color_text
    COLOR_BACKGROUND = color_bg
    iniMatrix = OuvrirImg(file)
    my_container = Container(iniMatrix)
    for m_name, m_values in sorted(my_container.subMatrixDict.iteritems(), \
            key=lambda tuple: tuple[1].positionIni):
        print colored(m_name + ":", "red"), "\n", m_values


if __name__ == "__main__":
    """List of possibles arguments:
        - argv[1] : IMG_FILE
        - argv[2] : COLOR_TEXT
        - argv[3] : COLOR_BACKGROUND"""
    if len(argv) > 1:
        IMG_FILE = argv[1]
    if len(argv) == 4:
        COLOR_TEXT = argv[1]
        COLOR_BACKGROUND = argv[2]
    imgToMatrix(IMG_FILE, COLOR_TEXT, COLOR_BACKGROUND)
