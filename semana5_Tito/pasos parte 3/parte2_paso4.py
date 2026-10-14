from nltk.corpus import stopwords 

stop_es = set(stopwords.words("spanish"))
print("Cantidad:", len(stop_es)) 
print(list(stop_es)[:30])