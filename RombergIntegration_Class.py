import numpy as np
import sys

class RombergIntegration:
    def __init__(self, a, b, n, exact) -> None:
        self.initialize(a, b, n, exact)
        self.initTrapezhoid()
    
    def initialize(self,a, b, n, exact):
        self.a = a
        self.b = b
        self.n = n
        self.exact = exact
        self.data = np.zeros((self.n, self.n))
        self.pow_4 = 4 ** np.arange(self.n) - 1
    
    def initTrapezhoid(self):
        self.h = (self.b - self.a)
        self.data[0, 0] = self.h * (self.fn(self.a) + self.fn(self.b)) / 2
    
    # Function ex^2 + 2x
    def fn(self, x):
        return np.exp(x**2) + 2*x

    def calculate(self):
        for j in range(1, self.n):
            self.h /= 2

            # Menggunakan aturan trapezhoid yang di rekursi secara terus menerus
            self.data[j, 0] = self.data[j - 1, 0] / 2
            self.data[j, 0] += self.h * sum(self.fn(self.a + i * self.h) for i in range(1, 2 ** j + 1, 2))

            # Dengan bantuan extrapolation richardson
            for k in range(1, j + 1):
                self.data[j, k] = self.data[j, k - 1] + (self.data[j, k - 1] - self.data[j - 1, k - 1]) / self.pow_4[k]

    def result(self):
        print(self.data, file=sys.stderr)
        if self.exact:
            errors = ['%.2e' % i for i in np.abs(self.data.diagonal() - self.exact)]
            print(f'Absolute error: {errors}',  file=sys.stderr)
        return self.data[-1, -1]


romberg = RombergIntegration(0, 1, 5, 0.7212691982)
romberg.calculate()
result = romberg.result()
print(f'Result : {result}')
