from pathlib import Path
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import create_learning_path
from explanation_module import explain_topic

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent

app.mount("/static", StaticFiles(directory=BASE_DIR/"static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR/"templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/explain")
def explain(request: Request, topic: str = Form(...)):
    return {"result": explain_topic(topic)}


@app.post("/ask")
def ask(request: Request, question: str = Form(...)):
    return {"result": answer_question(question)}


@app.post("/quiz")
def quiz(request: Request, passage: str = Form(...)):
    return {"result": generate_quiz(passage)}


@app.post("/summarize")
def summarize(request: Request, text: str = Form(...)):
    return {"result": summarize_text(text)}


@app.post("/learning-path")
def learning_path(request: Request, topic: str = Form(...)):
    return {"result": create_learning_path(topic)}