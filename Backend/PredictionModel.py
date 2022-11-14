from joblib import load


class Model:

    def __init__(self):
        self.model = load("assets/ProyectoNB.joblib")

    def make_predictions(self, texto):
        result = self.model.predict([texto])
        return result

