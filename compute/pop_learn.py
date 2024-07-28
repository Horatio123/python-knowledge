import pandas as pd
import matplotlib.pyplot as plt


def get_col_country_df(input_df):
    country_year = input_df.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis=1)
    country_year = country_year.rename(columns={'Country Name': 't-index'})
    # print(country_year)
    country_year.set_index('t-index', inplace=True)
    # print(country_year)
    transposed_country_year = country_year.transpose().reset_index().rename(columns={'index': 'Time'})
    # transposed_country_year.rename(columns={'Country Name': 'Time'})
    # print(transposed_country_year)
    # print(transposed_country_year[['Time', 'China']])
    return transposed_country_year


if __name__ == '__main__':
    pop_df = pd.read_csv('metadata/API_SP.POP.TOTL_DS2_en_csv_v2_6298256/'
                     'API_SP.POP.TOTL_DS2_en_csv_v2_6298256.csv', skiprows=4)

    transposed_df = get_col_country_df(pop_df)
    selected_countries = transposed_df[['Time', 'China', 'India']]

    gap = transposed_df['China'] - transposed_df['India']
    print(gap)
    selected_countries.insert(0, 'Gap', gap)
    selected_countries.plot.line(y=['Gap', 'China', 'India'], x='Time', figsize=(10, 6))

    plt.show()
