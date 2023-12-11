import pandas as pd

def calculate_toll_rate(distance_df):

    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}

    for vehicle_type, rate_coefficient in rate_coefficients.items():

        distance_df[vehicle_type] = distance_df['distance'] * rate_coefficient

    return distance_df

unrolled_result_df = unroll_distance_matrix(result_df)

result_with_toll_rate = calculate_toll_rate(unrolled_result_df)
print(result_with_toll_rate)
