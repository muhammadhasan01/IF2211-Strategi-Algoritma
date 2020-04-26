# Aplikasi Ekstraktor Informasi

Aplikasi Ekstraktor Informasi adalah aplikasi yang dapat digunakan untuk melakukan ekstraksi suatu *keyword* yang diberikan pada beberapa teks berita, hasil yang akan dikeluarkan adalah pasangan jumlah angka dan waktu yang berhubungan dengan *keyword* tersebut.


### Cara menjalankan Aplikasi

Berikut adalah tata cara dalam menjalankan aplikasi ini:

1. Pastikan sudah terinstall **[python](https://www.python.org/)**, terutama **python version 3.7**, pada sistem Anda.
2. Kemudian install `pip` pada `python` (jika belum ada) dan install semua *python dependency* yang diperlukan dengan mengetik *command* ini pada folder `src`:
```
pip install -r requirements.txt
```
3. Jika nltk yang terinstall belum pernah digunakan, download terlebih dahulu **module punkt** dengan menjalankan *python* pada *command prompt* dan gunakan *command*:
```
>>> import nltk
>>> nltk.download('punkt')
```
4. Gunakan *command* `flask run` pada `command prompt` di folder `src` untuk menjalankan *localhost* pada *server*. Flask akan menjalankan *localhost* pada **port** yang diberikan di *command prompt*
5. Gunakan *browser* untuk mengakses *web* tersebut dengan menggunakan *port* yang telah diberikan.

## Kontributor

Muhammad Hasan - 13518012

## Dibuat dengan

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [Python](https://www.python.org/)
