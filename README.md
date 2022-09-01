# KC-house-dataset-Machine-Learning


The objective of this kernel is to create a linear regression model for a given dataset( House Sales in King County, USA). The overall idea of regression is to examine two things: (1) does a set of predictor variables do a good job in predicting an outcome (dependent) variable? (2) Which variables in particular are significant predictors of the outcome variable, and in what way do they–indicated by the magnitude and sign of the beta estimates–impact the outcome variable? These regression estimates are used to explain the relationship between one dependent variable and one or more independent variables.

Linear Regression Analysis consists of more than just fitting a linear line through a cloud of data points. It consists of 3 stages – (1) analyzing the correlation and directionality of the data, (2) estimating the model, i.e., fitting the line, and (3) evaluating the validity and usefulness of the model.

(1) First import the file, perform data preprocessing(removing null values, changing data type, etc) and then perform EDA(Exploratory Data Analysis) for the data. Find if there are any correlations between the data.

(2) Now we create a base model ABC, create required abstract classes. Create linearmodel class which is sub class of ABC class. Define the required methods. We are performing least squares and least mean sqaures for the given dataset. The least squares is perfect for smaller datasets, it is not normalized where as least mean squares is perfect for large datasets, we normalize the data for reducing the skewness of the data. We plot graphs for the line and see if it fits correctly for the data or not. The preliminary tests shows that we obtained both least squares and least mean squares correctly.


(3) In order to know that the created model is valid, we create plots to see the predicted line and the points where the required value should be vaild. We know that the model is valid and is useful when it passes the preliminary test, where the least mean square and least squares are verified with various data.

(4) Square feet of living has the highest R^2 and coefficient of determination 
    Square feet of lving has the least RMSE value 
