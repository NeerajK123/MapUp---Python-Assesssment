import pandas as pd

def filter_routes(df):

    avg_truck_by_route = df.groupby('route')['truck'].mean()


    selected_routes = avg_truck_by_route[avg_truck_by_route > 7].index.tolist()


    selected_routes.sort()

    return selected_routes


df = pd.read_csv('dataset-1.csv')


result = filter_routes(df)
print(result)
