---
title: Shell Command antara Linux dan Windows
tags: ['🌏Content/Note/Basic']
aliases: []
date: 2024-11-15T17:30
description:  
publish: true
---

*[[Shell]]* merupakan antarmuka baris perintah (_command line interface_/CLI) yang menjadi bagian tak terpisahkan dari setiap sistem operasi, meskipun mungkin jarang digunakan oleh pengguna [[Windows]] rumahan (itupun sepengetahuan saya 😊).

Di sisi lain, penggunaan *shell* merupakan aspek fundamental dalam mengoperasikan sistem operasi [[Linux]]. Para *Programmer* dan *Developer* khususnya, kerap memanfaatkan aplikasi *[[terminal]]* untuk menunjang aktivitas mereka.

Daftar perintah _shell_ pada Windows memang relatif lebih terbatas dibandingkan dengan Linux. Sebagai gambaran, Windows memiliki sekitar [[https://www.ninjaone.com/blog/windows-cmd-commands/#:~:text=How%20many%20Windows%20CMD%20commands%20are%20there?|280-300 perintah]], sementara Linux menawarkan lebih dari [[https://www.linuxtrainingacademy.com/linux-commands-cheat-sheet/#:~:text=Did%20you%20know%20that%20there%20are%20literally%20hundreds%20of%20Linux%20commands?%20Even%20on%20a%20bare%2Dbones%20Linux%20server%20install%20there%20are%20easily%20over%201%2C000%20different%20commands.|1000 perintah]] (jumlahnya bervariasi tergantung distro yang digunakan). Menariknya, perintah-perintah Linux tersebut sebenarnya dapat diakses di Windows melalui *software* seperti [[Cygwin]], [[MSYS]], [[GnuWin32]], dan [[WSL]].

Berikut beberapa daftar perintah antara Linux dan Windows:

| Linux     | Windows           | Deskripsi                                                          |
| --------- | ----------------- | ------------------------------------------------------------------ |
| `ls`      | `dir`             | Menampilkan daftar file atau folder pada direktori saat ini        |
| `cd`      | `cd`              | Mengubah direktori saat ini                                        |
| `mv`      | `move` / `rename` | Memindahkan atau mengganti nama file atau folder                   |
| `mkdir`   | `md`              | Membuat folder                                                     |
| `rm`      | `del` / `rmdir`   | Menghapus file atau folder                                         |
| `echo`    | `echo`            | Menampilkan text pada console                                      |
| `cat`     | `type`            | Menampilkan isi file berbasis text pada console                    |
| `grep`    | `find`            | Mencari text tertentu  di dalam sebuah file berbasis text          |
| `more`    | `more`            | Menampilkan semua isi file berbasis text dengan  fitur scrolling   |
| `df`      | `net use`         | Menampilkan semua perangkat penyimpanan                            |
| `who`     | `net session`     | Menampilkan semua pengguna yang sedang login                       |
| `man`<br> | `help`<br>        | Membuka bantuan atau informasi lebih lanjut tentang suatu perintah |