# Importing the libraries/modules

from utils.db import get_resources_module, get_subject_modules, get_subjects
from flask import Flask, render_template
from utils.htmlgen import (
    index_html_gen,
    module_html_gen,
    subject_html_gen,
    subject_html_gen,
)

# Creating the flask app
app = Flask(__name__)

# Creating the flask routes


# Home page route
@app.route("/")
def index():
    subjects = get_subjects()
    subdiv1, subdiv2 = index_html_gen(subjects)

    return (
        render_template("index.html")
        .replace("SUBDIV1", subdiv1)
        .replace("SUBDIV2", subdiv2)
    )


# Subject page route
@app.route("/subject/<subject_code>")
def subject(subject_code):
    subject_code = subject_code.split("-")[0].upper()
    modules = get_subject_modules(subject_code)
    module_html = subject_html_gen(modules)

    return render_template("subject.html", SUBJECT=modules["name"]).replace(
        "MODULE_HTML", module_html
    )


# Module page route
@app.route("/module/<module_code>")
def module(module_code):
    module_code = "-".join(module_code.split("-")[:2]).upper()
    resources = get_resources_module(module_code)
    resource_html = module_html_gen(resources)

    return render_template("module.html", SUBJECT=resources["name"]).replace(
        "RESOURCE_HTML", resource_html
    )
