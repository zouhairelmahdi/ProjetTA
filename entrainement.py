##############################
#YOUNESS MOUAD (20 132 250)
#EL MAHDI ZOUHAIR (20 132 241)
###############################

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import make_scorer, accuracy_score

def classifier_donnees(classifieur, params, x_entrain, y_entrain, x_test, y_test):
    """
    Cette méthode est pour entrainer le classifieur en utilisant la gridSearch
    params: dictionnaire des hyperparamètres
    x_entrain, y_entrain: données d'entrainement
    x_test, y_test: données de test
    """
    
    #indices de division equilibirée (stratification)
    indices_validation_croisee = StratifiedKFold(n_splits=5, shuffle=True)
    #definir la justesse comme score
    justesse_score = make_scorer(accuracy_score)
    
    #appliquer la recherche par grille à l'estimateur
    grille_recherche = GridSearchCV(estimator=classifieur,
                        param_grid=params,
                        scoring=justesse_score,
                        cv=indices_validation_croisee)
    
    #entrainer le modèle à nouveau après l'obtention des meilleurs hyperparametres
    grille_recherche.fit(x_entrain, y_entrain)
    
    #prediction des données d'entrainement et de test
    prediction_entrain = grille_recherche.predict(x_entrain)
    prediction_test = grille_recherche.predict(x_test)
    
    #calcul de la justesse d'entrainement et de test
    justesse_entrain = accuracy_score(y_entrain, prediction_entrain)
    justesse_test = accuracy_score(y_test, prediction_test)

    #justesse moyenne trouvée lors de la validation croisée pour le meilleur classifieur
    meilleure_justesse = grille_recherche.best_score_ 

    #meilleurs hyperparamètres trouvés
    meilleurs_params = grille_recherche.best_params_

    #meilleur estimateur trouvé
    meilleur_classifieur = grille_recherche.best_estimator_
    
    resultat = {}
    
    #mettre les résultat dans un dictionnaire
    resultat['justess_entrain'] = justesse_entrain
    resultat['justess_test'] = justesse_test
    resultat['meilleure_justesse'] = meilleure_justesse
    resultat['meilleurs_params'] = meilleurs_params
    resultat['meilleur_classifieur'] = meilleur_classifieur
    
    return resultat