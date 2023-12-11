import pandas as pd

def calculate_distance_matrix(file_path):

    df = pd.read_csv(file_path)

    distance_matrix = df.pivot(index='from_id', columns='to_id', values='distance')

    distance_matrix = distance_matrix.fillna(0)

    distance_matrix = distance_matrix + distance_matrix.T

    for col in distance_matrix.columns:
        distance_matrix.at[col, col] = 0

    for row in distance_matrix.index:
        for col in distance_matrix.columns:
            if distance_matrix.at[row, col] == 0:

                known_routes = df[(df['from_id'] == row) & (df['to_id'] == col)]
                if not known_routes.empty:
                    distance_matrix.at[row, col] = known_routes['distance'].sum()

    return distance_matrix


result_df = calculate_distance_matrix('dataset-3.csv')


print(result_df)
