# -*- coding: utf-8 -*-

GOLDEN_ID_RULES = [
    # 1) Simple period to end sentence
    ("Hari ini cuaca sangat cerah. Saya ingin pergi ke pantai.",
     ["Hari ini cuaca sangat cerah.", "Saya ingin pergi ke pantai."]),

    # 2) Question mark to end sentence
    ("Apakah kamu sudah makan? Saya belum makan.",
     ["Apakah kamu sudah makan?", "Saya belum makan."]),

    # 3) Exclamation point to end sentence
    ("Selamat datang! Semoga betah di sini.",
     ["Selamat datang!", "Semoga betah di sini."]),

    # 4) One-letter upper-case abbreviation (name initial)
    ("Laporan ini disusun oleh A. Siregar dari divisi keuangan.",
     ["Laporan ini disusun oleh A. Siregar dari divisi keuangan."]),

    # 5) Professional title Dr. as non-sentence boundary (mid-sentence)
    ("Pasien itu diperiksa oleh Dr. Budi setiap minggu.",
     ["Pasien itu diperiksa oleh Dr. Budi setiap minggu."]),

    # 6) Professional title Dr. at end of clause followed by new sentence
    ("Laporan itu ditulis oleh Dr. Santoso. Beliau adalah pakar terkemuka.",
     ["Laporan itu ditulis oleh Dr. Santoso.", "Beliau adalah pakar terkemuka."]),

    # 7) Prof. as non-sentence boundary
    ("Makalah ini dibimbing oleh Prof. Ahmad Yani dari Universitas Indonesia.",
     ["Makalah ini dibimbing oleh Prof. Ahmad Yani dari Universitas Indonesia."]),

    # 8) Ir. and Drs. as non-sentence boundary
    ("Proyek itu dipimpin oleh Ir. Wahyu dan Drs. Hendra secara bergantian.",
     ["Proyek itu dipimpin oleh Ir. Wahyu dan Drs. Hendra secara bergantian."]),

    # 9) Yth. honorific as non-sentence boundary
    ("Kepada Yth. Bapak Direktur Utama PT Maju Bersama.",
     ["Kepada Yth. Bapak Direktur Utama PT Maju Bersama."]),

    # 10) dll. (dan lain-lain) as non-sentence boundary
    ("Toko itu menjual baju, celana, sepatu, dll. Harganya sangat terjangkau.",
     ["Toko itu menjual baju, celana, sepatu, dll.", "Harganya sangat terjangkau."]),

    # 11) dkk. (dan kawan-kawan) as non-sentence boundary
    ("Penelitian ini dilakukan oleh Sari dkk. Hasilnya dipublikasikan tahun lalu.",
     ["Penelitian ini dilakukan oleh Sari dkk.", "Hasilnya dipublikasikan tahun lalu."]),

    # 12) dsb. (dan sebagainya) as non-sentence boundary
    ("Kegiatan meliputi membaca, menulis, berhitung, dsb. Semua siswa wajib mengikutinya.",
     ["Kegiatan meliputi membaca, menulis, berhitung, dsb.", "Semua siswa wajib mengikutinya."]),

    # 13) dst. (dan seterusnya) as non-sentence boundary
    ("Formulir harus dilengkapi dengan nama, alamat, tanggal lahir, dst. Harap dikirimkan sebelum batas waktu.",
     ["Formulir harus dilengkapi dengan nama, alamat, tanggal lahir, dst.", "Harap dikirimkan sebelum batas waktu."]),

    # 14) No. followed by a number as non-sentence boundary
    ("Silakan hubungi kami di No. 021-5551234 untuk informasi lebih lanjut.",
     ["Silakan hubungi kami di No. 021-5551234 untuk informasi lebih lanjut."]),

    # 15) Jl. (Jalan) address abbreviation as non-sentence boundary
    ("Kantor kami berlokasi di Jl. Sudirman No. 10, Jakarta Pusat.",
     ["Kantor kami berlokasi di Jl. Sudirman No. 10, Jakarta Pusat."]),

    # 16) Kec. and Kel. address abbreviations as non-sentence boundary
    ("Alamat lengkapnya adalah Gg. Mawar No. 3, Kel. Menteng, Kec. Menteng.",
     ["Alamat lengkapnya adalah Gg. Mawar No. 3, Kel. Menteng, Kec. Menteng."]),

    # 17) Month abbreviation mid-sentence as non-sentence boundary
    ("Acara tersebut akan diadakan pada 15 Nov. 2024 di gedung utama.",
     ["Acara tersebut akan diadakan pada 15 Nov. 2024 di gedung utama."]),

    # 18) Decimal number as non-sentence boundary
    ("Pertumbuhan ekonomi mencapai 5.2 persen pada kuartal ketiga tahun ini.",
     ["Pertumbuhan ekonomi mencapai 5.2 persen pada kuartal ketiga tahun ini."]),

    # 19) Currency amount as non-sentence boundary
    ("Harga barang itu adalah Rp10.000,00 per unit.",
     ["Harga barang itu adalah Rp10.000,00 per unit."]),

    # 20) Number as sentence boundary
    ("Total tagihan Anda adalah Rp250.000,00. Pembayaran dapat dilakukan melalui transfer.",
     ["Total tagihan Anda adalah Rp250.000,00.", "Pembayaran dapat dilakukan melalui transfer."]),

    # 21) Double punctuation (exclamation point)
    ("Luar biasa!! Saya tidak menyangka bisa sampai sejauh ini.",
     ["Luar biasa!!", "Saya tidak menyangka bisa sampai sejauh ini."]),

    # 22) Double punctuation (question mark)
    ("Sungguh?? Kamu benar-benar melihatnya sendiri?",
     ["Sungguh??", "Kamu benar-benar melihatnya sendiri?"]),

    # 23) Double punctuation (exclamation / question mark)
    ("Tidak mungkin!? Bagaimana itu bisa terjadi?",
     ["Tidak mungkin!?", "Bagaimana itu bisa terjadi?"]),

    # 24) Numbered list (period marker, no period to end item)
    ("1. Siapkan bahan-bahan 2. Panaskan oven 3. Masukkan adonan",
     ["1. Siapkan bahan-bahan", "2. Panaskan oven", "3. Masukkan adonan"]),

    # 25) Numbered list (parenthesis marker)
    ("1) Pendahuluan 2) Metodologi 3) Hasil dan Pembahasan",
     ["1) Pendahuluan", "2) Metodologi", "3) Hasil dan Pembahasan"]),

    # 26) Single quotation inside sentence (non-boundary)
    ("Ia berkata, 'Ini adalah hari yang indah.' sambil tersenyum.",
     ["Ia berkata, 'Ini adalah hari yang indah.' sambil tersenyum."]),

    # 27) Double quotation at end of sentence (boundary)
    ('Dia berteriak, "Tolong!" Semua orang langsung berbalik.',
     ['Dia berteriak, "Tolong!"', "Semua orang langsung berbalik."]),

    # 28) Double quotation inside sentence (non-boundary)
    ('Pepatah mengatakan "Berakit-rakit ke hulu, berenang-renang ke tepian." yang bermakna kerja keras.',
     ['Pepatah mengatakan "Berakit-rakit ke hulu, berenang-renang ke tepian." yang bermakna kerja keras.']),

    # 29) Academic degree abbreviation as non-sentence boundary
    ("Pembicara utama adalah Ani Rahayu, S.Pd. yang mengajar di sekolah tersebut.",
     ["Pembicara utama adalah Ani Rahayu, S.Pd. yang mengajar di sekolah tersebut."]),

    # 30) Organizational abbreviation PT. as non-sentence boundary
    ("Perusahaan itu bernama PT. Maju Bersama Tbk. yang berdiri sejak 1995.",
     ["Perusahaan itu bernama PT. Maju Bersama Tbk. yang berdiri sejak 1995."]),

    # 31) Multiple sentences in sequence
    ("Indonesia adalah negara kepulauan. Ibukotanya adalah Jakarta. Penduduknya sangat beragam.",
     ["Indonesia adalah negara kepulauan.", "Ibukotanya adalah Jakarta.", "Penduduknya sangat beragam."]),

    # 32) Ellipsis as non-sentence boundary
    ("Saya tidak tahu... mungkin besok saya akan datang ke sana.",
     ["Saya tidak tahu... mungkin besok saya akan datang ke sana."]),

    # 33) Time notation with period — pukul HH.MM is not a sentence boundary
    ("Rapat dimulai pukul 08.00 dan berakhir pukul 17.00.",
     ["Rapat dimulai pukul 08.00 dan berakhir pukul 17.00."]),

    # 34) Time notation with seconds — pukul HH.MM.SS is not a sentence boundary
    ("Rekaman menunjukkan kejadian itu berlangsung pada pukul 01.35.20 dini hari.",
     ["Rekaman menunjukkan kejadian itu berlangsung pada pukul 01.35.20 dini hari."]),

    # 35) tgl. (tanggal) date abbreviation as non-sentence boundary
    ("Surat ini dibuat pada tgl. 17 Agustus 1945 di Jakarta.",
     ["Surat ini dibuat pada tgl. 17 Agustus 1945 di Jakarta."]),

    # 36) s.d. (sampai dengan) date-range abbreviation as non-sentence boundary
    ("Pendaftaran peserta dibuka dari Senin s.d. Jumat di setiap minggunya.",
     ["Pendaftaran peserta dibuka dari Senin s.d. Jumat di setiap minggunya."]),

    # 37) a.n. (atas nama) delegation marker in formal letters
    ("Surat ini ditandatangani a.n. Direktur Utama yang sedang bertugas ke luar negeri.",
     ["Surat ini ditandatangani a.n. Direktur Utama yang sedang bertugas ke luar negeri."]),

    # 38) u.b. (untuk beliau) attention-to marker in formal correspondence
    ("Mohon sampaikan berkas ini kepada u.b. Bapak Santoso di divisi keuangan.",
     ["Mohon sampaikan berkas ini kepada u.b. Bapak Santoso di divisi keuangan."]),

    # 39) Informal shorthands yg. and dgn. as non-sentence boundary
    ("Saya mencari buku yg. membahas sejarah Indonesia dgn. pembahasan yang lengkap.",
     ["Saya mencari buku yg. membahas sejarah Indonesia dgn. pembahasan yang lengkap."]),

    # 40) Multiple academic degrees after a name, mid-sentence (non-boundary)
    ("Seminar itu dipandu oleh Budi Santoso, S.T., M.T. selaku moderator utama.",
     ["Seminar itu dipandu oleh Budi Santoso, S.T., M.T. selaku moderator utama."]),

    # 41) Academic degree at sentence end (is a boundary)
    ("Makalah itu ditulis oleh Ani Rahayu, S.Pd. Beliau mengajar di sekolah tersebut.",
     ["Makalah itu ditulis oleh Ani Rahayu, S.Pd.", "Beliau mengajar di sekolah tersebut."]),

    # 42) ibid. academic citation as non-sentence boundary
    ("Teori ini dijelaskan lebih lanjut dalam bab sebelumnya (Ibid., hlm. 45).",
     ["Teori ini dijelaskan lebih lanjut dalam bab sebelumnya (Ibid., hlm. 45)."]),

    # 43) op. cit. academic citation as non-sentence boundary
    ("Pernyataan tersebut dikutip dari sumber yang sama (Smith, op. cit., hlm. 23).",
     ["Pernyataan tersebut dikutip dari sumber yang sama (Smith, op. cit., hlm. 23)."]),

    # 44) et al. in academic citation as non-sentence boundary
    ("Penelitian yang dilakukan oleh Wijaya et al. menunjukkan hasil yang signifikan.",
     ["Penelitian yang dilakukan oleh Wijaya et al. menunjukkan hasil yang signifikan."]),

    # 45) Named entity with exclamation point inside sentence (non-boundary)
    ("Kami memesan makanan dari Go-Jek! untuk acara perusahaan malam itu.",
     ["Kami memesan makanan dari Go-Jek! untuk acara perusahaan malam itu."]),

    # 46) Parenthetical phrase inside sentence (non-boundary)
    ("Harga tiket masuk adalah Rp50.000,00 (termasuk pajak PPN) per orang.",
     ["Harga tiket masuk adalah Rp50.000,00 (termasuk pajak PPN) per orang."]),

    # 47) hlm. before a page number as non-sentence boundary
    ("Pembahasan lebih lanjut mengenai topik ini dapat dilihat pada hlm. 42 buku tersebut.",
     ["Pembahasan lebih lanjut mengenai topik ini dapat dilihat pada hlm. 42 buku tersebut."]),

    # 48) Four-dot ellipsis as sentence boundary
    ("Saya sudah mencoba segalanya.... Tidak ada yang berhasil.",
     ["Saya sudah mencoba segalanya....", "Tidak ada yang berhasil."]),

    # --- Hyperlink / URL ---

    # 49) URL mid-sentence is not a sentence boundary
    ("Artikel selengkapnya dapat dibaca di https://www.kompas.com/artikel/judul-berita.html untuk informasi terbaru.",
     ["Artikel selengkapnya dapat dibaca di https://www.kompas.com/artikel/judul-berita.html untuk informasi terbaru."]),

    # 50) URL at sentence end followed by new sentence
    ("Silakan kunjungi situs kami di https://www.kemendikbud.go.id. Informasi lebih lanjut tersedia di sana.",
     ["Silakan kunjungi situs kami di https://www.kemendikbud.go.id.", "Informasi lebih lanjut tersedia di sana."]),

    # 51) Indonesian .id country-code TLD inside URL is not a sentence boundary
    ("Portal resmi layanan publik tersedia di https://www.indonesia.go.id/layanan-publik.html setiap saat.",
     ["Portal resmi layanan publik tersedia di https://www.indonesia.go.id/layanan-publik.html setiap saat."]),

    # 52) URL with path segments and numeric components is not a sentence boundary
    ("Gunakan tautan https://example.com/cari/bahasa-indonesia/halaman/1 untuk pencarian.",
     ["Gunakan tautan https://example.com/cari/bahasa-indonesia/halaman/1 untuk pencarian."]),

    # 53) Email address at sentence end followed by new sentence
    ("Kirimkan berkas Anda ke info@perusahaan.co.id. Kami akan segera merespons.",
     ["Kirimkan berkas Anda ke info@perusahaan.co.id.", "Kami akan segera merespons."]),

    # 54) Email address mid-sentence is not a sentence boundary
    ("Untuk informasi lebih lanjut, hubungi budi.santoso@univ.ac.id atau kunjungi kantor kami.",
     ["Untuk informasi lebih lanjut, hubungi budi.santoso@univ.ac.id atau kunjungi kantor kami."]),

    # --- Markdown ---

    # 55) Markdown inline link is not a sentence boundary
    ("Baca [panduan lengkap](https://docs.example.com/panduan.html) untuk memulai penggunaan.",
     ["Baca [panduan lengkap](https://docs.example.com/panduan.html) untuk memulai penggunaan."]),

    # 56) Markdown bold marker followed by sentence content is not a sentence boundary
    ("**Penting:** Jangan lupa membawa dokumen asli ke kantor pada hari yang ditentukan.",
     ["**Penting:** Jangan lupa membawa dokumen asli ke kantor pada hari yang ditentukan."]),

    # 57) Markdown heading with decimal section number is not a sentence boundary
    ("## 2.1 Latar Belakang Masalah",
     ["## 2.1 Latar Belakang Masalah"]),

    # 58) Markdown inline code containing dots is not a sentence boundary
    ("Jalankan perintah `pip install pysbd` untuk menginstal pustaka ini di sistem Anda.",
     ["Jalankan perintah `pip install pysbd` untuk menginstal pustaka ini di sistem Anda."]),

    # 59) Markdown ordered list items are split correctly
    ("1. Unduh formulir pendaftaran 2. Isi data diri dengan lengkap 3. Kirimkan ke kantor terdekat",
     ["1. Unduh formulir pendaftaran", "2. Isi data diri dengan lengkap", "3. Kirimkan ke kantor terdekat"]),

    # 60) Multiple sentences containing URLs and plain text
    ("Laporan tersedia di https://laporan.go.id/2024/ringkasan.pdf. Harap dibaca sebelum rapat.",
     ["Laporan tersedia di https://laporan.go.id/2024/ringkasan.pdf.", "Harap dibaca sebelum rapat."]),
]
