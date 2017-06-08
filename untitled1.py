# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 10:10:43 2017

@author: Harleyhihew
"""

def CreateSLRTable(trans,state,Terms,nonTerms):
    table = [[0 for x in range(len(Terms)+len(nonTerms)+1)] for y in range(len(state)+1)]
    mixTnt = Terms+nonTerms   