import matplotlib.pyplot as plt
from matplotlib import style


def show(df, date):
    df['Adj. Close'].plot()
    style.use('ggplot')

    plt.scatter(date, df.loc[date]['Adj. Close'], s=100, c='r')
    plt.legend(loc=4)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()
