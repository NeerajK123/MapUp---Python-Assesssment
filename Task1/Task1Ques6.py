import pandas as pd

def verify_time_completeness(df):

    df['start_timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])

    df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])

    completeness_check = (
        (df['start_timestamp'].dt.time == pd.to_datetime('00:00:00').time()) &
        (df['end_timestamp'].dt.time == pd.to_datetime('23:59:59').time()) &
        (df['start_timestamp'].dt.day_name() == 'Monday') &
        (df['end_timestamp'].dt.day_name() == 'Sunday')
    )


    completeness_check = completeness_check.groupby([df['id'], df['id_2']]).all()

    return completeness_check

df = pd.read_csv('dataset-2.csv')

result = verify_time_completeness(df)
print(result)
