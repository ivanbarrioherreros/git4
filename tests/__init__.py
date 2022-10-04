import pandas as pd

from tests.test_preprocessing import get_numerical_features

def test_get_numerical_features_simple():
    """En este vamos a probar a distinguir entre str y int"""

    df = pd.DataFrame({
    "numerica": [5],
    "categorica": ["rojo"]
    })

    # assert es "como un if" pero falla si la condición 
    # es falsa. Esto es ideal para los test.

    assert get_numerical_features(df) == ["numerica"]