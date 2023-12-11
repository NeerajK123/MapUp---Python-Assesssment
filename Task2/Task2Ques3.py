import pandas as pd

def find_ids_within_ten_percentage_threshold(distance_df, reference_id_start):

    reference_avg_distance = distance_df[distance_df['id_start'] == reference_id_start]['distance'].mean()

    lower_threshold = reference_avg_distance * 0.9
    upper_threshold = reference_avg_distance * 1.1

    filtered_df = distance_df[(distance_df['id_start'] != reference_id_start) &
                              (distance_df['distance'] >= lower_threshold) &
                              (distance_df['distance'] <= upper_threshold)]


    result_ids = sorted(filtered_df['id_start'].unique())

    return result_ids

unrolled_result_df = unroll_distance_matrix(result_df)

reference_value = 1  
result_ids = find_ids_within_ten_percentage_threshold(unrolled_result_df, reference_value)
print(result_ids)
