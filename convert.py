from operator import index
import pandas as pd

data = pd.read_csv(r'data\sample_runtime.csv')

data = data.fillna("")

# data.to_records(index=False)

data.to_json(orient='values')