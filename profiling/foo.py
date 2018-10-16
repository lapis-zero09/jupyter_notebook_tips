
import numpy as np
import pandas as pd
from time import sleep

def foo():
    df = pd.DataFrame(np.empty((100, 200)))
    sleep(2)
    for _ in range(50):
        df = df.applymap(lambda x: x+1000)
    return df.values