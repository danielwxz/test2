# -*- coding: utf-8 -*-
"""
Created on Thu Sep 5 10:22:14 2021

@author: dsoto@imn.ac.cr
"""


import os
#import pandas as pd
import numpy as np

def coherencia(serie1,serie2):
    # serie1 -> max
    # serie2 -> min
    
    indices = (serie1 <= serie2)
    #print(indices)
    serie1[indices] = np.nan
    serie2[indices] = np.nan
    
    return serie1, serie2

if __name__=="__main__":
    os.chdir('C:\\Users\\Usuario\\Documents\\IMN\\Proyectos\\Proyecto_RBD')
    
    c = 100
    s1 = np.random.rand(c)
    s2 = np.random.rand(c)
    
    s1, s2 = coherencia(s1,s2)

