# Kutai NFT Generator
Kutai NFT Generator adalah Random Generative Engine yang bisa digunakan untuk menciptakan random mix/generative collections. Saya mengembangkan program ini menggunakan bahasa pemrograman python. Sebenarnya proyek ini terinspirasi dengan [Hashlips Art Engine](https://github.com/HashLips/hashlips_art_engine). Bedanya saya menambahkan suatu function semacam logic untuk menghindari atribut tidak cocok untuk terpilih.

Anyway, apa yang saya coba bikin sebenarnya mengembangkan koding sesederhana mungkin supaya orang dengan tanpa latar belakang juga bisa menggunakan.

## Gimana cara pakenya?
Kamu bisa coba jalankan script [test.py](test.py) melalui IDE seperti VS Code atau terminal sebagai berikut:
```terminal
python test.py
```
atau kamu juga bisa coba bikin folder project kamu sendiri mengunakan perintah sebagai berikut
```terminal
python manage.py generate <n-output> <output-destination>
```
Dimana `n-output` adalah jumlah output yang kamu inginkan (jumlahnya akan terbatas tentu saja), sedangkan `output-destination` adalah folder project yang ingin kamu buat.

Perintah diatas akan membuat folder source, termasuk file attributes.json, config.json, probability.json, dan source.svg didalamnya.

    ⚠ Pastikan folder layers tidak kosong dan pastikan pula png file didalam folder layers ditulis dengan format `index_trait-type_trait-name.png`

Layers didalam folder layers akan diidentifikasi oleh program  sebagai `index`, `trait-type`, dan `trait-name`. Informasi tersebut kemudian akan digunakan untuk menciptakan file-file json dan svg didalam folder source. Pastikan tidak memuat karakter underscore ("\_") didalam variabel-variable tersebut karena itu akan digunakan sebagai pemisah.

Selain itu pastikan kamu juga sudah menginstall modul-modul yang diperlukan. Kamu bisa menginstall modul-modul tersebut dengan mengeksekusi perintah berikut melalui terminal.
```terminal
pip install -r requirements.txt
```
