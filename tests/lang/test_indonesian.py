# -*- coding: utf-8 -*-
import pytest
import pysbd

GOLDEN_ID_RULES_TEST_CASES = [
    # Basic sentence splitting
    ("Hari ini cuaca sangat cerah. Saya ingin pergi ke pantai.",
     ["Hari ini cuaca sangat cerah.", "Saya ingin pergi ke pantai."]),

    # Question mark
    ("Apakah kamu sudah makan? Saya belum makan.",
     ["Apakah kamu sudah makan?", "Saya belum makan."]),

    # Exclamation mark
    ("Selamat datang! Semoga betah di sini.",
     ["Selamat datang!", "Semoga betah di sini."]),

    # Title abbreviation Dr. should not split
    ("Pasien itu diperiksa oleh Dr. Budi Santoso. Beliau adalah dokter terbaik.",
     ["Pasien itu diperiksa oleh Dr. Budi Santoso.", "Beliau adalah dokter terbaik."]),

    # Title abbreviation Prof. should not split
    ("Makalah ini ditulis oleh Prof. Ahmad Yani. Beliau mengajar di universitas.",
     ["Makalah ini ditulis oleh Prof. Ahmad Yani.", "Beliau mengajar di universitas."]),

    # Abbreviation dll. should not split
    ("Toko itu menjual baju, celana, sepatu, dll. Harganya sangat terjangkau.",
     ["Toko itu menjual baju, celana, sepatu, dll.", "Harganya sangat terjangkau."]),

    # Abbreviation dkk. should not split
    ("Penelitian ini dilakukan oleh Sari dkk. Hasilnya sangat memuaskan.",
     ["Penelitian ini dilakukan oleh Sari dkk.", "Hasilnya sangat memuaskan."]),

    # Address abbreviation Jl. should not split
    ("Kantor kami berlokasi di Jl. Sudirman No. 10. Silakan berkunjung.",
     ["Kantor kami berlokasi di Jl. Sudirman No. 10.", "Silakan berkunjung."]),

    # Decimal number should not split
    ("Pertumbuhan ekonomi mencapai 5.2 persen tahun ini. Angka ini lebih tinggi dari tahun lalu.",
     ["Pertumbuhan ekonomi mencapai 5.2 persen tahun ini.", "Angka ini lebih tinggi dari tahun lalu."]),

    # Multiple sentences
    ("Indonesia adalah negara kepulauan. Ibukotanya adalah Jakarta. Penduduknya sangat beragam.",
     ["Indonesia adalah negara kepulauan.", "Ibukotanya adalah Jakarta.", "Penduduknya sangat beragam."]),
]

ID_MORE_TEST_CASES = [
    # dsb. should not split
    ("Kegiatan meliputi membaca, menulis, berhitung, dsb. Semua siswa wajib mengikutinya.",
     ["Kegiatan meliputi membaca, menulis, berhitung, dsb.", "Semua siswa wajib mengikutinya."]),

    # No. abbreviation before number
    ("Silakan hubungi kami di No. 021-5551234. Kami siap melayani Anda.",
     ["Silakan hubungi kami di No. 021-5551234.", "Kami siap melayani Anda."]),

    # Month abbreviation
    ("Acara tersebut akan diadakan pada 15 Nov. 2024. Semua peserta diharap hadir.",
     ["Acara tersebut akan diadakan pada 15 Nov. 2024.", "Semua peserta diharap hadir."]),

    # Yth. honorific
    ("Kepada Yth. Bapak Direktur. Dengan hormat, saya ingin mengajukan permohonan.",
     ["Kepada Yth. Bapak Direktur.", "Dengan hormat, saya ingin mengajukan permohonan."]),

    # Mixed punctuation
    ("Benarkah itu? Ya, benar! Saya sudah membuktikannya sendiri.",
     ["Benarkah itu?", "Ya, benar!", "Saya sudah membuktikannya sendiri."]),
]

ID_HYPERLINK_MARKDOWN_TEST_CASES = [
    # URL mid-sentence is not a sentence boundary
    ("Artikel selengkapnya dapat dibaca di https://www.kompas.com/artikel/judul-berita.html untuk informasi terbaru.",
     ["Artikel selengkapnya dapat dibaca di https://www.kompas.com/artikel/judul-berita.html untuk informasi terbaru."]),

    # URL at sentence end followed by new sentence
    ("Silakan kunjungi situs kami di https://www.kemendikbud.go.id. Informasi lebih lanjut tersedia di sana.",
     ["Silakan kunjungi situs kami di https://www.kemendikbud.go.id.", "Informasi lebih lanjut tersedia di sana."]),

    # Indonesian .id TLD inside URL is not a sentence boundary
    ("Portal resmi layanan publik tersedia di https://www.indonesia.go.id/layanan-publik.html setiap saat.",
     ["Portal resmi layanan publik tersedia di https://www.indonesia.go.id/layanan-publik.html setiap saat."]),

    # Email address at sentence end followed by new sentence
    ("Kirimkan berkas Anda ke info@perusahaan.co.id. Kami akan segera merespons.",
     ["Kirimkan berkas Anda ke info@perusahaan.co.id.", "Kami akan segera merespons."]),

    # Email address mid-sentence is not a sentence boundary
    ("Untuk informasi lebih lanjut, hubungi budi.santoso@univ.ac.id atau kunjungi kantor kami.",
     ["Untuk informasi lebih lanjut, hubungi budi.santoso@univ.ac.id atau kunjungi kantor kami."]),

    # Markdown inline link is not a sentence boundary
    ("Baca [panduan lengkap](https://docs.example.com/panduan.html) untuk memulai penggunaan.",
     ["Baca [panduan lengkap](https://docs.example.com/panduan.html) untuk memulai penggunaan."]),

    # Markdown bold marker is not a sentence boundary
    ("**Penting:** Jangan lupa membawa dokumen asli ke kantor pada hari yang ditentukan.",
     ["**Penting:** Jangan lupa membawa dokumen asli ke kantor pada hari yang ditentukan."]),

    # Markdown inline code with dots is not a sentence boundary
    ("Jalankan perintah `pip install pysbd` untuk menginstal pustaka ini di sistem Anda.",
     ["Jalankan perintah `pip install pysbd` untuk menginstal pustaka ini di sistem Anda."]),

    # Multiple sentences containing a URL
    ("Laporan tersedia di https://laporan.go.id/2024/ringkasan.pdf. Harap dibaca sebelum rapat.",
     ["Laporan tersedia di https://laporan.go.id/2024/ringkasan.pdf.", "Harap dibaca sebelum rapat."]),
]


@pytest.mark.parametrize('text,expected_sents', GOLDEN_ID_RULES_TEST_CASES)
def test_id_sbd(id_default_fixture, text, expected_sents):
    segments = id_default_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents


@pytest.mark.parametrize('text,expected_sents', ID_MORE_TEST_CASES)
def test_id_more(id_default_fixture, text, expected_sents):
    segments = id_default_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents


@pytest.mark.parametrize('text,expected_sents', ID_HYPERLINK_MARKDOWN_TEST_CASES)
def test_id_hyperlink_markdown(id_default_fixture, text, expected_sents):
    segments = id_default_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents
