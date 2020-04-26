import re

# declare constant regex times
hari = '(?:senin|selasa|rabu|kamis|jumat|sabtu|minggu)?'
bulan = '(?:januari|februari|maret|april|mei|juni|juli|agustus|september|oktober|november|desember)'
ketwaktu = '(?:sekarang|kemarin|pagi|sore|malam|siang)?'
lanjutwaktu = '(?:sampai|hingga|pada|saat)'
jamkata = '(?:jam|pukul)'
jamangka = '(?:\d{2}\.\d{2})'
jamket = '(?:wib|wit|wita|pm|am)'
jamwaktu = '(?:' + jamkata + '\s' + jamangka + '\s' + jamket + ')?'
tanggalangka = '(?:\(\d{1,2}/\d{1,2}/\d+\))?'
tanggalhuruf = '(?:\d{1,2}\s(?:' + bulan + ')\s\d+)?'
rwaktu = '(?:' + hari + '\s?' + ketwaktu + '\s?' + tanggalhuruf + '\s?' + tanggalangka + ',?\s?' + jamwaktu + ')'
regexwaktu = rwaktu + '\s?(?:' + lanjutwaktu + '\s?' + rwaktu + ")?"

# method to get waktu
def getWaktu(kalimat):
    list_waktu = re.findall(regexwaktu, kalimat)
    invalid_list = ["sampai", "hingga", "pada", "saat"]
    for waktu in list_waktu:
        waktu = waktu.strip()
        if len(waktu) <= 1:
            continue
        if waktu in invalid_list:
            continue
        return waktu.replace(',', '').strip()

    return None

# method to get date
def getTanggal(kalimat):
    list_date = re.findall(tanggalangka, kalimat)
    for date in list_date:
        date = date.strip()
        if len(date) <= 1:
            continue
        return date

    list_date = re.findall(tanggalhuruf, kalimat)
    for date in list_date:
        date = date.strip()
        if len(date) <= 1:
            continue
        return date

    return None