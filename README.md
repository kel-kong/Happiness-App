# Happiness-App
## About This Project
This project uses the World Happiness Reports for the years 2015 - 2019, to create an app using the platform Streamlit. The app allows the user to choose a starting year, ending year, and area (country or region). Using the slider, the user can choose their starting and ending year. Next, the user would then be prompted to choose their area type of either country or region. They can then select which country/region they'd like using the dropdown menu displayed.

If country is selected, the results would be the Rank Difference for that selected country between the two year selected. In contrast, if region is selected, the results would display the average Rank Difference of countries within the selected region. 

To further dive into the data, a dataset will be displayed showing the Country, Rank Difference, Happiness Score Difference, Economic Difference, Health Difference, Freedom Difference, and lastly Governmental Difference for the selected years. To help the user visualize these differences, there will be an interactive graph shown that will plot the scores for each category for those two years. To select one category you click on the coloor-coordinated tiles on the left legend, and to select multiple you hold shift while selecting the wanted categories. 


## Built With
- Python ; Altair, SQL
- MySQL, MySQL WorkBench, Streamlit

## Content of this Repo
Happiness.ipynb
- this is a notebook containing the code that would imitate the app's functions (happiness.py)

README.md
- what you are currently reading that details the whole projects

happiness.py 
- this .py file is what is used to create the interface of the app through Streamlit

requirements.txt, secrets.toml
- extra files needed to connect MySQL

## Pre-Process: 
I will now be going into the process and challenges that I encountered while working on this project.

In order to download MySQL I had to use a community download since I do not have a Windows machine. Through this community download, I watched a Youtube tutorial and followed the additional needed steps of adding a bash profile. After that, I examined the dataset and from the hint given, I noticed that each year had different columns and column names. I found the columns that all the years ('15-'19) had in common, which were: Country, Happiness Rank, Happiness Score, Economy (GDP), Health (life expectancy), Freedom, and Government and changed their names to make it easier to work with. Next, when working with region, I realized that the years 2017-2019 did no have a regions column. Because 2015 had the most amount of countries, I used the year 2015 as a key for mapping regions to countries.

I used the following query to get the country/region key:
"SELECT DISTINCT Country, Region FROM `happiness`.`2015` ORDER BY `Country` ASC"

I then downloaded the .csv and uploaded the years with the missing region along with the key to map it. 
To do this I used VLOOKUP to create a new column, region: 
"VLOOKUP(B2, Region_Key!$A$2:$C$159, 2, 1)"

After getting a new dataset with the regions column, I uploaded that back into MySQL Workbench. From there, I was able to work on the actual parts of the app relating to the rank differences. 


## Sources 
Dataset used: 
https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2015.csv (2015 - 2019)

Video reference to download MySQL: 
https://www.youtube.com/watch?v=n1zT1OZcgnw&ab_channel=99MasterClass

Some of the websites referred to (in attempt to fix connectivity issue): 
https://jennyttt.medium.com/the-solution-to-cant-connect-to-mysql-server-on-xxxxx-2fe7d4e1d460
https://sebhastian.com/mysql-fix-secure-file-priv-error/

Video reference explaining the app and the process of making it: 
https://ucsd.zoom.us/rec/share/Bqad7N-_cvsifxnQZkLLs6POOSeYY630CRugpbZtaUnEt3w8T7n4jdIS9MjyzqfK.eDMSLI8p7Jv69_yY?startTime=1652203946000
Passcode: dM88eoJ^

