from fastapi import FastAPI
from .models.model_1 import get_dummy_model, count_parameters

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "OK"}


@app.get("/model-count")
def model_count():
    model = get_dummy_model()
    name = model.name_or_path
    count = count_parameters(model)
    return {"name": name, "count": count}
