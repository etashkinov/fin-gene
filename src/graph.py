import matplotlib.pyplot as plt
from matplotlib import style


def show(df, fracture):
    df['Adj. Close'].plot()
    style.use('fivethirtyeight')

    index = fracture[0]

    try:
        day = df.iloc[index]
        name = day.name
        close_ = day['Adj. Close']
        plt.scatter(name, close_, s=100, c='r')
    except Exception as e:
        print(e)

    try:
        m1 = fracture[2][0]
        b1 = fracture[2][1]

        plt.plot([df.iloc[0].name, df.iloc[index].name], [b1, m1 * index + b1])

        m2 = fracture[3][0]
        b2 = fracture[3][1]
        plt.plot([df.iloc[index].name, df.iloc[len(df) - 1].name], [m2 * index + b2, m2 * len(df) + b2])
    except Exception as e:
        print(e)

    plt.legend(loc=4)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()
