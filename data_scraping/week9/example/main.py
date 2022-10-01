import base64
import os
import io

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from unicodedata import numeric
from fastapi import FastAPI, Form, File, Request, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


matplotlib.use('Agg')
app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

@app.get("/")
async def root(request: Request, message='Metalists!'):
    return templates.TemplateResponse(
        'index.html',
        {
            'request': request,
            'message': message
        })

@app.get("/lib")
async def get_lib(request: Request):
    books = os.listdir('static/lib')
    return templates.TemplateResponse(
        'lib.html',
        {
            'request': request,
            'books': books
        })

@app.post("/upload_book")
async def upload(
    request: Request,
    name:str = Form(...),
    book_file: UploadFile = File(...)):
    file_name = '_'.join(name.split()) + '.txt'
    save_path = f'static/lib/{file_name}'
    with open(save_path, 'wb') as f:
        for line in book_file.file:
            f.write(line)

    return {'result': 'success'}

@app.post("/show_plot")
async def show_plot(request: Request, numbers:str = Form(...)):
    numbers = list(map(int, numbers.split(',')))

    fig = plt.figure()
    plt.plot(numbers)
    png_image = io.BytesIO()
    fig.savefig(png_image)
    encoded = base64.b64encode(png_image.getvalue()).decode('ascii')
    return templates.TemplateResponse(
        'plot.html',
        {
            'request': request,
            'numbers': numbers,
            'image': encoded
        })


@app.get("/solve")
async def root(request: Request, a: int, b: int, c: int):
    roots = np.unique(np.roots([a, b, c]))
    roots = sorted(roots)
    return { 'roots': roots }