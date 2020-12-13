##############################
#YOUNESS MOUAD (20 132 250)
#EL MAHDI ZOUHAIR (20 132 241)
###############################
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold

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
        chemin_test = './data/test.csv'
        les_donnees_entrain = pd.read_csv(chemin_entrain)
        les_donnees_test = pd.read_csv(chemin_test)

        id_entrain = les_donnees_entrain.pop('id')
        classes = les_donnees_entrain.pop('species')
        id_test = les_donnees_test.pop('id')
        
        y_entrain = LabelEncoder().fit(classes).transform(classes)
        
        if(self.distribution_gaussienne):
            x_entrain = StandardScaler().fit(les_donnees_entrain).transform(les_donnees_entrain)
            x_test = StandardScaler().fit(les_donnees_test).transform(les_donnees_test)
        else:
            x_entrain = les_donnees_entrain.values
            x_test = les_donnees_test.values
        
        return id_entrain, x_entrain, y_entrain, id_test, x_test
    
    def generer_donnees_validation_croisee(self, x_entrain, y_entrain):
        """
        Generer les donnees pour k=10 validation croisee tel que les 10 sous ensembles contiennent toutes les classes (Stratification)
        """
        skf = StratifiedKFold(n_splits=10, shuffle=True) #shuffle: mélanger les données

    
    
    
    
    
    
    
    
    
    
    