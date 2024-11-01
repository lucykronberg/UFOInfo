from flask import Flask, request, url_for, render_template, flash
from markupsafe import Markup
from datetime import datetime

import os
import json

app = Flask(__name__)


@app.route('/')
def render_about():
    return render_template('info.html')

@app.route('/location')
def render_popularity():
    with open('ufo_sightings.json') as UFO_data:
        weeks = json.load(UFO_data)
    states=shape_by_state()
    if 'state' in request.args:
        state = request.args['state']
        mostCommon = see_location_shape(state)
        return render_template('location.html', stateList=states, mostCommon=mostCommon)
            
    return render_template('location.html',stateList=states)
    

@app.route('/timeline')
def render_databyshow():
    with open('ufo_sightings.json') as UFO_data:
        weeks = json.load(UFO_data)
   
    return render_template('timeline.html', dataPoints=total_sightings(weeks))
    
def total_sightings(weeks):
    years= {}
    for w in weeks:
        year = w["Dates"]["Sighted"]["Year"]
        if year not in years:
            years[year] = 1
        else:
            years[year] = years[year] + 1 
            
    years = dict(sorted(years.items()))
    #del years[1940]
    #del years[2022]
    
    code = "["
    for year, gross in years.items():
        code = code + Markup("{ x: '" + str(year) + "', y: " + str(gross) + " },")
    code = code[:-1] #remove the last comma
    code = code + "]"
    print(code)
    return code
    


def see_location_shape(location):
    with open('ufo_sightings.json') as ufo_data:
        sightings = json.load(ufo_data)
    counts = {}
    for s in sightings:
        if s["Location"]["State"]==location:
            if s["Data"]["Shape"] in counts and s["Data"]["Shape"] != "light":
                counts[s["Data"]["Shape"]] = counts[s["Data"]["Shape"]] + 1
            else:
                counts[s["Data"]["Shape"]] = 1
    print(counts)
    max = 0
    mostCommon = ""
    for key,value in counts.items():
        if value > max:
            max = value
            mostCommon=key
            
    return mostCommon
        

def shape_by_state():
    with open('ufo_sightings.json') as ufo_data:
        sightings = json.load(ufo_data)
    states=list(set([s["Location"]["State"] for s in sightings])) #sets do not allow duplicates and the set function is optimized for removing duplicates
    return states    
   
if __name__ == '__main__':
    app.run(debug=False) # change to False when running in production