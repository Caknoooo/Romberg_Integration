
# Integrasi Romberg

## Kelompok 5 Komputasi Numerik C

## Identitas Anggota
| Nama                      | NRP        |
|---------------------------|------------|
|Yoel Mountanus Sitorus     | 5025211078 |
|Darren Prasetya            | 5025211162 |
|M Naufal Badruttamam       | 5025211240 |




## 🚀 Penjelasan Singkat Integrasi Romberg
Integrasi Romberg merupakan salah satu metode ekstrapolasi yang didasarkan pada perluasan ekstrapolasi Richardson, dimana pada setiap penerapan ekstrapolasi Richadson akan menaikkan orde galat pada hasil solusinya sebesar dua. (Google)

Metode Romberg merupakan metode integrasi yang didasarka pada perluasan ``` ekstrapolasi  Richardson``` 
yang dihasilkan dari aturan ``` Metode Trapesium``` yang dilakukan secara terus menerus (Rekursif). Kelemahan dari metode ini adalah harus menggunakan jumlah interval 
yang besar guna mencapai akurasi yang diharapkan. Untuk meningkatkan akurasi kita harus melakukan rekursi terus menerus sampai nilai integral yang dihitung mendekati nilai 
2^k yang konvergen pada suatu nilai

Pada dasarnya, seperti halnya algoritma integrasi adaptif, Integrasi Romberg adalah perluasan yang relatif mudah dari keluarga algoritma Newton-Cotes.
Keduanya bekerja dengan menggunakan iterasi yang disempurnakan dari beberapa metode Newton-Cotes yang mendasarinya untuk memberikan perkiraan nilai integral yang 
cenderung lebih akurat. Tidak seperti ``` Metode Rieman``` yang masih terbilang kurang akurat.

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

Maka fungsi rekursif akan selesai. Sehingga diperoleh rumus:

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


