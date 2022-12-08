## Importacion de librerías
import pandas as pd
import numpy as np 
import plotly.express as px
import datetime as dt
from sklearn import preprocessing
from sklearn.cluster import KMeans
from datetime import datetime
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import random
from sklearn.covariance import LedoitWolf
import sys
from sklearn.covariance import empirical_covariance
from scipy.spatial import distance
from sklearn.mixture import GaussianMixture

## Importacion datos
# df = pd.read_csv('D:/nuevo/universidad/Master/Proyecto_Integrador/bdCompletarAgrupRefinada.csv',  parse_dates=[2], infer_datetime_format= True)
# df["Unidades"] = pd.to_numeric(df["Unidades"])

dfinal = pd.DataFrame()

def predictInve(tienda,semana):
    ##Trae los datos con los que entrena el modelo, cambiar por las sentencias desde S3
    df = pd.read_csv('D:/nuevo/universidad/Master/Proyecto_Integrador/bdCompletarAgrupRefinada.csv',  parse_dates=[2], infer_datetime_format= True)
    df["UNIDADES"] = pd.to_numeric(df["UNIDADES"])
    dretu = pd.DataFrame()
    datSem = df[df['TIENDA'] == tienda]
    df_en = datSem.drop(columns = 'TIENDA')

    #Codificación de la columna Prendas
    encoder = preprocessing.LabelEncoder()
    enc1 = encoder.fit(df_en['PRENDA'])  #no se guardan las clases
    df_en['PRENDA']  = enc1.transform(df_en['PRENDA'])

    # Kmeans
    kmeans = KMeans(n_clusters = 25, random_state = 250).fit(df_en) #original df_en
    df_en['Cluster'] = kmeans.labels_

    dretu = seman(semana,df_en)
    return dretu

def seman(Semana, df):
    datSem = df[df['SEMANA'] == Semana]
    tam = len(datSem)
    prd = pd.DataFrame(columns=['PRENDA','UNIDADES'],index=range(tam))
    for i in range(len(datSem)):
        #print(datSem.iloc[i]['Cluster'])
        unidadesDat = df[df['Cluster'] == datSem.iloc[i]['Cluster']]
        #print(datSem.iloc[i]['Prenda'])
        unidadesDatre = unidadesDat['UNIDADES'][unidadesDat['PRENDA'] == datSem.iloc[i]['PRENDA']]
        prd.iloc[i] = (datSem.iloc[i]['PRENDA'], unidadesDatre.median())
        
    return prd

#dfinal = predictInve('MOLINOS 1',5)
# print(dfinal)