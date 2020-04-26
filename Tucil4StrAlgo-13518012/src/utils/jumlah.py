import re
# Regex for jumlah
regexJumlah = '(?<!\S)\d{1,3}(?:\.\d{3})*(?!\S)'

def getJumlah(kalimat):
    list_jumlah = re.findall(regexJumlah, kalimat)
    for jumlah in list_jumlah:
        if len(jumlah) == 0:
            continue
        return jumlah
    return None
