from statistics import mean
import numpy as np

xs = np.array([1,6,7,9,2], dtype=np.float64)
ys = np.array([5,3,2,9,0], dtype=np.float64)

def best_fit_slope(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)**2) - mean(xs**2)))
    return m

m = best_fit_slope(xs,ys)
print(m)