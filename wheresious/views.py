#import numpy as np
from flask import render_template
from flask import request
from wheresious import app
from get_scores import one_score
from get_scores import all_scores


# define homepage ('/' and index.html)
@app.route('/')
@app.route('/index')
def home():
    # render page
    return render_template("index.html")



# define about page
@app.route('/about')
def about():
    # render page
    return render_template("about.html")



@app.route('/contact')
def contact():
    # render page
    return render_template("contact.html")



# define output for searching a specific address
@app.route('/one_address', methods=['GET'])
def single_lookup():
    # pull input fields and store them
    address = request.args.get('address')
    naics_code_simple = request.args.get('naics_code_simple')

    # get score from external file
    score = one_score(address,naics_code_simple)

    # render page
    return render_template("one_address.html", address = address, naics_code_simple = naics_code_simple, score = score)



# define output for entire city map
@app.route('/all_city', methods=['GET'])
def full_city_lookup():
    # pull input field and store it
    naics_code_simple = request.args.get('naics_code_simple')

    # get map of scores from external file
    score_map = all_scores(naics_code_simple)
    
    # render page
    return render_template("all_city.html", naics_code_simple = naics_code_simple, score_map = score_map)
