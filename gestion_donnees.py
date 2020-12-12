#####
#   YOUNESS MOUAD (20 132 250)
#   EL MAHDI ZOUHAIR
###

import numpy as np
import matplotlib.pyplot as plt

class GestionDonnees:
    def __init__(self, nb_train, nb_test, bruit):
        self.nb_train = nb_train
        self.nb_test = nb_test
        self.bruit = bruit

    def generer_donnees(self):
        