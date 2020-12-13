from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import make_scorer, accuracy_score

def classifier_donnees(classifieur, params, x_entrain, y_entrain, x_test):
    
    indices_validation_croisee = StratifiedKFold(n_splits=5, shuffle=True)
    justesse_score = make_scorer(accuracy_score)
    
    grille_recherche = GridSearchCV(estimator=classifieur,
                        param_grid=params,
                        scoring=justesse_score,
                        cv=indices_validation_croisee)
    
    grille_recherche.fit(x_entrain, y_entrain)
    prediction = grille_recherche.predict(x_test)
    return prediction
    
    
    
    
