# -*- coding: utf-8 -*-
"""
Created on Mon Sep 9 14:37:32 2021

@author: dsoto@imn.ac.cr
"""


import os
#import pandas as pd
import numpy as np

def prueba_saltos(serie,jump):
    print(serie)
    
    for i in range(0, len(serie)):
        if i > 0:
            #print(serie[i],serie[i-1],np.abs(serie[i]-serie[i-1]))
            salto = np.abs(serie[i]-serie[i-1])
            if salto > jump:
                serie[i] = np.nan
            #print(serie[i],serie[i-1])
                
    return serie

if __name__=="__main__":
    os.chdir('C:\\Users\\Usuario\\Documents\\IMN\\Proyectos\\Proyecto_RBD')

    data = np.random.uniform(low=0.5, high=13.3, size=(20,))
    
    data = prueba_saltos(data,5)

