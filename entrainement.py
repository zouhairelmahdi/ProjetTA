##############################
#YOUNESS MOUAD (20 132 250)
#EL MAHDI ZOUHAIR (20 132 241)
###############################

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import make_scorer, accuracy_score

def classifier_donnees(classifieur, params, x_entrain, y_entrain, x_test, y_test):
    
    indices_validation_croisee = StratifiedKFold(n_splits=5, shuffle=True)
    justesse_score = make_scorer(accuracy_score)
    
    grille_recherche = GridSearchCV(estimator=classifieur,
                        param_grid=params,
                        scoring=justesse_score,
                        cv=indices_validation_croisee)
    
    grille_recherche.fit(x_entrain, y_entrain)
    
    prediction_entrain = grille_recherche.predict(x_entrain)
    prediction_test = grille_recherche.predict(x_test)
    
    justesse_entrain = accuracy_score(y_entrain, prediction_entrain)
    justesse_test = accuracy_score(y_test, prediction_test)

    meilleure_justesse = grille_recherche.best_score_
    meilleurs_params = grille_recherche.best_params_
    meilleur_classifieur = grille_recherche.best_estimator_
    
    resultat = {}
    
    resultat['justess_entrain'] = justesse_entrain
    resultat['justess_test'] = justesse_test
    resultat['meilleure_justesse'] = meilleure_justesse
    resultat['meilleurs_params'] = meilleurs_params
    resultat['meilleur_classifieur'] = meilleur_classifieur
    
    return resultat