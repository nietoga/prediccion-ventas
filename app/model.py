import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import KMeans

import os


def predictInve(tienda, semana):
    ##Trae los datos con los que entrena el modelo, cambiar por las sentencias desde S3
    df = pd.read_csv(os.getenv("DATABASE_SOURCE"), parse_dates=[2],
                     infer_datetime_format=True)
    df["UNIDADES"] = pd.to_numeric(df["UNIDADES"])
    dretu = pd.DataFrame()
    datSem = df[df['TIENDA'] == tienda]
    df_en = datSem.drop(columns='TIENDA')

    # Codificación de la columna Prendas
    encoder = preprocessing.LabelEncoder()
    enc1 = encoder.fit(df_en['PRENDA'])  # no se guardan las clases
    df_en['PRENDA'] = enc1.transform(df_en['PRENDA'])

    # Kmeans
    kmeans = KMeans(n_clusters=25, random_state=250).fit(df_en)  # original df_en
    df_en['Cluster'] = kmeans.labels_

    # Volver a ponerle a las prendas su valor
    df_en['PRENDA'] = enc1.inverse_transform(df_en['PRENDA'])

    dretu = seman(semana, df_en)
    return dretu


def seman(Semana, df):
    datSem = df[df['SEMANA'] == Semana]
    tam = len(datSem)
    prd = pd.DataFrame(columns=['PRENDA', 'UNIDADES'], index=range(tam))
    for i in range(len(datSem)):
        unidadesDat = df[df['Cluster'] == datSem.iloc[i]['Cluster']]
        unidadesDatre = unidadesDat['UNIDADES'][unidadesDat['PRENDA'] == datSem.iloc[i]['PRENDA']]
        prd.iloc[i] = (datSem.iloc[i]['PRENDA'], int(unidadesDatre.median()))

    return prd
