from faker import Faker
from flask import Flask, jsonify
import csv
import requests

app = Flask(__name__)
fake = Faker()


@app.route("/requirements/")
def requirement():
    with open('requirements.txt', 'r') as file:
        d = file.read().splitlines()
    return jsonify(d)


@app.route("/generate-users/")
def generate_users():
    g = {}
    for _ in range(100):
        g.setdefault(fake.first_name(), fake.free_email())
    return g


@app.route("/mean/")
def mean():
    with open('hw.csv', 'r') as file:
        h_row, w_row = [], []
        reader = csv.DictReader(file)
        for row in reader:
            h_row.append(float(row[' "Height(Inches)"']))
            w_row.append(float(row[' "Weight(Pounds)"']))
        total_h = str(sum(h_row) / len(h_row))
        total_w = str(sum(w_row) / len(w_row))
        return f'Average height = {total_h}; Average weight = {total_w}'


@app.route("/space/")
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    a = len(r.json()["people"])
    return f'Number of astronauts at the moment - {a}'
