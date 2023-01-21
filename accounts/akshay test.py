import pandas as pd

try:
    d = {'col1': [1, 2,10,12,None], 'col2': [1, None ,10,12,40]}
    df = pd.DataFrame(data=d)
    df.loc[df.col1 != None], ['col1', 'col2']
    print("*************")
except Exception as e:
    print(e)