import glob
import os

from model import predictInve


def predecir(tienda, semana):
    return predictInve(tienda, semana)


def actualizar():
    for f in glob.glob('fit.*.joblib'):
        os.remove(f)
