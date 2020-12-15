##############################
#YOUNESS MOUAD (20 132 250)
#EL MAHDI ZOUHAIR (20 132 241)
###############################
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


class GestionDonnees:
    def __init__(self, distribution_gaussienne, bruit):
        """ 
            distribution_gaussienne: True si on veut que les donnees suivent une distribution gaussienne
            bruit: présence du bruit
        """
        self.distribution_gaussienne = distribution_gaussienne
        self.bruit = bruit

    def generer_donnees(self):

        #lire le csv des données
        chemin_entrain = './data/train.csv'
        donnees_entrain = pd.read_csv(chemin_entrain)
        
        #eliminer la colonne Id
        donnees_entrain.pop('id')

        #mettre les classes dans un tableau
        classes = donnees_entrain.pop('species')
        #encoder les classes pour obtenir un tableau des cibles
        y = LabelEncoder().fit(classes).transform(classes)
                
        if(self.bruit):
            #ajouter un bruit gaussien au données
            mu, sigma = 0, 0.1
            bruit_ = np.random.normal(mu, sigma, donnees_entrain.shape)
            donnees_entrain = donnees_entrain + bruit_
        
        if(self.distribution_gaussienne):
            #mettre les données sous une distribution gaussienne
            x = StandardScaler().fit(donnees_entrain).transform(donnees_entrain)
        else:
            #bruit False et gaussienne False: récuperer les valeurs
            x = donnees_entrain.values
           
        #diviser les données en un ensemble de test et de l'entrainement
        x_entrain, x_test, y_entrain, y_test = train_test_split(x, y, train_size=0.8, random_state=0, shuffle=True)


        return x_entrain, y_entrain, x_test, y_test
    
    
    
    
    
    
    
    
    
    
    