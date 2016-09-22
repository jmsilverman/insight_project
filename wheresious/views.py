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

    # read in dataframe of tracts, codes, and scores
    df_scores = pd.read_csv('/Users/jsilverman/insight/project/wheresious/static/tracts_codes_scores.csv',index_col=0)

    # get average overall score for SD
    mean_score = int(float(np.mean(df_scores.score)))
    
    # render page
    return render_template("one_address.html", address = address, naics_code_simple = naics_code_simple, score = score, mean = mean_score)



# define output for entire city map
@app.route('/all_city', methods=['GET'])
def full_city_lookup():
    # pull input field and store it
    naics_code_simple = request.args.get('naics_code_simple')

    if naics_code_simple=='11':
        description = 'Agriculture, Forestry, Fishing and Hunting'
    elif naics_code_simple=='22':
        description = 'Utilities'
    elif naics_code_simple=='23':
        description = 'Construction'
    elif naics_code_simple=='31':
        description = 'Manufacturing'
    elif naics_code_simple=='32':
        description = 'Manufacturing'
    elif naics_code_simple=='33':
        description = 'Manufacturing'
    elif naics_code_simple=='42':
        description = 'Wholesale Trade'
    elif naics_code_simple=='44':
        description = 'Retail Trade'
    elif naics_code_simple=='45':
        description = 'Retail Trade'
    elif naics_code_simple=='48':
        description = 'Transportation and Warehousing'
    elif naics_code_simple=='49':
        description = 'Transportation and Warehousing'
    elif naics_code_simple=='51':
        description = 'Information'
    elif naics_code_simple=='52':
        description = 'Finance and Insurance'
    elif naics_code_simple=='53':
        description = 'Real Estate and Rental and Leasing'
    elif naics_code_simple=='54':
        description = 'Professional, Scientific, and Technical Services'
    elif naics_code_simple=='55':
        description = 'Management of Companies and Enterprises'
    elif naics_code_simple=='56':
        description = 'Administrative and Support and Waste Management and Remediation Services'
    elif naics_code_simple=='61':
        description = 'Educational Services'
    elif naics_code_simple=='62':
        description = 'Health Care and Social Assistance'
    elif naics_code_simple=='71':
        description = 'Arts, Entertainment, and Recreation'
    elif naics_code_simple=='72':
        description = 'Accommodation and Food Services'
    elif naics_code_simple=='81':
        description = 'Other Services (except Public Administration)'
    elif naics_code_simple=='92':
        description = 'Public Administration'
    else:
        description = 'Something went wrong with the NAICS code...'
        
    # render page
    return render_template("all_city.html", naics_code_simple = naics_code_simple, description = description)
