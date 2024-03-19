import pandas
import matplotlib.pyplot as plt


def plot_curve():
    df = pandas.read_csv('metadata/API_SP.POP.TOTL_DS2_en_csv_v2_6298256/'
                         'API_SP.POP.TOTL_DS2_en_csv_v2_6298256.csv', skiprows=4)

    selected_countries = df[df['Country Name'].isin(["China", "India"])].T
    # print(type(selected_countries))
    # print(selected_countries.head())
    rows = selected_countries.shape[0]
    # cols = selected_countries.shape[1]
    # print(rows, cols)
    selected_countries = selected_countries.iloc[4:rows - 1, :]
    selected_countries.columns = ['China', 'India']

    # print(selected_countries.head())
    # print(selected_countries.index.to_numpy())
    # print(selected_countries.columns)
    selected_countries.insert(0, 'years', selected_countries.index.to_numpy())
    # print(selected_countries)

    # 设置 'date' 列为索引，并确保它是日期类型
    # selected_countries.set_index('years', inplace=True)

    # 绘制多条线图
    selected_countries.plot.line(y=['China', 'India'], x='years', figsize=(10, 6))

    plt.show()


if __name__ == '__main__':
    plot_curve()
