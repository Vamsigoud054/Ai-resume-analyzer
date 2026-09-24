from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import os

from app.resume_parser import extract_text_from_pdf
from app.llm_service import analyze_resume

app = FastAPI(title="AI Resume Analyzer")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/analyze", response_class=HTMLResponse)
async def analyze(
    request: Request,
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        resume.filename
    )

    with open(file_path, "wb") as file:
        file.write(await resume.read())

    resume_text = extract_text_from_pdf(file_path)

    result = analyze_resume(
        resume_text,
        job_description
    )

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": result
        }
    )
