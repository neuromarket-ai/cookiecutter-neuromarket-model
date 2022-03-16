{%- if cookiecutter.api|lower == 'gradio' %}
"""GRadio-based service. See https://gradio.app/docs/ for details."""

import sys
import gradio as gr
from {{cookiecutter.project_slug}}.model import Model

model = Model()

def main():
    # TODO: Describe inputs/outputs here
    # Example:
    # image = gr.inputs.Image(shape=(64, 64))
    # label = gr.outputs.Label(num_top_classes=3)
    # gr.Interface(fn=model.process_sample, inputs=image, outputs=label).launch()
    pass

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

{%- endif %}
{%- if cookiecutter.api|lower == 'fastapi' %}
"""Simple FastAPI based service. See https://fastapi.tiangolo.com/ for details."""
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from {{cookiecutter.project_slug}}.model import Model

# TODO: adapt for model inputs
class ModelRequest(BaseModel):
    input: str = Field(..., title="Input data")

# TODO: adapt for mode outputs
class ModelResponse(BaseModel):
    name: str = Field(..., title="Class name")
    score: float = Field(..., example=0.9, title="Class probability")

# Define application
app = FastAPI(
    title="{{cookiecutter.project_name}}",
    version="{{cookiecutter.version}}",
    debug=True)

# Load model to memory
model = Model()

# Define process sample endpoint
@app.post("/api/predict", response_model=ModelResponse, name="predict")
async def predict(request: ModelRequest):
    # TODO: preprocess request before run
    prediction = model.process_sample(request.input)
    return prediction


if __name__ == "__main__":
    uvicorn.run(app, debug=True)

{%- endif %}
