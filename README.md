# Django-DiabetesPrediction

# Django
Django is a high-level open-source Python web framework that allows developers to create complex web applications quickly and efficiently. It follows the Model-View-Controller (MVC) architectural pattern and provides a robust set of tools and libraries for tasks such as handling HTTP requests and responses, database modeling, user authentication, and form handling. This project utilizes the MVC framework, where the graphical user interface is created using HTML and CSS.

Five models have been created to store the data required for analysis and statistics, as well as the data input by the user in the questionnaire. The data in the models can be updated or deleted using views, which act as intermediaries that connect the data tables in the models to the HTML templates. Machine learning algorithms and statistical analyses are executed on request using the views, and the results are then submitted to the HTML templates for display.
# Data and Python Machine learning Model
The NHANES dataset for years 2011-2014 was utilized in this study. It contains a range of health-related variables, including demographic features, as well as health measures. The dataset was pre-processed to eliminate any missing values. Using scikit-learn library in python, a feature selection and machine learning algorithm were built for the prediction. Dimensional reduction was performed on the data using recursive feature elimination (RFE) function in the model selection tool. The elimination was done using a Decision tree estimator, resulting in the selection of the most significant features with respect to the condition. Decision Tree Classifier was used to train the model with BMI, weight, cholesterol and Triglycerides levels, physical activity to predict the stage of diabetes. Data distribution visualizations were conducted to examine the variation of data between pre-diabetic and diabetic conditions, while the Pearson correlation coefficient test was utilized to analyze the correlation between features.
# Hypertext Markup language (HTML)
HTML is a language that relies on tags to format and update data on a website. When combined with Cascading Style Sheets (CSS), the visual appearance of a website can be improved. Our website was built using HTML. We created an interactive dashboard with visualizations using highcharts10 scripts for pie charts, maps, and scatter plots. These visualizations show the distribution of diabetes and its aspects.

# SQL connector
MySQL Connector is a popular Python driver used for MySQL databases. It enables developers to execute various database operations and is frequently used in web development and data analysis projects. For our project, we used MySQL Connector to connect the SQL database to Django and import data into models, which are essentially the tables in the SQL database.
