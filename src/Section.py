# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

class Section:
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
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False

        # Objects list
        self.objects = []

        # Generates the wall from parameters
        self.generate()

    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]

    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self

    # Defines the vertices and faces
    def generate(self):
        self.vertices = [ # dans le bon sens cette fois ci (important pour les tests)
                [0,0,0], 
                [0, 0, self.parameters['height']], 
                [self.parameters['width'], 0, self.parameters['height']],
                [self.parameters['width'], 0, 0],
                
                [0, self.parameters['thickness'], 0 ], 
                [0, self.parameters['thickness'], self.parameters['height']], 
                [self.parameters['width'],  self.parameters['thickness'], self.parameters['height']],
                [self.parameters['width'],  self.parameters['thickness'], 0]
                ]
        
        self.faces = [
                [0, 3, 2, 1],
                [1, 2, 6, 5],
                [5, 6, 7, 4],
                [0, 3, 7, 4],
                [2, 3, 7, 6],
                [1, 0, 4, 5]
                ]   


    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        # A compléter en remplaçant pass par votre code
        pass

    # Creates the new sections for the object x
    def createNewSections(self, x):
        # A compléter en remplaçant pass par votre code
        pass

    # Draws the edges
    def drawEdges(self):
        #TODO: ici y faut refaire en utilisant generate(), et self.vertices, self.faces
        self.generate()
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE) # on trace les faces : GL_FILL
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.5*0.05, 0.5*0.05, 0.5*0.05]) # Couleur plus foncée
        for face in self.faces:
          for vertex in face:
            gl.glVertex3fv(self.vertices[vertex])
        gl.glEnd()

      
        ##ARETE ENTRE LES DEUX
        #1
        gl.glBegin(gl.GL_LINES) # Tracé des arêtes 
        for face in self.faces:
          for vertex in face:
            gl.glVertex3fv(self.vertices[vertex])
        gl.glEnd()



    # Draws the faces
    #TODO: meme chose ici avec self.vertices
    def draw(self):
        gl.glPushMatrix()
        gl.glTranslatef(self.parameters['position'][0] , self.parameters['position'][1], self.parameters['position'][2])
        self.drawEdges()
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace les faces : GL_FILL
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen
        for face in self.faces:
          for vertex in face:
            gl.glVertex3fv(self.vertices[vertex])
        gl.glEnd()
        gl.glPopMatrix()