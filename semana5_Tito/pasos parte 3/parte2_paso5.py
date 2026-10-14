from nltk.corpus import stopwords 
stop_es = set(stopwords.words("spanish")) 
def quitar_stopwords(texto):    
    tokens = texto.split()    
    utiles = [t for t in tokens if t not in stop_es]    
    return " ".join(utiles)

frase = "dónde está la biblioteca de la escuela" 
print(quitar_stopwords(frase))