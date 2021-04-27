# Health Data Analysis

Since Februrary 2020, I have collected data from my Apple Watch (tracking cardio workouts, heart rate, steps), the Apple Health App (tracking blood pressure, weight), MyFitnessPal (tracking caloric, macronutrient, and micronutrient intake), Strong (tracking lifting progression). I am curious to analyze this data to understand patterns that will help me reach my fitness goals.

The pipeline includes the following:
1. Extract, transform, load, and merge the data from the different sources. [This](ETL.html) notebook includes the ETL process.
2. Process and engineer features. Some features are dropped for redunancy, while others are added based on linear combinations of other predictors. Refer to [this](FeatureEngineering.html) notebook.
3. Analyze the data and construct models to answer research questions. In [this](Research and EDA.html) notebook, I primarily seek to study my body fat levels, maintenance calories, and whether tracking calories or macronutrients is a better approach to healthy nutrition.

Presentation Link: https://youtu.be/3UXps8PyMAo
