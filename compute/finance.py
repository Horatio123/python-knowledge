import pandas as pd
from datetime import datetime
import math


def get_start_time_and_money(data, column, start=0):
    start_str = data['time'].iloc[start]
    start_money_value = data[column].iloc[start]
    # print(f'start row is {start_row}')
    for idx, row in data[column].items():
        # start from start_row
        if idx < start:
            continue
        if not math.isclose(row, 0.00):
            start_str = data['time'].iloc[idx]
            start_money_value = row
            # print(f'start_row is {start_row} {column} is start from {start_time}')
            break
    return start_str, start_money_value


def calculate_earning_and_interest_rate(start, end, days):
    return (end - start), (end - start) / start / days * 365

def calculate_all():
    raw_data = pd.read_csv('bank/finance-20240722.csv', skiprows=1)
    print(raw_data)

    for col in raw_data.columns:
        # 对每列做操作
        if col == 'time':
            continue

        # print(f"Column {col}:")
        # print(raw_data[col])
        # get start time
        start_row = 0
        start_time, start_money = get_start_time_and_money(raw_data, col, start_row)
        # print(f'{col} start time is {start_time}, start money is {start_money}')
        start_date = datetime.strptime(start_time, "%Y.%m.%d")

        end_row = -1
        end_money = raw_data[col].iloc[end_row]
        end_time = raw_data['time'].iloc[end_row]
        end_date = datetime.strptime(end_time, "%Y.%m.%d")
        delta = end_date - start_date
        days_between = delta.days
        # print(f'{col} end time is {end_time}, end money is {end_money}, save for {days_between} days')

        earning, interest_rate = calculate_earning_and_interest_rate(start_money, end_money, days_between)
        print(f'{col} start money is {start_money}, end money is {end_money}, earning is {earning} ,interest_rate is {interest_rate}')


if __name__ == '__main__':
    calculate_all()






