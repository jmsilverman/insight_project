# initial imports
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2

# fire up the US Census Geocode
from censusgeocode import CensusGeocode
cg = CensusGeocode()

# fire up the PostgreSQL DB
user = 'jsilverman'
host = 'localhost'
dbname = 'wheresious'
db = create_engine('postgres://%s%s/%s'%(user,host,dbname))
con = None
con = psycopg2.connect(database = dbname, user = user)

# initialize current city and state
city_state = 'San Diego, CA'



# get a business score for a give address
# possibly using the NAICS code as well
def one_score(address,naics_code_simple):
    # escape any quotes
    address = address.replace("'","''")
    address = address.replace('"','""')

    # strip whitespace at beginning and end
    address = address.strip()

    # try to look up address (assuming they included city in address), at most 5 times
    n_attempts = 0
    address_info = []
    while True:
        try:
            n_attempts += 1
            address_info = cg.onelineaddress(address)
            break
        except:
            if n_attempts >= 5:
                break

    # if no result found, try again with city and state appended, at most 5 times
    if len(address_info) == 0:
        n_attempts = 0
        while True:
            try:
                n_attempts += 1
                address_info = cg.onelineaddress(address+', '+city_state)
                break
            except:
                if n_attempts >= 5:
                    break

    # see if we got a result
    if len(address_info) != 0:
        # get census tract
        try:
            tract = str(address_info[0]['geographies']['Census Tracts'][0]['TRACT'])
        except:
            tract = '-1'
    else:
        tract = '-1'

    # read-in business scores for all census tracts
    scores = pd.read_csv('~/insight/project/wheresious/static/sd_active_businesses.csv')
    
    # find score for input census tract (possibly use business code as well)
    return tract

    # convert address to upper case
    address_upper = address.upper()

    
    # strip whitespace from input addresses
    #scores.address_str = scores.address_str.map(lambda x: x.strip())
    # find the business name for the input address
    #score = scores.loc[scores.address_str==address_upper].doing_bus_as_name.to_string(index=False)
    
    # query sd_businesses database
    query = "SELECT doing_bus_as_name FROM sd_active_businesses WHERE address_str='%s '" % address_upper
    query_results = pd.read_sql_query(query,con)
    # save address
    if len(query_results) > 0:
        score = query_results.iloc[0]['doing_bus_as_name']
    else:
        score = "Address not found"
    return score



# get scores for all census tracts and return a heatmap of the scores
# possibly using the NAICS code as well
def all_scores(naics_code_simple):
    # read-in business scores for all census tracts

    # turn scores and tracts into a heat map (possibly use business code as well)
    score_map = [1.]
    
    return score_map
