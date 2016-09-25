#import numpy as np
from flask import render_template
from flask import request
from wheresious import app
from get_scores import one_score
import numpy as np
import pandas as pd



# define homepage ('/' and index.html)
@app.route('/')
@app.route('/index')
def home():
    # render page
    return render_template("index.html")



# define about page
@app.route('/test')
def test():
    # render page
    return render_template("test.html")



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

    # get score for this address and code
    score = one_score(address,naics_code_simple)

    # read in dataframe of tracts and scores for this code
    if naics_code_simple != 'all':
        df_scores = pd.read_csv('/Users/jsilverman/insight/project/wheresious/static/tracts_scores_'+naics_code_simple+'.csv',index_col=0)
        blurb = 'Only businesses with Highest Level Business (NAICS) Code '+naics_code_simple+' were used to predict this score.'
    else:
        df_scores = pd.read_csv('/Users/jsilverman/insight/project/wheresious/static/tracts_scores.csv',index_col=0)
        blurb = 'All businesses were used to predict this score.'
        
    # get average overall score for SD for this code
    mean_score = int(float(np.mean(df_scores.score)))
    
    # render page
    return render_template("one_address.html", address = address, naics_code_simple = naics_code_simple, score = score, mean = mean_score, code_blurb = blurb)



# define output for entire city map
@app.route('/all_city', methods=['GET'])
def full_city_lookup():
    # pull input field and store it
    naics_code_simple = request.args.get('naics_code_simple')

    if naics_code_simple=='44':
        description = 'Highest Level Business (NAICS) Code: 44 - Retail Trade'
    elif naics_code_simple=='45':
        description = 'Highest Level Business (NAICS) Code: 45 - Retail Trade'
    elif naics_code_simple=='53':
        description = 'Highest Level Business (NAICS) Code: 53 - Real Estate and Rental and Leasing'
    elif naics_code_simple=='54':
        description = 'Highest Level Business (NAICS) Code: 54 - Professional, Scientific, and Technical Services'
    elif naics_code_simple=='56':
        description = 'Highest Level Business (NAICS) Code: 56 - Administrative and Support and Waste Management and Remediation Services'
    elif naics_code_simple=='62':
        description = 'Highest Level Business (NAICS) Code: 62 - Health Care and Social Assistance'
    elif naics_code_simple=='72':
        description = 'Highest Level Business (NAICS) Code: 72 - Accommodation and Food Services'
    elif naics_code_simple=='81':
        description = 'Highest Level Business (NAICS) Code: 81 - Other Services (except Public Administration)'
    else:
        description = 'All Businesses'
        
    # render page
    return render_template("all_city.html", naics_code_simple = naics_code_simple, description = description)
