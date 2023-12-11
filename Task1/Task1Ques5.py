import pandas as pd

def multiply_matrix(input_df):

    modified_df = input_df.copy()


    modified_df[modified_df > 20] *= 0.75
    modified_df[modified_df <= 20] *= 1.25

    modified_df = modified_df.round(1)

    return modified_df

result_df = generate_car_matrix('dataset-1.csv')


modified_result_df = multiply_matrix(result_df)
print(modified_result_df)
