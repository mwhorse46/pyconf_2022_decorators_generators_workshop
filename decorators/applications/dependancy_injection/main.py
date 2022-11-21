from flask import Flask, jsonify
from utils import inject, Query

app = Flask("PyconDI")


@app.errorhandler(Exception)
def handle(e: Exception):
    res = jsonify({"error": str(e)})
    res.status_code = 400
    return res


@app.get("/sample")
@inject
def sample(name: str = Query("wow")):
    return f"Hi {name}"


if __name__ == "__main__":
    app.run(debug=True)
