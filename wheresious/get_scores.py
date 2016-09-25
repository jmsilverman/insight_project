# initial imports
import pandas as pd

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

        # read in dataframe of tracts, codes, and scores
        if naics_code_simple != 'all':
            df_scores = pd.read_csv('/Users/jsilverman/insight/project/wheresious/static/tracts_scores_'+naics_code_simple+'.csv',index_col=0)
        else:
            df_scores = pd.read_csv('/Users/jsilverman/insight/project/wheresious/static/tracts_scores.csv',index_col=0)

        # get correct row of dataframe
        score_row = df_scores[df_scores.census_tract==tract].score

        # return actual score
        return int(round(score_row.values[0]))

    except:
        return -1
