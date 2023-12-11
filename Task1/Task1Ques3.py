import pandas as pd

def get_bus_indexes(df):

    bus_mean = df['bus'].mean()

    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()


    bus_indexes.sort()

    return bus_indexes


df = pd.read_csv('dataset-1.csv')


result = get_bus_indexes(df)
print(result)
