# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl
from Section import Section

class Wall:
    # Constructor
    def __init__(self, parameters = {}) :
        # Parameters
        # position: position of the wall
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]

        # Objects list
        self.objects = []

        # Adds a Section for this object
        self.parentSection = Section({'width': self.parameters['width'], \
                                      'height': self.parameters['height'], \
                                      'thickness': self.parameters['thickness'], \
                                      'color': self.parameters['color'],
                                      'position': self.parameters['position'],
                                      'orientation': self.parameters['orientation']})
        self.objects.append(self.parentSection)

    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]

    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self

    # Finds the section where the object x can be inserted
    def findSection(self, x):
        for item in enumerate(self.objects):
            if isinstance(item[1], Section) and item[1].canCreateOpening(x):
                return item
        return None

    # Adds an object
    def add(self, x):
        sec = self.findSection(x)
        assert sec

        newSec = sec[1].createNewSections(x)

        sections = sec[1].createNewSections(x)
        self.objects.pop(sec[0])
        self.objects.append(x) #on ajoute l'objet

        for k in newSec:
            self.objects.append(k) ##on ajoute toutes les nouvelles sections

        return self

    # Draws the faces
    #NOTE: c'est faux ? en tout cas revoir ./Section.py
    def draw(self):
        gl.glPushMatrix()
        #self.parentSection.drawEdges()
        for x in self.objects:
          x.draw()
        gl.glPopMatrix()



  
