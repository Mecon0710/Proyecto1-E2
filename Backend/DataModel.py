from pydantic import BaseModel

class DataModel(BaseModel):

# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
    serial_no: float
    gre_score: float
    toefl_score: float
    university_rating: float
    sop: float
    lor: float 
    cgpa: float
    research: float
    admission_points: float


#Esta función retorna un diccionario con los atributos del modelo
    def to_dict(self):
        return {
            "Serial No.": self.serial_no,
            "GRE Score": self.gre_score,
            "TOEFL Score": self.toefl_score ,
            "University Rating": self.university_rating,
            "SOP": self.sop,
            "LOR": self.lor,
            "CGPA": self.cgpa,
            "Research": self.research,
            "Admission Points": self.admission_points
        }
#Esta función retorna los nombres de las columnas correspondientes con el modelo exportado en joblib.
    def columns(self):
        return ["Serial No.","GRE Score","TOEFL Score","University Rating","SOP","LOR" ,"CGPA","Research","Admission Points"]
