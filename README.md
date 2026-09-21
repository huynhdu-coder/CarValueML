# Project Proposal

## CarValueML: An ML-Powered Used Car Price Estimator 

## Course: Machine Learning Systems Design 


## 1. Domain Problem & Stakeholders  

The CarValue ML system is designed to address multiple problems existing in the current used car market. First, there is often a value gap between prices expected by potential buyers and those set by car dealers. Buyers are struggling to define the true price value of the car they are researching because listing prices of car dealers could be overpriced and overvalued. With the help of the CarValueML model, it will find the pattern in recent car sales prices and predict the value based on comparison to the historical data sales. 

Additionally, used car prices are affected by multi-characteristics of a car such as car model, make, mileage, fuel types, etc. Our CarValueML will weight those features when working on predictions to provide the most appropriate quote for both users and buyer in the car market. 

The key stakeholders of our CarValueML model are: 

App Users 

AI/ML Developers 

Data Analysts 

Car Buyers 

Car Sellers 

Service Providers (Azure) 

Investors 

## 2. Justification for ML Approach 

Used car prices are affected by many different factors, including the vehicle’s age, mileage, brand, model, fuel type, transmission, and overall condition. Since all of these variables influence the selling price at the same time, it is difficult to create a simple rule that can accurately estimate a vehicle’s value. 

Machine learning is a good fit for this problem because it can learn patterns from historical used car data and use those patterns to estimate the price of similar vehicles. As more vehicle data becomes available over time, the model can also be retrained so that it continues to reflect current market trends. This provides a more consistent and data-driven approach than relying only on manual pricing or personal judgment. 

Describe and justify the ML model you plan to implement. 

For this project, we plan to use Linear Regression as our baseline machine learning model because our goal is to predict a continuous value, which is the selling price of a used car. The model will use features such as the vehicle’s manufacturer, model, model year, mileage, fuel type, transmission, and other available characteristics to estimate its market price. 

We selected Linear Regression because it is simple, easy to understand, and provides a strong starting point for a price prediction problem. It also allows us to see how different vehicle characteristics affect the predicted price. If time allows, we may compare its performance with another regression model to determine whether a more advanced model provides better prediction accuracy. 

 

## 3. Value Proposition 

The used car price estimator can help make the pricing process faster, easier, and more consistent. Instead of spending a lot of time looking through different listings and trying to guess what a car should be worth, the model can use past vehicle data to give a reasonable price estimate. 

### 1. Tangible Benefits 

Reduce time spent researching prices: The model can quickly estimate a car’s value based on things like make, model, year, mileage, and condition, which saves time compared to manually comparing a bunch of listings. 

Reduce overpricing and underpricing: The estimator can help sellers avoid pricing a car way too high or too low compared to similar vehicles. 

Potentially increase sales conversion: If a car is priced more accurately, buyers may be more likely to consider it and make a purchase. 

Improve inventory turnover: For dealerships, better pricing could help cars sell faster instead of sitting on the lot for a long time. 

Support better profit margins: Sellers can use the estimate as a reference to find a price that is competitive while still allowing them to make a reasonable profit. 

 

 

 

### 2. Intangible Benefits 

Increase customer trust: Buyers may feel more comfortable with a price if it is backed by data instead of just being based on someone’s opinion. 

Improve pricing consistency: Using the same model for different vehicles can make pricing more consistent and reduce differences caused by personal judgment. 

Improve buyer and seller confidence: Buyers can feel more confident that they are getting a fair price, while sellers can feel more confident that they are not asking for too little. 

Support data-driven decision-making: The model gives users another source of information to help them make better decisions instead of relying only on guesses or a few online listings. 

 

## 4. Performance Metrics 

To measure how well the used car price estimator is working, we will look at both technical metrics and business metrics. The technical metrics will focus on how accurate and efficient the model is, while the business metrics will focus more on whether the system actually improves the vehicle pricing process. 

### 1. Technical Metrics 

R² (R-squared): Measures how much of the variation in used car prices can be explained by the model. A higher R² generally means the model is doing a better job of predicting prices based on the available vehicle features. 

