from flask import Flask, request, url_for, render_template, flash
from markupsafe import Markup
from datetime import datetime

import os
import json

app = Flask(__name__)

with open('ufo_sightings.json') as ufo_data:
    sightings = json.load(ufo_data)
counts = {}
for num in numbers:
    if num in counts:
        counts[num] = counts[num] + 1
    else:
        counts[num] = 1
    