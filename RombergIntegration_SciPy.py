import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# misal mau mencari integral dari [0 - 2] dari ex^2 + 2x
def func(x):
    return np.exp(x**2) + 2*x

# Menggunakan fungsi bawaan scipy yaitu integrasi romberg
romberg = integrate.romberg(func, 0, 1, show=True)

print(f'Result : {romberg}')