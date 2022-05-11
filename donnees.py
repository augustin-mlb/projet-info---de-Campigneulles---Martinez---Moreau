import variable

class Donnees:
    '''classe qui représente un jeu de données
    
    Un jeu de données est représenté par une liste de variables

    Attributes
    ----------
    liste_var : list
        Une liste d'objets de la classe Variable
    
    Examples
    --------
    >>> age=Variable('age',[12,14,11],'int')
    >>> taille=Variable('taille',[156,165,139],'int')
    >>> donnees=Donnees([age, taille])
    >>> donnees.entete()
    ['age', 'taille']
    >>> donnees.corps()
    [[12, 14, 11], [156, 165, 139]]
    '''

    def __init__(self, liste_var):
        '''constructeur'''
        self.liste_var=liste_var

    def nombreVar(self):
        '''retourne'' le nombre de variable d un jeu de donneees'''
        return len(self.liste_var)

    def entete(self):
        '''retourne la liste du nom des variables d un jeu de données'''
        header=[]
        for variable in self.liste_var:
            header=header + [variable.nom_colonne]
        return header
    
    def corps(self):
        '''retourne la liste des valeurs prises par chaque variable pour chaque opération'''
        body=[]
        for variable in self.liste_var:
            body=body + [variable.liste_obs]
        return body
    
    def insererLigne(self, liste_valeurs, position):
        '''permet de renseigner pour chaque variable la valeur d une nouvelle observation à la position indiquée'''
        if len(liste_valeurs)!=len(self.liste_var):
            raise ValueError("variable manquante ou en trop")
        else:
            i=0
            for variable in self.liste_var:
                variable.liste_obs.insert(position, liste_valeurs[i])
                i=i+1
            
    def insererColonne(self, variable, position):
        '''permet de renseigner pour chaque observation la valeur d'une nouvelle variable à la position indiquée'''
        if len(variable.liste_obs)!=len(self.liste_var[1].liste_obs):
            raise ValueError("obs manquante ou en trop")
        else:    
            self.liste_var.insert(position, variable)
        
    def supprimerLigne(self, position):
        '''permet de supprimer pour chaque variable la valeur d'une observation à la position indiquée'''
        for variable in self.liste_var:
            del variable.liste_obs[position]
            
    def supprimerColonne(self, position):
        '''permet de supprimer pour chaque obsrevation la valeur d'une variable à la position indiquée'''
        del self.liste_var[position]

    def retournerColonne(self, nom_var):
        '''permet de retourner à partir du nom d'une variable la liste des valeurs prises par chaque observation'''
        for variable in self.liste_var:
            if variable.nom_colonne == nom_var:
                var_cherchee = variable
        return var_cherchee.liste_obs

if __name__=='__main__':
    import doctest
    doctest.testmod()
