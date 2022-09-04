# KC-house-dataset-Machine-Learning

This exercise is based on a dataset on house sales in King County, USA. The dataset is taken
from Kaggle – https://www.kaggle.com/harlfoxem/housesalesprediction.

Linear Regression Analysis consists of more than just fitting a linear line through a cloud of data points. It consists of 3 stages – (1) analyzing the correlation and directionality of the data, (2) estimating the model, i.e., fitting the line, and (3) evaluating the validity and usefulness of the model.

1. First import the file, perform data preprocessing(removing null values, changing data type, etc) and then perform EDA(Exploratory Data Analysis) for the data. Find if there are any correlations between the data.

2. Now we create a base model ABC, create required abstract classes. Create linearmodel class which is sub class of ABC class. Define the required methods. We are performing least squares and least mean sqaures for the given dataset. The least squares is perfect for smaller datasets, it is not normalized where as least mean squares is perfect for large datasets, we normalize the data for reducing the skewness of the data. We plot graphs for the line and see if it fits correctly for the data or not. The preliminary tests shows that we obtained both least squares and least mean squares correctly.

3. In order to know that the created model is valid, we create plots to see the predicted line and the points where the required value should be vaild. We know that the model is valid and is useful when it passes the preliminary test, where the least mean square and least squares are verified with various data.


### Data
In this dataset we have to predict the sales price of houses in King County, Seattle. It includes homes sold between May 2014 and May 2015. Before doing anything we should first know about the dataset what it contains what are its features and what is the structure of data.

The dataset consists of 21,613 observations of recently transacted properties, and contains the
following seventeen variables:

1. id :- It is the unique numeric number assigned to each house being sold.
2. date :- It is the date on which the house was sold out.
3. price:- It is the price of house which we have to predict so this is our target variable and aprat from it are our features.
4. bedrooms :- It determines number of bedrooms in a house.
5. bathrooms :- It determines number of bathrooms in a bedroom of a house.
6. sqft_living :- It is the measurement variable which determines the measurement of house in square foot.
7. sqft_lot : It is also the measurement variable which determines square foot of the lot.
6. floors: It determines total floors means levels of house.
7. waterfront : This feature determines whether a house has a view to waterfront 0 means no 1 means yes.
8. view : This feature determines whether a house has been viewed or not 0 means no 1 means yes.
9. condition : It determines the overall condition of a house on a scale of 1 to 5.
10. grade : It determines the overall grade given to the housing unit, based on King County grading system on a scale of 1 to 11
11. sqft_above : It determines square footage of house apart from basement.
12. sqft_basement : It determines square footage of the basement of the house.
13. yr_built : It detrmines the date of building of the house.
14. yr_renovated : It detrmines year of renovation of house.
15. zipcode : It determines the zipcode of the location of the house.

### Result

By observing the data, we can know that the price is dependent on various features like bedrooms(which is most dependent feature), bathrooms, sqft_living(second most important feature), sqft_lot, floors etc. The price is also dependent on the location of the house where it is present. The other features like waterfront, view are less dependent on the price. Of all the records, there are no missing values, which helps us creating better model.

1. Square feet of living has the highest R^2 and coefficient of determination 
2. Square feet of living has the least RMSE value 
