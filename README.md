# ETL_project

A look at the health of honey bee colonies, honey production, and pesticide usage in the USA.

Data Resources include the USDA (https://www.nass.usda.gov/Surveys/Guide_to_NASS_Surveys/Bee_and_Honey/) and Kaggle (https://www.kaggle.com/kevinzmith/honey-with-neonic-pesticide).

We will need to filter data from all sources for 2015.

Source year: 2015

Merging data on state

From Resources/Bee Colonies 2015
  combine and clean CSVs (hcny_p06_t002, t013, t009, t010) to include:
  
  
    number of colonies (start)
    % colony change (+/-)

From Resournces/Honey 2015
 clean the CSV (t003)  to include:
  
  
    total production
    yield/colony(lbs)
    
From Resources/AgrPesticideUse_2014-2015
  clean the CVS (2015) to include information for:
  
  
  acetamiprid, clothianidin, imidacloprid, nitenpyram, 
  nithiazine, thiacloprid and thiamethoxam
    
