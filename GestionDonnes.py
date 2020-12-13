##############################
#YOUNESS MOUAD (20 132 250)
#EL MAHDI ZOUHAIR (20 132 241)
###############################
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class GestionDonnees:
    def __init__(self, bruit):
        """
            bruit: présence du bruit
        """
        self.bruit = bruit

    def generer_donnees(self):

        chemin_entrain = './data/train.csv'
        chemin_test = './data/test.csv'
        les_donnees_entrain = pd.read_csv(path, sep=',')
        les_donnees_test = pd.read_csv(path, sep=',')      