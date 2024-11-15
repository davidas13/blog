---
title: Shell Command untuk Linux dan Windows
tags: ['🗃️Library/📝Literature', '🌏Content/Note', 'linkerexclude']
aliases: []
date: 2024-11-15T11:59
description:  
publish: true
---

Seperti yang kita tahu perintah shell adalah antarmuka baris perintah ([[📬 Inbox/Command Line Interface|CLI]]) dan pada setiap [[📬 Inbox/Operating System|sistem operasi]] pasti mempunyai hal ini, meskipun pada pengguna [[Windows|Windows]] modern mungkin bisa dikatakan jarang digunakan :-D.

Akan tetapi, untuk pengguna [[Linux|Linux]] penggunaan shell merupakan aspek fundamental dalam mengoperasikan sistem operasi. Terutama para programmer atau developer, sering menggunakan aplikasi terminal untuk melakukan kegiatannya.

Daftar command shell pada Windows memang memang lebih sedikit jika dibandingkan dengan Linux, sebagai referensi Windows mempunyai [[https://www.ninjaone.com/blog/windows-cmd-commands/#:~:text=How%20many%20Windows%20CMD%20commands%20are%20there?|280-300 commands]] sedangkan Linux mempunyai lebih dari [[https://www.linuxtrainingacademy.com/linux-commands-cheat-sheet/#:~:text=Did%20you%20know%20that%20there%20are%20literally%20hundreds%20of%20Linux%20commands?%20Even%20on%20a%20bare%2Dbones%20Linux%20server%20install%20there%20are%20easily%20over%201%2C000%20different%20commands.|1000 commands]] (tergantung dari distro yang digunakan). Fakta uniknya command pada [[Linux]] sebenarnya bisa kita akses di Windows melalui [[Cygwin]], [[MSYS]], [[GnuWind32]] dan [[WSL]].

Berikut daftar equivalent perintah antara Linux dan Windows

#### Menampilkan daftar file atau folder pada direktori saat ini
```sh title="Linux"
ls
```

```cmd title="Windows"
dir
```


| Linux       | Windows        | Deskripsi                                                               |
| ----------- | -------------- | ----------------------------------------------------------------------- |
| ls          | dir            | Menampilkan daftar file dan folder di direktori kerja saat ini.         |
| cd          | cd             | Mengubah direktori kerja saat ini.                                      |
| cp          | copy           | Menyalin file atau folder ke lokasi baru.                               |
| mv          | move / rename  | Memindahkan atau mengganti nama file atau folder.                       |
| mkdir       | md             | Membuat folder atau subdirektori baru.                                  |
| rm          | del atau rmdir | Menghapus file atau folder.                                             |
| echo        | echo           | Menampilkan teks ke layar konsol.                                       |
| cat         | type           | Menampilkan isi file berbasis teks.                                     |
| grep        | find           | Mencari string teks di dalam file.                                      |
| more        | more           | Menampilkan isi file berbasis teks dengan kemampuan scrolling.          |
| df          | net use        | Menampilkan semua perangkat penyimpanan.                                |
| uname       | ver            | Menampilkan informasi tentang sistem operasi atau versi kernel.         |
| who         | net session    | Menampilkan semua pengguna yang sedang login.                           |
| adduser     | net user       | Mengelola akun pengguna pada sistem.                                    |
| useradd     | net localgroup | Mengelola pengguna dan grup.                                            |
| ping        | ping           | Mengirim ping ke host jarak jauh.                                       |
| ifconfig -a | ipconfig /all  | Menampilkan informasi tentang adaptor jaringan dan koneksi.             |
| traceroute  | tracert        | Melacak rute paket jaringan yang berjalan ke host jarak jauh.           |
| ftp         | ftp            | Mentransfer file antar sistem.                                          |
| telnet      | telnet         | Telnet adalah program konsol jarak jauh.                                |
| nslookup    | nslookup       | Melakukan resolusi nama host menggunakan DNS.                           |
| man         | help           | Mendapatkan bantuan atau informasi lebih lanjut tentang suatu perintah. |



---
# Reference Links
-