##############################
#YOUNESS MOUAD (20 132 250)
#EL MAHDI ZOUHAIR (20 132 241)
###############################

import numpy as np
import matplotlib.pyplot as plt

def afficher_graphe_justesse(resultats, bruit, gaussienne):
    classifieurs = resultats.keys()
    justesse_entrain = [resultats[resultat]['justess_entrain'] for resultat in resultats]
    justesse_test = [resultats[resultat]['justess_test'] for resultat in resultats]

    large = 0.3
    plt.subplots(figsize=(10,6))
    plt.margins(0.04, 0.1)  
    bar1 = np.arange(len(classifieurs))
    bar2 = [i+large for i in bar1]

    plt.bar(bar1, justesse_entrain, large, label='Justesse entrainement', color='tomato')
    plt.bar(bar2, justesse_test, large, label='Justesse test', color='steelblue')

    plt.xticks(bar1+large/2, classifieurs, rotation=50)
    plt.xlabel('Classifieurs')
    plt.ylabel('Justesse')
    plt.legend(loc=9, ncol=2)
    plt.title(f"Justesses des classifieurs avec bruit = {bruit!s} et distribution gaussienne = {gaussienne!s}.")
    plt.show()
    
def visualisation_justesse_cas_gaussienne(justesse_non_gaussienne, justesse_gaussienne):
    classifieurs = justesse_non_gaussienne.keys()
    
    justesses_entrain_non_gaussienne = [justesse_non_gaussienne[c]['justess_entrain'] for c in classifieurs]
    justesses_entrain_gaussienne = [justesse_gaussienne[c]['justess_entrain'] for c in classifieurs]
    
    justesses_test_non_gaussienne = [justesse_non_gaussienne[c]['justess_test'] for c in classifieurs]
    justesses_test_gaussienne = [justesse_gaussienne[c]['justess_test'] for c in classifieurs]
    
    cas_justesses = ['entrainement', 'test']
    valeurs = [[justesses_entrain_non_gaussienne, justesses_entrain_gaussienne],
               [justesses_test_non_gaussienne, justesses_test_gaussienne]]
    for i in range(2):
        cas_justesse = cas_justesses[i]
        justesses = valeurs[i]
        large = 0.3
        plt.subplots(figsize=(10,6))
        plt.margins(0.04, 0.1)  
        bar1 = np.arange(len(classifieurs))
        bar2 = [i+large for i in bar1]
        
        plt.bar(bar1, justesses[0], large, label='non gaussienne', color='tomato')
        plt.bar(bar2, justesses[1], large, label='gaussienne', color='steelblue')

        plt.xticks(bar1+large/2, classifieurs, rotation=50)
        plt.xlabel('Classifieurs')
        plt.ylabel(f"Justesses d'{cas_justesse!s}")
        plt.legend(loc=9, ncol=2)
        plt.title(f"Justesses d'{cas_justesse!s} des classifieurs en fonction de la nature de distribution")
        plt.show()
    
    
    
    
    
    