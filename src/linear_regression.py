from statistics import mean
import numpy as np


def _best_fit_slope_and_intercept(xs, ys):
    m = (((mean(xs) * mean(ys)) - mean(xs * ys)) /
         ((mean(xs) * mean(xs)) - mean(xs * xs)))
    b = mean(ys) - m * mean(xs)
    return m, b


def _squared_error(ys_orig, ys_line):
    return sum((ys_line - ys_orig) * (ys_line - ys_orig))


def train(xs, ys):
    xs = [xs[0], xs[-1]]
    ys = [ys[0], ys[-1]]
    return _best_fit_slope_and_intercept(np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64))
