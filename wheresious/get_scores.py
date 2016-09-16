# initial imports
import pandas as pd
import os.path

# fire up the US Census Geocode
from censusgeocode import CensusGeocode
cg = CensusGeocode()

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
            if n_attempts >= 1:
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
                if n_attempts >= 1:
                    break

    # see if we got a result
    try:
        # get census tract
        tract = float(address_info[0]['geographies']['Census Tracts'][0]['TRACT'])

        # read-in business scores for all census tracts
        filename = '/Users/jsilverman/insight/project/wheresious/static/tracts_scores_'+str(naics_code_simple)+'.csv'
        if os.path.isfile(filename):        
            tracts_scores = pd.read_csv(filename,sep=' ',names=['tracts','scores'])
        else:
            tracts_scores = pd.read_csv('/Users/jsilverman/insight/project/wheresious/static/tracts_scores_all.csv',sep=' ',names=['tracts','scores'])

        # find score for input census tract (possibly use business code as well)
        return float(tracts_scores[tracts_scores.tracts==tract].scores.to_string(index=False))

    except:
        return -1



# get scores for all census tracts and return a heatmap of the scores
# possibly using the NAICS code as well
def all_scores(naics_code_simple):
    # read-in business scores for all census tracts

    # turn scores and tracts into a heat map (possibly use business code as well)
    score_map = [1.]
    
    return score_map
