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

        chemin_entrain = './data/train.csv'
        chemin_nouveau_test = './data/test.csv'
        donnees_entrain = pd.read_csv(chemin_entrain)
        donnees_nouveau_test = pd.read_csv(chemin_nouveau_test)
        
        donnees_entrain.pop('id')
        classes = donnees_entrain.pop('species')
        y = LabelEncoder().fit(classes).transform(classes)
        
        id_test = donnees_nouveau_test.pop('id')
        
        if(self.bruit):
            mu, sigma = 0, 0.1
            bruit_ = np.random.normal(mu, sigma, donnees_entrain.shape)
            donnees_entrain = donnees_entrain + bruit_
        
        if(self.distribution_gaussienne):
            x = StandardScaler().fit(donnees_entrain).transform(donnees_entrain)
            x_nouveau_test = StandardScaler().fit(donnees_nouveau_test).transform(donnees_nouveau_test)
        else:
            x = donnees_entrain.values
            x_nouveau_test = donnees_nouveau_test.values
           
        x_entrain, x_test, y_entrain, y_test = train_test_split(x, y, train_size=0.8, random_state=0, shuffle=True)
             
        return x_entrain, y_entrain, x_test, y_test, x_nouveau_test
    
    
    
    
    
    
    
    
    
    
    