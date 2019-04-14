# ETL Project Report

A look at the health of honey bee colonies, honey production, and pesticide usage in the USA.

## Extracting Data Resources 
* [USDA](https://www.nass.usda.gov/Surveys/Guide_to_NASS_Surveys/Bee_and_Honey/) - CSV on honey bee colonies in the United States and CSV on honey production in the United States. 
* [Kaggle](https://www.kaggle.com/usgs/pesticide-use/version/1) - CSV of pesticide use in the United States via the USGS.

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

### These 2 dataframes were merged on state.


### From Resources/AgrPesticideUse_2014-2015

Clean the CVS (2015) to include information for:
```
Use of acetamiprid, clothianidin, imidacloprid, nitenpyram, nithiazine, thiacloprid and thiamethoxam in 2015
```    


## Loading Data 

* Load cleaned data into a SQL database
* The SQL database was queried to show the following:
```
* Top 5 states with the highest honey/colony yield
* Production rates for the 5 states that ended the 2015 year with the most colonies
* Pesticide rates for the 5 states that saw the highest colony loss
* Pesticide rates for the 5 states that saw the most colonies added
* olony change for the states with the greatest pesticide use
```

### Consideration in reading the data:

In reading this data, please be aware that for some states data is not published separately to avoid disclosing data for individual operations.

For the collected data on colonies: 
Alaska, Delaware, Nevada, New Hampshire, and Rhode Island were not individually reported.

For the collected data on honey production:
Alaska, Connecticut, Delaware, Maryland, Massachusetts, Nevada, New Hampshire, New Mexico, Oklahoma, and Rhode Island were not individually reported on.


## Authors
* [**Emily Tavik**](https://github.com/emilyt1985/)
* [**Erica Leon**](https://github.com/ericaleon)
* [**Ian Schuler**](https://github.com/ischuler)
