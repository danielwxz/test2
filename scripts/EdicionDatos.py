# -*- coding: utf-8 -*-

"""
Created on Tue May 25 07:18:14 2021

@author: dsoto@imn.ac.cr
"""

import os
import pandas
#import numpy


os.chdir('C:\\Users\\Usuario\\Documents\\IMN\\Proyectos\\Proyecto_RBD')

# Datos descargados de la BD del IMN
met = pandas.read_csv('temp_Hora_69_abiertas.csv')
#met = pandas.read_csv('temp_Hora_69_abiertas-pruebas.csv')

# Hace la hora un int
hora_int = met['HORA']/100
hora_int = hora_int.astype(int)


# Separa las fecha 
fecha = met['FECHA'].str.split('/', expand=True)
dia = fecha[0]
mes = fecha[1]
anio = fecha[2]

hora_str = hora_int.astype(str)

for i in range(len(hora_int)):
    if hora_int[i] == 24:
        hora_int[i] = 0
    if hora_int[i] < 10:
        hora_str[i] = '0' + str(hora_int[i])

fecha_internacional = anio + '-' + mes + '-' + dia + ' ' + hora_str+':00:00'
met['FECHA'] = fecha_internacional


# Obtener estaciones y cuencas
estaciones = met['ESTACION'].unique()
cuencas = met['CUENCA'].unique()

for est in estaciones:
    datos_estacion = pandas.DataFrame()#columns = ['CUENCA' , 'ESTACION', 'FECHA', 'TEMP', 'ESTADO'])
    for m in range(len(met['ESTACION'])):
        if est == met['ESTACION'][m]:
            linea = [(met['CUENCA'][m],met['ESTACION'][m], met['FECHA'][m],met['TEMP'][m],met['ESTADO'][m])]
            #print(linea)
            datos_estacion = datos_estacion.append(linea)
            
    datos_estacion.columns = ['CUENCA' , 'ESTACION', 'FECHA', 'TEMP', 'ESTADO']
    # Guarda archivo csv
    print('TEMP_C'+str(met['CUENCA'][m])+'_E'+str(est)+'.csv')
    nombre = 'TEMP_C'+str(met['CUENCA'][m])+'_E'+str(est)+'.csv'
    datos_estacion.to_csv(nombre,index=False)