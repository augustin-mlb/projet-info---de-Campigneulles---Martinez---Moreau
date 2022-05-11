import gzip
import csv
from donnees2 import Donnees
from variable import Variable

# Dossier où se trouve le fichier :
folder = 'C:/Users/Moreau/OneDrive/Desktop/Données/Fichiers de Données .csv.gz-20220508/données_météo/'
filename = 'synop.201301.csv.gz'
data = []
with gzip.open(folder + filename, mode='rt') as gzfile :
    synopreader = csv.reader(gzfile, delimiter=';')
    for row in synopreader :
        data.append(row)

donnees_meteo = Donnees([])
i=0
for variable in data[0]:
    donnees_meteo.insererColonne(Variable(variable,[],str(type(variable))),i)
    i=i+1

for i in range(1,len(data)):
   donnees_meteo.insererLigne(data[i],i)
