## Kutai NFT Generator

Kutai NFT Generator adalah Random Artworks/Collection Generator yang saya kembangkan menggunakan bahasa pemrograman Python. Project ini sendiri terinspirasi oleh Hashlips Artwork Engine. Adapun fungsi utama project ini adalah membantu Artist untuk menciptakan koleksi karya seninya sendiri.  

Alasan saya menggunakan bahasa pemrograman Python sebagai bahasa utamanya karena bahasa pemrograman ini lebih ekspresif dan cukup mudah bagi awam. Tujuan akhir dari pengembangan script ini sendiri adalah agar lebih mudah digunakan oleh orang dengan tanpa latar belakang koding.

## Cara Menggunakan
Tahapan penggunaan script ini
1. Pastikan kamu sudah meng-install Python (intepreter) dikomputer mu. Python bisa didownload di [python.org](https://www.python.org/downloads/).
2. Install library yang akan digunakan didalam project ini. Library yang dibutuhkan dapat dilihat di [requirements.txt](requirements.txt). Kamu bisa menggunakan perintah dibawah ini untuk menginstall seluruh modul yang akan digunakan. 
    ```terminal
    pip install -r requirements.txt
    ```
3. Setelah itu kamu bisa membuat sebuah project directory dengan cara mengeksekusi perintah berikut
    ```terminal
    python manage.py startproject -p <project-path>
    ```
    Perintah diatas akan membuat sebuah folder baru didalam folder *project*. Dengan subfolder berupa *layers*, *settings*, dan *output*.  

    Lebih rinci, folder *layers* adalah tempat dimana kamu akan menempatkan seluruh layers image (traits) didalamnya dengan format nama file *<index>_<trait-type>_<trait-name>.png* sebagai contoh *0_Background_Natural.png*, pastikan juga jenis file gambar yang kamu gunakan berekstensi "`.png`". Sedangkan folder *settings* adalah folder dimana kamu akan menemukan file seperti `attributes.json`, `config.json`, dan `probability.json`.  

    Folder *output* sendiri adalah folder dimana hasil generative kamu akan ditempatkan.

4. pass