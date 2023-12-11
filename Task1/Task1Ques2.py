import pandas as pd


def generate_car_matrix(file_path):
    df = pd.read_csv(file_path)

    matrix_df = df.pivot(index='id_1', columns='id_2', values='car')

    matrix_df = matrix_df.fillna(0)

    for col in matrix_df.columns:
        matrix_df.at[col, col] = 0

    return matrix_df


result_df = generate_car_matrix('dataset-1.csv')

print(result_df)
