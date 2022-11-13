from joblib import dump,load
import numpy as np
from sklearn import mean_squared_error as mse


class Model:

    def __init__(self):
        self.model = load("assets/modelo.joblib")

    def make_predictions(self, data):
        result = self.model.predict(data)
        return result

    def retrain(self, data):
        #Separates the data
        X = data.drop('Admission Points', axis=1) 
        y = data['Admission Points']

        #Retrains the model using partial_fit
        self.model = self.model.fit(X,y)

        #Gets the R2 metric
        r_2 = self.model.score(X,y)

        #Gets the RSME metric
        y_true = y
        y_predicted = self.model.predict(X)
        rmse = np.sqrt(mse(y_true, y_predicted))

        #Saves the new model
        dump(self.model,"assets/modelo.joblib")
        return r_2, rmse
