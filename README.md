
# Integrasi Romberg

| Nama                      | NRP        | Github                              |
|---------------------------|------------|-------------------------------------|
|Yoel Mountanus Sitorus     | 5025211078 |[Yoel](https://github.com/zemetia/)  |
|Darren Prasetya            | 5025211162 |[Darren](https://github.com/Mikask1/)|
|M Naufal Badruttamam       | 5025211240 |[Cakno](https://github.com/Caknoooo/)|

## 🚀 Penjelasan Singkat Integrasi Romberg
Integrasi Romberg merupakan salah satu metode ekstrapolasi yang didasarkan pada perluasan ekstrapolasi Richardson, dimana pada setiap penerapan ekstrapolasi Richadson akan menaikkan orde galat pada hasil solusinya sebesar dua. (Google)

Metode Romberg merupakan metode integrasi yang didasarka pada perluasan ```Ekstrapolasi  Richardson``` 
yang dihasilkan dari aturan ```Metode Trapesium``` yang dilakukan secara terus menerus (Rekursif). Kelemahan dari metode ini adalah harus menggunakan jumlah interval 
yang besar guna mencapai akurasi yang diharapkan. Untuk meningkatkan akurasi kita harus melakukan rekursi terus menerus sampai nilai integral yang dihitung mendekati nilai 
2^k yang konvergen pada suatu nilai

Pada dasarnya, seperti halnya algoritma integrasi adaptif, Integrasi Romberg adalah perluasan yang relatif mudah dari keluarga algoritma Newton-Cotes.
Keduanya bekerja dengan menggunakan iterasi yang disempurnakan dari beberapa metode Newton-Cotes yang mendasarinya untuk memberikan perkiraan nilai integral yang 
cenderung lebih akurat. Tidak seperti ```Metode Rieman``` yang masih terbilang kurang akurat.

Integrasi Romberg bukanlah pendekatan adaptif terhadap intergrasi. Gal tersebut berarti metode Romberg tiddak mengubah perilakunya sendiri berdasarkan perilaku fungsi yang akan
diintegrasikan. Sebaliknya, kita juga dapat mengeksploitasi perilaku fungsi trapesiumm pada batas untuk menghasilkan estimasi integral
## 🛠 Algoritma Integrasi Romberg

Dengan menggunakan rekursif yang dilakukan secara terus menerus oleh metode Trapezoida. 
Jika kita mulai dengan suatu fungsi ```T(f, m)``` dimana T adalah fungsi trapesium, f adalah fungsi yang akan diintegrasikan, 
dan m adalah jumlah panel untuk diintegrasikan, maka:

![1](https://user-images.githubusercontent.com/92671053/208663483-0b59c7d6-e65a-4d2f-83de-e381ccbd7c40.PNG)

Dimana S adalah aturan Simpson yang akan diintegrasikan sebagai

```bash
T = (f, 0) = (b - a)(f(b) + f(a)) = 2
```

Maka fungsi rekursif akan selesai, karena berdasarkan hubungan tersebut, fraksi yang diberikan dalam persamaan diatas juga merupakan perkiraan untuk integral.

Secara umum rumusnya adalah sebagai berikut:

![2](https://user-images.githubusercontent.com/92671053/208665099-fa684fa8-3c79-409d-815b-957d7fac5eb8.PNG)





## 🤔 Langkah Penyelesaian Metode Romberg

1. Mendefinisikan fungsi integral yang diberikan yaitu f(x), jika hanya diketahui titik-titik, maka kita harus mencari fungsi integralnya terlebih dahulu
2. Menentukan batas-batas integral dengan nilai konstanta
3. Menentukan jumlah iterasi yang akan dilakukan (N)
4. Menentukan nilai interval pada selang [a, b] atau bisa dengan [x2, x1] lalu menghitung h nya dengan cara: 
   `h = x2 - x1`
5. Menghitung Integrasi pada kolom pertama dengan menggunakan rumus:

![3](https://user-images.githubusercontent.com/92671053/208666808-bde01be4-001d-44d9-807b-fd9ff73d7eba.PNG)

6. Menghitung nilai integrasi pada kolom kedua sampai n dengan menggunakan rumus integrasi Romberg:

![4](https://user-images.githubusercontent.com/92671053/208667023-f430f9e4-3ff2-423e-b406-0241e0d94be6.PNG)



## Code

Ada berbagai cara dalam pemrograman untuk menyelesaikan `Metode Rpmberg` 

#### Menggunakan fungsi bawaan SciPy dengan import integrate

```py
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# misal mau mencari integral dari [0 - 2] dari ex^2 + 2x
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# misal mau mencari integral dari [0 - 2] dari ex^2 + 2x
def func(x):
    return np.exp(x**2) + 2*x

# Menggunakan fungsi bawaan scipy yaitu integrasi romberg
romberg = integrate.romberg(func, 0, 1, show=True)

print(f'Result : {romberg}')
```
![5](https://user-images.githubusercontent.com/92671053/208717314-29249433-1c1e-474b-acf9-a94896f61b23.PNG)

#### Menggunakan Class 

```py
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
        return np.exp(-x**2)

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
            print('absolute error:', errors, file=sys.stderr)
        return self.data[-1, -1]


romberg = RombergIntegration(0, 1, 5, 0.7212691982)
romberg.calculate()
result = romberg.result()
print(result)
```
![6](https://user-images.githubusercontent.com/92671053/208718101-59f1ec12-1c2e-412f-9f00-8ab6166c9d41.PNG)


## Jupyter Notebook
([Romberg Integration](https://github.com/Caknoooo/Romberg_Integration/blob/main/RombergIntegration_Notebook.ipynb)) | Romberg Integration Using Notebook

## Referensi

Github : 
[mohrosidi](https://github.com/mohrosidi/metode_numerik/blob/master/09-diferensiasi_dan_integrasi.Rmd)

Youtube : [Shams ElFouly](https://youtu.be/2BxLDODvnQA) , 
[Poetro Sambegoro](https://youtu.be/Dj1Gzy52nNk)

