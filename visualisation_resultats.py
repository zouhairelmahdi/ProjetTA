##############################
#YOUNESS MOUAD (20 132 250)
#EL MAHDI ZOUHAIR (20 132 241)
###############################

import numpy as np
import matplotlib.pyplot as plt

def afficher_graphe_justesse(resultats, bruit, gaussienne):
	classifieurs = resultats.keys()
	justesse_entrain = [resultats[resultat]['justesse_entrain'] for resultat in resultats]
	justesse_test = [resultats[resultat]['justesse_test'] for resultat in resultats]

	large = 0.3
	plt.subplots(figsize=(10,5))

	bar1 = np.arange(len(classifieurs))
	bar2 = [i+large for i in bar1]

	plt.bar(bar1, justesse_entrain, large, label='Justesse entrainement', color='coral')
	plt.bar(bar2, justesse_test, large, label='Justesse test', color='cornflowerblue')

	plt.xticks(bar1+large/2, classifieurs, rotation=45)
	plt.xlabel('Classifieurs')
	plt.ylabel('Justesse')

	plt.title(f"Justesses des classifieurs avec bruit = {bruit!s} et distribution gaussienne = {gaussienne!s}.")
	plt.show()"