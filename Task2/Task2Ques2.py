import pandas as pd

def unroll_distance_matrix(distance_matrix):

    unrolled_df = pd.DataFrame(columns=['id_start', 'id_end', 'distance'])

    for id_start in distance_matrix.index:
        for id_end in distance_matrix.columns:

            if id_start != id_end:

                distance = distance_matrix.at[id_start, id_end]

                unrolled_df = unrolled_df.append({'id_start': id_start, 'id_end': id_end, 'distance': distance}, ignore_index=True)

    unrolled_df = unrolled_df.reset_index(drop=True)

    return unrolled_df

result_df = generate_car_matrix('dataset-1.csv')

unrolled_result_df = unroll_distance_matrix(result_df)
print(unrolled_result_df)
