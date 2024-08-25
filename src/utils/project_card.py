import os
import nbformat
import yaml


filename = "./../../resources/project-card.ipynb"
with open(filename, "r") as f:
    nb = nbformat.read(f, as_version=4)


