"""Page providers setup"""
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader("src.main.pages"))
