# Telco_Project
## Churn Predictors
### Goals:
>	To create a classification model that can accurately identify the customers probability to churn using the TELCO data. 
>To attain this goal, I will be identifying the drivers of the churn and create a model that will incorporate these drivers(variables)
>to accurately predict the customer’s likelihood to churn. 

### Data Dictionary:
>customer_id:  unique identifier for each customer

>senior_citizen: 1 to indicate the customer is a senior citizen, 0 to indicate they are not

>partner: 1 to indicate they have partners, 0 to indicate they don’t have partners

>dependents: 1 to indicate they have dependents, 0 to indicate they don’t have partners

>tenure: length customer has been with the company in months

>phone_service: 1 to indicate they have phone service, 0 to indicate they don’t have phone service

>multiple_lines: 1 to indicate they have multiple lines, 0 to indicate that they don’t

>online_security: 1 to indicate if the customers opted in for online security service, 0 to indicate they havent

>device_protection:

>tech_support:

>streaming_movies:

>paperless_billing:

>monthly_charges:

>total_charges:

>churn:

>partner_dependents:

>phone_and_multiple_lines:

>streaming_tv_movie:

>online_security_and_backup:

>payment_auto:

>payment_not_auto:

>month-to-month:

>one year:

>two year:

>DSL:

>fiber optic:

>no_internet:


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



