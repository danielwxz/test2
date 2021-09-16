# -*- coding: utf-8 -*-
"""
Created on Thu Agu 29 07:18:14 2021

@author: dsoto@imn.ac.cr
"""


import os
#import pandas as pd
import numpy as np

def test_4sd(serie):
    std = serie.std()
    
    lim_superior = std+std*4
    lim_inferior = std-std*4
    
    print('std',std,lim_inferior,lim_superior)
    
    serie[serie > lim_superior] = np.nan
    serie[serie < lim_inferior] = np.nan
    
    return serie

if __name__=="__main__":
    os.chdir('C:\\Users\\Usuario\\Documents\\IMN\\Proyectos\\Proyecto_RBD')

    data = np.random.uniform(low=0.5, high=13.3, size=(500,))
    data[34] = 25.2
    data[58] = -120.4
    data[123] = 40.8
    data[345] = -30.69
    data[456] = 139.7
    
    data = test_4sd(data)