MAE (Mean Absolute Error): Measures the average difference between the model's predicted price and the actual price. This is useful because it gives us an easy-to-understand dollar amount for how far off the predictions are on average. 

RMSE (Root Mean Squared Error): Measures prediction error while giving more weight to bigger mistakes. This can help identify situations where the model predicts a price that is very far from the actual value. 

MAPE (Mean Absolute Percentage Error): Measures the prediction error as a percentage of the actual vehicle price. This makes it easier to compare the model's performance across cheaper and more expensive vehicles. 

Latency: Measures how long it takes the system to generate a price prediction after the vehicle information is entered. Ideally, the prediction should be generated within a few seconds, so the system is easy and practical to use. 

 

 

 

### 2. Business Metrics 

Time saved when pricing vehicles: Compare how long it takes someone to research and price a vehicle manually versus using the ML price estimator. 

Pricing accuracy: Track how close the suggested price is to the vehicle's actual selling price or market value. 

Inventory turnover: Measure whether vehicles priced using the model sell faster and spend less time sitting in inventory. 

Sales conversion rate: Track whether vehicles priced using the estimator are more likely to sell compared to vehicles priced using the normal process. 

User adoption: Measure how often employees or users choose to use the estimator when pricing vehicles. This can help show whether the system is actually useful and easy enough to include in their normal workflow. 

## 5. Data Source & DataOps Concepts 

To enhance the ML model calculation, we are using a Used Cars Dataset from Kaggle with more than 762,000 data rows scraped from Cars.com. This dataset contains all the car characteristics that we need to train the CarValueML model, highlighted with model, year, mileage, and manufacturer. 

Once the dataset is ready, we plan to use VSCode as our working environment for our first ML Development Life Cycle. Moreover, the project will be installed with Python and relevant packages such as pandas and matplotlib for DataOps Pipeline. The following plan demonstrates our plan to incorporate Data Management. 

The Python package that we plan to use for Data Ingestion is Pandas. It is a well-known package with multifunctional capabilities for data injection, cleaning, and validation. The process will begin with downloading the CSV file from Kaggle and uploading it into our working environment. Then, we use the read_csv() method to load the dataset into a Pandas DataFrame and prepare it for the data validation process. 

To deliver a successful data validation and preprocessing process, four requirements we target are handing missing data and duplicates, ensuring correct data types, and processing invalid data values. The built-in fillna() method could be utilized to fill out any empty numeric data fields with Median number or use “unknown” for categorical features. Next, we handle duplicates by duplicated().sum() method to check the total duplicates in 762,000 rows and drop_duplicates() to clear any unwanted matching data rows. Any irrelevant data fields and data types such as negative value of mileage, $0 car, and incorrect manufacturers’ names will be modified or eliminated based on the circumstances.  

After finishing the data validation process, we will store and version our current dataset with DVC (Data Versioning Control) running on the local machine. It is a great package to migrate to our polished dataset, keep track of the changes, and allow different data versions to be stored and retrieved for future calculations and comparisons. 

 

 

 

## 6. Design Principles 

To guide the development of CarValueML, our project will follow three machine learning system design principles discussed in Chapter 1: Modularity & Abstraction, Reproducibility, and Monitoring & Maintenance. 

 

### Modularity & Abstraction 

We plan to organize the project into separate components, including data collection, data cleaning, model training, model evaluation, and price prediction. Keeping these tasks separate makes the project easier to develop, test, and update. For example, if we improve the data cleaning process later, we can do so without changing the rest of the system. 

### Reproducibility 

Reproducibility means that the same results can be recreated using the same data, code, and settings. We plan to use GitHub for version control and DVC (Data Version Control) to keep track of different versions of our dataset as it is cleaned and prepared. This will help our team collaborate more effectively and make it easier to repeat experiments or compare future improvements. 

### Monitoring & Maintenance 

Although our project is a prototype, we want it to be easy to maintain as new data becomes available. We will evaluate our model using metrics such as R², MAE, and RMSE to measure its performance. If newer used car data is collected in the future, the model can be retrained to improve its accuracy and better reflect changes in the used car market. 

 
