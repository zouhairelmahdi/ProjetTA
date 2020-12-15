##############################
#YOUNESS MOUAD (20 132 250)
#EL MAHDI ZOUHAIR (20 132 241)
###############################

import numpy as np
import matplotlib.pyplot as plt

def afficher_graphe_justesse(resultats, bruit, gaussienne):
	"""
	Cette fonction sert à afficher le diagramme en batons des justesses d'entrainement et test pour tous les classifieurs
	pour un cas donnée(bruit, gaussienne)
	resultats: dictionnaire qui contient les résultats pour chaque classifieur
	bruit et gaussienne: sont des booleans
	"""

	#récuperer les noms des classifieurs
    classifieurs = resultats.keys()

    #récupérer les justesses d'entrainement et de test
    justesse_entrain = [resultats[resultat]['justess_entrain'] for resultat in resultats]
    justesse_test = [resultats[resultat]['justess_test'] for resultat in resultats]

    
    large = 0.3 #largeur du baton 
    plt.subplots(figsize=(10,6))
    plt.margins(0.04, 0.1) #ajouter la marge 0.1 en haut pour bien afficher la légende
    bar1 = np.arange(len(classifieurs))
    bar2 = [i+large for i in bar1]

    #construction des batons pour chaque justesse
    plt.bar(bar1, justesse_entrain, large, label='Justesse entrainement', color='tomato')
    plt.bar(bar2, justesse_test, large, label='Justesse test', color='steelblue')

    plt.xticks(bar1+large/2, classifieurs, rotation=50)
    plt.xlabel('Classifieurs')
    plt.ylabel('Justesse')
    plt.legend(loc=9, ncol=2)

    #titre qui montre le cas des classifieurs
    plt.title(f"Justesses des classifieurs avec bruit = {bruit!s} et distribution gaussienne = {gaussienne!s}.")
    plt.show()
    
def visualisation_justesse_cas_gaussienne(justesse_non_gaussienne, justesse_gaussienne):
	"""
	Cette fonction sert à afficher deux diagrammes en batons un pour la justesse d'entrainement et l'autre pour la justesse de test
	et ceci pour tous classifieurs pour la distribution gaussienne et non gaussienne
	justesse_non_gaussienne: dictionnaire des résultats cas distribution non gaussienne
	justesse_gaussienne: dictionnaire des résultats cas distribution gaussienne
	"""

	#récuperer les noms des classifieurs
    classifieurs = justesse_non_gaussienne.keys()
    
    #recupérer les justesses
    justesses_entrain_non_gaussienne = [justesse_non_gaussienne[c]['justess_entrain'] for c in classifieurs]
    justesses_entrain_gaussienne = [justesse_gaussienne[c]['justess_entrain'] for c in classifieurs]
    
    justesses_test_non_gaussienne = [justesse_non_gaussienne[c]['justess_test'] for c in classifieurs]
    justesses_test_gaussienne = [justesse_gaussienne[c]['justess_test'] for c in classifieurs]
    

    cas_justesses = ['entrainement', 'test']
    valeurs = [[justesses_entrain_non_gaussienne, justesses_entrain_gaussienne],
               [justesses_test_non_gaussienne, justesses_test_gaussienne]]

    #boucle pour afficher les deux diagrammes un pour l'entrainement et l'autre pour le test
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
    
    
    
    
    
    