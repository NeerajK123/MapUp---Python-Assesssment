import pandas as pd
import datetime

def calculate_time_based_toll_rates(distance_df):

    weekday_time_ranges = [(datetime.time(0, 0, 0), datetime.time(10, 0, 0)),
                           (datetime.time(10, 0, 0), datetime.time(18, 0, 0)),
                           (datetime.time(18, 0, 0), datetime.time(23, 59, 59))]

    weekend_time_ranges = [(datetime.time(0, 0, 0), datetime.time(23, 59, 59))]


    for start_time, end_time in weekday_time_ranges:
        mask = (distance_df['start_time'].dt.time >= start_time) & (distance_df['end_time'].dt.time <= end_time) & (distance_df['start_day'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']))
        distance_df.loc[mask, ['moto', 'car', 'rv', 'bus', 'truck']] *= 0.8

    for start_time, end_time in weekday_time_ranges:
        mask = (distance_df['start_time'].dt.time >= start_time) & (distance_df['end_time'].dt.time <= end_time) & (distance_df['start_day'].isin(['Saturday', 'Sunday']))
        distance_df.loc[mask, ['moto', 'car', 'rv', 'bus', 'truck']] *= 0.7


    distance_df['start_day'] = distance_df['start_timestamp'].dt.day_name()
    distance_df['end_day'] = distance_df['end_timestamp'].dt.day_name()
    distance_df['start_time'] = distance_df['start_timestamp'].dt.time
    distance_df['end_time'] = distance_df['end_timestamp'].dt.time

    return distance_df


result_with_toll_rate = calculate_toll_rate(unrolled_result_df)


result_with_time_based_toll_rates = calculate_time_based_toll_rates(result_with_toll_rate)
print(result_with_time_based_toll_rates)
