# Telco_Project
## Churn Predictors
### Goals:
>	To create a classification model that can accurately identify the customers as someone that will churn or not  using the TELCO data. 
>To attain this goal, I will be identifying the drivers of the churn and create a model that will incorporate these drivers(variables)
>to accurately predict the customer’s likelihood to churn. 

### Data Dictionary:
> - **customer_id:**  unique identifier for each customer

> - **senior_citizen:** (int) 1 indicates the customer is a senior citizen, 0 indicates they are not

> - **partner:** (int) 1 indicates they have partners, 0 indicates they don’t have partners

> - **dependents:** (int) 1 indicates they have dependents, 0 indicates they don’t have dependents

> - **tenure:** (int) length customer has been with the company in months

> - **phone_service:** (int) 1 indicates they have phone service, 0 indicates they don’t have phone service

> - **multiple_lines:** (int) 1 indicates they have multiple lines, 0 indicates that they don’t

> - **online_security:** (int) 1 indicates customers opted in for online security service, 0  indicates they havent

> - **device_protection:** (int) 1 indicates customers have device protection, 0 indicates they dont

> - **tech_support:** (int) 1 indicates customers have tech support, 0 indicates they dont

> - **streaming_movies:** (int) 1 indicates customers have streaming movie service, 0 indicates they dont

> - **paperless_billing:** (int) 1 indicates customers have enrolled in paperless billing, 0 indicates they havent

> - **monthly_charges:** (int) monthly charge of a customer

> - **total_charges:** (float) total charges customers have paid

> - **churn:** (int) 1 to represent customers that have churned, 0 represent they havent

> - **partner_dependents:** (bool) to represent if customers have both partner and dependents

> - **phone_and_multiple_lines:** (bool) to represent if customers have both phone and multiple lines

> - **streaming_tv_movie:** (bool) to represent if customers have both streaming tv and movie

> - **online_security_and_backup:** (bool) to represent if customers have both online security and back up

> - **payment_auto:** (int) 1 indicates customers have automatic payment, 0 indicates they have not

> - **month-to-month:** (int) 1 indicates customers are with month to month, 0 indicates they have other form of contract

> - **one year:** (int) 1 indicates customers are with one year, 0 indicates they have other form of contract

> - **two year:** (int) 1 indicates customers are with two year, 0 indicates they have other form of contract

> - **DSL:** (int) 1 indicates customers have DSL, 0 indicates they have other form of internet

> - **fiber optic:** (int) 1 indicates customers have fiber optic, 0 indicates they have other form of internet



### Project Planning

#### Data Acqusition:
> -	Acquire data from CodeUp database. You are required to have credentials to access the data base.
> - Create a cache in your local repository in order to prevent from having to access the database every time you re-work on the project
> - Create **acquire.py** for reproducibility.

#### Data Preparation:
> - Summarize data
> - Check for duplicates, removed duplicates if present
> - Check for null values, missing values, and get count of them
> - Check the data types
> - Perform feature engineering
> - Perform data types conversion/Use Dummy variables
> - Drop redundant/useless columns
> - Split data into Train, Test, and Validate
> - Create **prepare.py**

#### Data Exploration:
> - Explore various features and relationships
> - Vizualize data
> - Impute missing values
> - Test different hypothesis

#### Model Building
> - Try various algorithms(Logit, Random Forest, KNN, Decision Tess) on Train data
> - Perform model evaluation
> - Pick top 3 perfomring models
> - Validate top 3 models on validate data and evaluate their performance
> - Pick best performing model on validate data
> - Use the top model with test data set and evaluate your model

#### Conclusion
> - Summarize the process
> - Summarize findings
> - Make recommendations
> - Road Ahead?



