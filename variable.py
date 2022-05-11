class Variable:
    '''classe qui représente une variable
    
    Attributes
    ----------
    nom_colonne : str
        nom de la variable
    liste_obs : list
        liste des valeurs de la variable pour chaque observation
    nom_type : str
        type de la variable

    Examples
    --------
    >>> age=Variable('age',[12,14,11],'int')
    >>> age.nom_colonne
    'age'
    >>> age.nombreObs()
    3
    '''
    def __init__(self, nom_colonne, liste_obs, nom_type):
        '''constructeur'''
        self.nom_colonne=nom_colonne
        self.liste_obs=liste_obs
        self.nom_type = nom_type

    def nombreObs(self):
        '''retourne le nombre d'observation d'une variable'''
        return len(self.liste_obs)
