# ETL_project

A look at the health of honey bee colonies, honey production, and pesticide usage in the USA.

## Extracting Data Resources 
* [USDA](https://www.nass.usda.gov/Surveys/Guide_to_NASS_Surveys/Bee_and_Honey/) - Databases on honey bee colonies in the United States and honey production in the United States. 
* [Kaggle](https://www.kaggle.com/usgs/pesticide-use/version/1) - Database of pesticide use in the United States .

## Transforming Data

Data sources filtered for 2015.

Given the limited time available and inconclusive datasets for many years, we will limit the scope of this project to 2015


### From Resources/bee_colonies_2015

Combine and clean CSVs (hcny_p06_t002, t013, t009, t010) to include:
```
number of colonies (start)- 2015
% colony change (+/-) - 2015
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
