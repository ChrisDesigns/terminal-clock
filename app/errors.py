from app import app, redirect
from werkzeug.exceptions import HTTPException

@app.errorhandler(HTTPException)
def handle_exception():
    return "Invalid syntax, please try to hit /clock" \
    "or /alarm/minute/second (where minute and second are time values."