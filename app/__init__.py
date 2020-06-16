from flask import Flask, Response, redirect

app = Flask(__name__)

from app import clock, alarm, errors