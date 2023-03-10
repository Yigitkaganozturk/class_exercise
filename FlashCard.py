# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 10:23:11 2021

@author: user
"""

class FlashCard:
    
    def __init__(self, question, answer, difficulty):
        self.__question = question
        self.__answer = answer
        self.setDifficulty(int(difficulty))
        
    def setQuestion(self, question):
        self.__question = question
    
    def getQuestion(self):
        return self.__question
    
    def setAnswer(self, answer):
        self.__answer = answer
    
    def getAnswer(self):
        return self.__answer
    
    def setDifficulty(self, difficulty):
        if difficulty >= 1 and difficulty <= 5:
            self.__difficulty = difficulty
        else:
            self.__difficulty = 0
    
    def __formatOutput( self, output ):
        if output == 'Q':
            data = self.__question
        else:
            data = self.__answer
        
        result = ( '*' * (len(data) + 10)) + '\n'
        result += 3 * (('*' + (4 * ' ') + (' ' * len(data)) + (4 * ' ') + '*' + '\n'))
        result += '*' + (4 * ' ') + data + (4 * ' ') + '*' +'\n'
        result += 3 * (('*' + (4 * ' ') + (' ' * len(data)) + (4 * ' ') + '*' + '\n'))
        result += ( '*' * (len(data) + 10)) + '\n'
        return result
    
    def showFlashCard( self ):
        print( self.__formatOutput('Q'))
        
    def flipFlashCard( self ):
        print( self.__formatOutput('A'))
        
    def __eq__(self, other):
        return self.__question.lower() == other.__question.lower() and self.__answer.lower() == other.__answer.lower()
    
    def __repr__( self ):
        return self.__question + '/' +self.__answer + ':' + str(self.__difficulty)
    def __lt__(self,obj):
        if self.__difficulty<obj.__difficulty:
            return True
        elif self.__difficulty==obj.__difficulty:
            return self.__question<obj.__question
        