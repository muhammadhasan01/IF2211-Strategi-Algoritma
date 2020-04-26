import nltk

def getKalimat(path):
    path = "../test/" + path
    try:
        with open(path) as file:
            data = file.read().replace('\n', '')
            return nltk.tokenize.sent_tokenize(data)
    except Exception as e:
        print(e)
        return None