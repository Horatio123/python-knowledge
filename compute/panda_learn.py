import pandas


def play_with_pandas():
    df = pandas.read_csv('cwe.csv')
    print(type(df))
    print(df['group'])
    print(df.File)