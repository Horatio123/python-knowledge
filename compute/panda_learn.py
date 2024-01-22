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
    china_df = df[df['Country Name'] == 'China'].iloc[:, 4:]
    print(china_df)

    india_df = df[df['Country Name'] == 'India'].iloc[:, 4:]
    print(india_df)

    years = china_df.columns.tolist()  # 行标题作为横坐标
    values = china_df.values.tolist()[0]  # 行内容作为纵坐标
    print(years)
    print(values)

    # plt.bar(years, values[0])
    # plt.xlabel('year')
    # plt.ylabel('population')
    # plt.title('China population')
    # plt.xticks(rotation=45)  # 可选：旋转横坐标标签以更好地显示
    # plt.show()

    c_pop_df = pandas.DataFrame({
        'years': years,
        'population': values
    })

    i_pop_df = pandas.DataFrame({
        'years': india_df.columns.tolist(),
        'population': india_df.values.tolist()[0]
    })

    pop_df = pandas.DataFrame({
        'years': india_df.columns.tolist(),
        'china_population': china_df.values.tolist()[0],
        'india_population': india_df.values.tolist()[0]
    })

    # i_pop_df.plot(kind='line', x='years', y='population')
    # c_pop_df.plot(kind='line', x='years', y='population')
    # plt.show()

    # 设置 'date' 列为索引，并确保它是日期类型
    pop_df.set_index('years', inplace=True)

    # 绘制多条线图
    pop_df.plot.line(y=['china_population', 'india_population'], figsize=(10, 6))

    # 显示图形
    plt.show()


if __name__ == '__main__':
    analyse_population()
