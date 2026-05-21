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
]
