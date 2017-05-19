import linear_regression

CHECK_PERIOD = 365 * 3


def get_point(ys):
    xs = range(len(ys))
    ys = ys['Adj. Close']

    result = (0, -99999)
    for i in xs[CHECK_PERIOD:-CHECK_PERIOD]:

        before_line = linear_regression.train(xs[i - CHECK_PERIOD:i], ys[i - CHECK_PERIOD:i])
        after_line = linear_regression.train(xs[i:i + CHECK_PERIOD], ys[i:i + CHECK_PERIOD])

        fracture = after_line[0]# - before_line[0]
        if fracture > result[1]:
            result = i, fracture, before_line, after_line

    return result
