import pandas
import matplotlib.pyplot as plt


def play_with_pandas():
    df = pandas.read_csv('cwe.csv')
    print(type(df))
    print(df['group'])
    print(df.File)


def analyse_population():
    df = pandas.read_csv('metadata/API_SP.POP.TOTL_DS2_en_csv_v2_6298256/'
                         'API_SP.POP.TOTL_DS2_en_csv_v2_6298256.csv', skiprows=4)

    print(type(df))
    # print(df['1977'])
    big_df = df[(df['Country Name'] == 'China') | (df['Country Name'].str.contains('India'))].iloc[:, [0] + list(range(4, df.shape[1]))]

    name_pop_df = big_df['Country Name'].apply(lambda x: x + '_population')
    big_df.insert(1, 'country_pop', name_pop_df)
    big_df = big_df.drop('Country Name', axis=1)

    #
    # years = big_df.columns.tolist()  # 行标题作为横坐标
    # values = big_df.values.tolist()[0]  # 行内容作为纵坐标
    # print(years)
    # print(values)

    pop_df = pandas.DataFrame({
        'years': big_df.columns.tolist()[1:],
        big_df.values.tolist()[0][0]: big_df.values.tolist()[0][1:],
        big_df.values.tolist()[1][0]: big_df.values.tolist()[1][1:]
    })

    # 设置 'date' 列为索引，并确保它是日期类型
    pop_df.set_index('years', inplace=True)

    # 绘制多条线图
    pop_df.plot.line(y=[big_df.values.tolist()[0][0], big_df.values.tolist()[1][0]], figsize=(10, 6))

    # 显示图形
    plt.show()

    gap_list = list(map(lambda x, y: x - y, big_df.values.tolist()[0][1:], big_df.values.tolist()[1][1:]))
    gap_df = pandas.DataFrame({
        'years': big_df.columns.tolist()[1:],
        'gap_population': gap_list
    })

    # 设置 'date' 列为索引，并确保它是日期类型
    gap_df.set_index('years', inplace=True)

    # 绘制多条线图
    gap_df.plot.line(y=['gap_population'], figsize=(10, 6))

    # 显示图形
    plt.show()


if __name__ == '__main__':
    analyse_population()
