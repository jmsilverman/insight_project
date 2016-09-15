# Files for WhereSIOUS

## My WhereSIOUS project for the City of San Diego while a Insight DS
   Fellow in Fall 2016

Predicts future business success for a given location in San Diego
based on information about that location.

### Presentations (presentations/)

* various presentations for the project (PowerPoint and PDFs)


### WhereSIOUS Website via Flask (wheresious/)

* templates/ - folder of HTML webpages
* static/ - folder of stylesheets, images, icons, and data to be
  served to website
* also contains some external Python scripts
* run.py in the main folder above this one also helps run the Flask-based website


### Jupyter Notebooks (*.ipynb)

* build_features_labels.ipynb - reads in cleaned data and labels and
combines important info into CSV files
* business_listings.ipynb - read in current SD businesses and mess
with the data
* housing_employment_income.ipynb - read in housing, employment, and
income data from the census and output relevant info
* lin_reg_training.ipynb - try to fit data with linear regression
* parking_meters.ipynb - read in parking meter info and output useful numbers
* population.ipynb - read in census population data and output
relevant info
* recheck_addresses.ipynb - use the Google Maps API to geocode addresses
  that failed the census geocoder
