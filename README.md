# ETL Project

A look at the health of honey bee colonies, honey production, and pesticide usage in the USA.

## Extracting Data Resources 
* [USDA](https://www.nass.usda.gov/Surveys/Guide_to_NASS_Surveys/Bee_and_Honey/) - CSV on honey bee colonies in the United States and CSV on honey production in the United States. 
* [Kaggle](https://www.kaggle.com/usgs/pesticide-use/version/1) - CSV of pesticide use in the United States .

## Transforming Data

### Data sources filtered for 2015

Given the limited time available and inconclusive datasets for many years, we will limit the scope of this project to 2015


### From Resources/bee_colonies_2015

Combine and clean CSVs (hcny_p01_t005, p02_t001, p03_t007, p04_t008) and export to one CSV with:
```
State
January 2015 colony count
December 2015 colony count
Change in colony count
Added colonies 2015
Lost colonies 2015
Renovated colonies 2015
```


### From Resournces/honey_2015

Clean the CSV (t003) to include:
```
total production - 2015
yield/colony(lbs) - 2015
```


### From Resources/AgrPesticideUse_2014-2015

Clean the CVS (2015) to include information for:
```
Use of acetamiprid, clothianidin, imidacloprid, nitenpyram, nithiazine, thiacloprid and thiamethoxam in 2015
```    

## Loading Data 

* Load cleaned data into a sqlite database
* Create a flask app to query the database for information on individual states 
* Create a flask app to query comparisons between 2 states
