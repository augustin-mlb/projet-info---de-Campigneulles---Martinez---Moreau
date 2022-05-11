import gzip
import json

# Dossier où se trouve le fichier :
folder = "C:/Users/Moreau/OneDrive/Desktop/Données/Fichiers de Données .json.gz-20220508/données_électricité/"
filename = "2013-01.json.gz"
with gzip.open(folder + filename, mode='rt') as gzfile :
    data = json.load(gzfile)
  
donnees_elec = Donnees([])
i=0
for variable in data[0]:
    donnees_elec.insererColonne(Variable(variable,[],str(type(variable))),i)
    i=i+1)
