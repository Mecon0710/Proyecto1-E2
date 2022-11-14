
import string
import json
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from Backend.PredictionModel import Model

app = FastAPI()
app.mount("/Fronted",StaticFiles(directory = "Fronted"), name = "Fronted")
templates = Jinja2Templates(directory="Fronted")

@app.get("/",response_class=HTMLResponse)
def read_root(request: Request):
   return templates.TemplateResponse("index.html", {"request":request, "message": "hola"})

@app.post("/calcularModelo")
async def calcularModelo(request: Request):
   input = await request.json()
   d = make_predictions(input["data"])
   result = {"data": d}
   encode = json.dumps(result)
   return Response(content=encode,media_type="application/json")

def make_predictions (texto: string):
   model = Model()
   result = model.make_predictions(texto)
   if result == "non-suicide":
      result = "no suicida"
   else:
      result = "suicida"
   
   res = "La frase de considera " + result
   return res



