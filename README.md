
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

Pada dasarnya, seperti halnya algoritma integrasi adaptif, Integrasi Romberg adalah perluasan yang relatif mudah dari keluarga algoritma Newton-Cotes.
Keduanya bekerja dengan menggunakan iterasi yang disempurnakan dari beberapa metode Newton-Cotes yang mendasarinya untuk memberikan perkiraan nilai integral yang 
cenderung lebih akurat. Tidak seperti ``` Metode Rieman``` yang masih terbilang kurang akurat.

Integrasi Romberg bukanlah pendekatan adaptif terhadap intergrasi. Gal tersebut berarti metode Romberg tiddak mengubah perilakunya sendiri berdasarkan perilaku fungsi yang akan
diintegrasikan. Sebaliknya, kita juga dapat mengeksploitasi perilaku fungsi trapesiumm pada batas untuk menghasilkan estimasi integral