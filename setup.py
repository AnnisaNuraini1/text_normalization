import setuptools

setuptools.setup(
    name='normalization_text',  # Ganti dengan nama paket yang sesuai
    version='1.0.0',  # Ganti dengan versi paket yang sesuai
    # Ganti dengan deskripsi paket yang sesuai
    description='Menormalisasikan Data Text',
    long_description='Package ini berfungsi untuk menormalisasi data teks sebelum melakukan pemrosesan lebih lanjut. Pertama Anda perlu mengimpor Modul yang diperlukan untuk package ini adalah : pandas, re (regular expression) untuk operasi pencocokan pola teks, nltk (Natural Language Toolkit) untuk pemrosesan bahasa alami, stopwords dari nltk.corpus untuk mengunduh dan menggunakan daftar kata-kata penghenti dalam bahasa Indonesia,  Kedua Anda perlu mengunduh daftar kata penghenti (stopwords) dalam bahasa Indonesia jika belum diunduh sebelumnya, Package ini memuat pemetaan antara kata informal dan formal dari file CSV "new_kamusalay.csv" ke dalam DataFrame "df_new_kamusalay". Pemetaan ini digunakan untuk mengganti kata-kata informal dengan kata-kata formal. memuat daftar kata-kata kasar (Abusive words) dari file CSV "abusive.csv" ke dalam DataFrame "df_abusive", daftar ini digunakan untuk menghapus kata-kata kasar dari teks. Mendefinisikan daftar kata penghenti (stopwords)  dalam bahasa indonesia. Selain itu, package ini digunakan untuk membersihkan teks dengan menghapus kata-kata penghenti (stopwords) dari teks. ini dilakukan dengan membagi teks menjadi kata-kata, memeriksa apakah kata-kata tersebut bukan kata penghenti, dan kemudian menggabungkan kembali kata-kata yang tersisa menjadi teks yang bersih. Membersihkan teks dengan menggunakan ekspresi regule (regex). Ini melibatkan serangkaian pemrosesan seperti menghapus tanda strip, simbol, spasi berlebih, karakter baris baru, retweet symbol, username, URL, angka, tanda seru, spasi berlebih, dan tanda baca, selanjutnya teks dikonversi menjadi huruf kecil. Mengganti kata-kata dalam teks menggunakan pemetaan kata informal dan menghapus kata-kata kasar. pada langkah ini, kata-kata dalam teks dibagi menjadi kata-kata kasar. kata-kata yang ditemukan diganti dengan pengganti yang sesuai atau diubah menjadi "*****" selanjutnya teks dibersihkan dari spasi awal dan akhir. fungsi utama nya adalah menggabungkan langkah-langkah preprocessing dengan mengaplikasikan langkah-langkah berikut secara berurutan : membersihkan stopwords; membersihkan menggunakan regex; mengganti kata-kata dan mengembalikan teks yang sudah di normalisasi.',  # Ganti dengan deskripsi yang lebih panjang jika diperlukan
    author='Annisa Nuraini',  # Ganti dengan nama penulis paket
    author_email='annisanuraini44@gmail.com',  # Ganti dengan email penulis
    # Ganti dengan URL proyek Anda
    # Ganti dengan daftar nama paket yang disertakan dalam distribusi
    packages=['normalisasitext'],
    # Ganti dengan daftar dependensi yang diperlukan oleh paket Anda
    install_requires=['pandas', 'numpy', 're',
                      'nltk', 'stopwords', 'nltk.corpus'],
    classifiers=['License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: 3.9',
                 'Programming Language :: Python :: 3.10',
                 'Programming Language :: Python :: 3.11',
                 ],

)
