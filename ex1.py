import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_data():
    df=pd.read_csv(r"C:\abhi\ainee\Visadataset - Visadataset.csv")
    return(df)
def frec():
    df1=read_data()
    keys=df1['continent'].value_counts().keys()
    values=df1['continent'].value_counts().values
    feq_df=pd.DataFrame(zip(keys,values),columns=['class','freq'])
    return(keys,values)
def Bar_chart():
    keys,values=frec()
    plt.bar(keys,values)
    plt.savefig('continent.jpg')
Bar_chart()