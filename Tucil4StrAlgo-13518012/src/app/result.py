from algorithms.BoyerMooreAlgorithm import searchPatternInTextWithBM
from algorithms.KMPAlgorithm import searchPatternInTextWithKMP
from algorithms.Regex import searchPatternInTextWithRegex
from utils.kalimat import getKalimat
from utils.jumlah import getJumlah
from utils.waktu import getWaktu, getTanggal

def getResults(form):
    # get input results
    filenames = form.get('filenames')
    keyword = form.get('keyword')
    algochoice = int(form.get('algochoice'))

    # get choice of algorithm
    algoritmsChoice = [searchPatternInTextWithBM, searchPatternInTextWithKMP,
        searchPatternInTextWithRegex]
    searchPattern = algoritmsChoice[algochoice - 1]

    # split filenames
    filenames = filenames.strip().split(',')

    # get jumlah, waktu, kalimat, and source
    results = []
    for filename in filenames:
        list_kalimat = getKalimat(filename)
        if list_kalimat == None:
            continue
        
        # filter list_kalimat
        list_kalimat = [x for x in list_kalimat if searchPattern(keyword.lower(), x.lower())]

        # get date first
        tanggal = None
        for kalimat in list_kalimat:
            tanggal = getTanggal(kalimat)
            if tanggal != None:
                break

        # get result
        for kalimat in list_kalimat:
            total_jumlah = getJumlah(kalimat)
            if total_jumlah == None:
                continue
            waktu = getWaktu(kalimat.lower())
            if waktu == None:
                if tanggal == None:
                    continue
                waktu = tanggal
            result = {}
            result['jumlah'] = total_jumlah
            result['waktu'] = waktu
            result['kalimat'] = kalimat
            result['source'] = filename
            results.append(result)
    
    if len(results) == 0:
        return None

    return results