import pandas as pd
from datetime import datetime
import math
import numpy as np


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


def calculate_all_time_interest_rate(raw_data):
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


def double_item(a):
    return a * 2


def get_sum(row):
    return row.sum()


def calculate_week_earn(raw_data):
    # print(raw_data.iloc[2])
    print('all raw_data is')
    print(raw_data)
    raw_data = raw_data.rename(columns={'time': 'idx'})
    # print(country_year)
    raw_data.set_index('idx', inplace=True)
    # print(country_year)
    transposed_raw_data = raw_data.transpose().reset_index().rename(columns={'index': 'project'})
    print('transposed raw_data is')
    modified_transposed_raw_data = transposed_raw_data.drop('project', axis=1)
    print(modified_transposed_raw_data)
    print(modified_transposed_raw_data.shape[1])

    for i in range(modified_transposed_raw_data.shape[1] - 1):
        cols = modified_transposed_raw_data.columns
        earn = modified_transposed_raw_data.iloc[:, i + 1] - modified_transposed_raw_data.iloc[:, i]
        print(f'{earn.sum()} is earned from {cols[i]} to {cols[i + 1]}')


def df_test():

    raw_data = pd.read_csv('bank/finance-20240722.csv', skiprows=1)
    # print(raw_data.iloc[2])
    print('all raw_data is')
    print(raw_data)

    icbc_double = raw_data[['icbc_a', 'icbc_b', 'icbc_c']].apply(double_item)
    print('use apply')
    print(icbc_double)

    icbc_sum = raw_data['icbc_a'] + raw_data['icbc_b'] + raw_data['icbc_c']
    print('icbc sum is')
    print(icbc_sum)

    all_sum = raw_data.drop('time', axis=1).apply(get_sum, axis=1)
    print('all sum is')
    print(all_sum)

    for name, col in raw_data.iloc[2].to_dict().items():
        print(f'name is {name}, col is {col}')

    # print(raw_data.iloc[:, 2])
    for idx, row in raw_data.iloc[:, 2].to_dict().items():
        print(f'idx is {idx}, row is {row}')

    for index, row in raw_data.iterrows():
        print(f'index is {index}\nrow is {row}')
        data = raw_data.at[index, 'icbc_b']
        print(data)
        data2 = raw_data.iloc[index, 2]
        print(data2)


if __name__ == '__main__':
    raw_data = pd.read_csv('bank/finance-20240806.csv', skiprows=1)
    calculate_week_earn(raw_data)
    calculate_all_time_interest_rate(raw_data)




