from flask import Flask, Response, redirect, request

app = Flask(__name__)

from app import clock, alarm, errors