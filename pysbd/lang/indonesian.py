# -*- coding: utf-8 -*-
from pysbd.abbreviation_replacer import AbbreviationReplacer
from pysbd.lang.common import Common, Standard


class Indonesian(Common, Standard):

    iso_code = 'id'

    class AbbreviationReplacer(AbbreviationReplacer):
        SENTENCE_STARTERS = (
            "Saya Kami Mereka Dia Ia Anda Kamu Beliau Kita Ini Itu Yang "
            "Dengan Pada Dalam Untuk Dari Ke Di Oleh Sebagai Karena Jika "
            "Meskipun Namun Selain Adapun Berdasarkan Menurut Setelah "
            "Sebelum Ketika Apabila Bahwa Para Semua Banyak Beberapa "
            "Salah Setiap Berbagai Hal Dalam Pihak"
        ).split(" ")

    class Abbreviation(Standard.Abbreviation):
        ABBREVIATIONS = [
            # Titles / honorifics
            'prof', 'dr', 'drg', 'ir', 'drs', 'dra', 'tn', 'ny', 'nn',
            'bpk', 'yth', 'sdr', 'sdri', 'hj', 'h',
            # Academic degrees
            's.e', 's.h', 's.t', 's.pd', 's.sos', 's.kom', 's.ip', 's.psi',
            's.farm', 's.kedg', 'm.m', 'm.si', 'm.pd', 'm.hum', 'm.kes',
            'm.h', 'm.kom', 'ph.d', 'sp',
            # Common Indonesian abbreviations
            'dll', 'dsb', 'dkk', 'dst', 'dlsb', 'tsb', 'svp', 'ybs',
            # Date / time
            'tgl', 's.d',
            # Informal shorthands
            'yg', 'dgn', 'utk',
            # Latin / academic
            'et', 'al',
            # Units
            'km', 'cm', 'mm', 'dm', 'kg', 'gr', 'mg', 'ml', 'lt', 'kw',
            # Address / location
            'jl', 'gg', 'kec', 'kel', 'kab', 'prov', 'no', 'rt', 'rw',
            'kd', 'kp',
            # Months
            'jan', 'feb', 'mar', 'apr', 'jun', 'jul', 'agu', 'sep',
            'okt', 'nov', 'des',
            # Organizations / legal entities
            'pt', 'cv', 'tbk', 'ud', 'kop', 'yay', 'lsm', 'bumn',
            # Document / reference
            'hlm', 'hal', 'vol', 'ed', 'cet', 'tel', 'fax', 'ttd',
            'gbr', 'tbl', 'ref', 'ibid', 'op', 'loc',
            # General
            'dll', 'a.n', 'u.p', 'u.b', 'd.a', 'p.o',
        ]
        PREPOSITIVE_ABBREVIATIONS = [
            'prof', 'dr', 'drg', 'ir', 'drs', 'dra', 'tn', 'ny', 'nn',
            'bpk', 'yth', 'sdr', 'sdri', 'hj', 'h', 'sp', 'jl', 'gg',
            'kec', 'kel', 'kab', 'prov', 'pt', 'cv', 'ud', 'a.n', 'u.b',
        ]
        NUMBER_ABBREVIATIONS = [
            'no', 'tel', 'fax', 'hlm', 'hal', 'vol', 'cet', 'ed', 'rt',
            'rw', 'tgl',
        ]
