"""
Este módulo contiene helpers para prepro

Debemos añadir fichero de requirements para que importe automáticamente numpy. 
Poetry declara en el pyproject.toml la versión que neceistamos
"""

import numpy as np

def get_numerical_features(df):
    return df.select_dtypes(include=[np.number]).columns