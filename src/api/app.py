import pandas as pd
from flask import Flask

app = Flask(__name__)


@app.route("/api/<name>", methods=["GET"])
def get_historic(name: str) -> tuple[str, int]:
    msg = f"Hello {name}!\n"

    return msg, 200
