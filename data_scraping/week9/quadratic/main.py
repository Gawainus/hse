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
async def root(request: Request):
    return templates.TemplateResponse(
        'index.html',
        {
            'request': request,
        })

def get_roots(a, b, c):
    roots = np.roots([a, b, c])
    roots = roots[~np.iscomplex(roots)]
    roots = np.unique(roots)
    return sorted(roots)

@app.get("/solve")
async def root(request: Request, a: int, b: int, c: int):
    return { 'roots': get_roots(a, b, c) }

def cal_y(x, coeffs):
    degrees = len(coeffs)
    return sum([coeffs[degrees - i - 1] * x**i for i in range(degrees)])


@app.post("/solve_plot")
async def show_plot(request: Request, coeffs:str = Form(...)):
    a, b, c = list(map(int, coeffs.split(',')))
    function_def = f"y = {a}x^2 + {b}x + {c}"
    roots = get_roots(a, b, c)
    root_desc = ", ".join(map(str, roots))

    fig = plt.figure()
    x = np.linspace(-13, 13, 200)
    if roots:
        plt.plot(x, cal_y(x, [a, b, c]))

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("roots:" + root_desc)

    png_image = io.BytesIO()
    fig.savefig(png_image)
    encoded = base64.b64encode(png_image.getvalue()).decode('ascii')
    return templates.TemplateResponse(
        'solve.html',
        {
            'request': request,
            'function_def': function_def,
            'image': encoded
        })