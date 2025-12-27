# **Crop Yield Prediction**
Unpredictable climate conditions have significantly affected agricultural productivity, contributing to global food insecurity (World Food Program USA, 2024). This project aims to identify key drivers of global crop yield and to forecast yields by accounting for weather impacts across different locations. The workflow includes descriptive analysis, correlation analysis, feature engineering, and machine learning modeling. 

**Tools, Techniques & Platforms Used**

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **Models:** Random Forest, Linear Regression, Decision Tree
- **Evaluation Metrics:** R² score ,MAE, MSE, RMSE
- **Resampling Technique:** Bootstrap

## Project Structure /method

### 1. Dataset
The datasets are sourced from the [World Bank](https://data.worldbank.org/) available on [Kaggle](https://www.kaggle.com/datasets/patelris/crop-yield-prediction-dataset/data). The dataset is provided under the **World Bank Dataset Terms of Use**.  Please refer to the [World Bank Terms](https://www.worldbank.org/en/about/legal/terms-of-use-for-datasets) for details on permitted usage.

This dataset is a compiled agricultural dataset containing historical crop yield records with environmental variables across multiple countries and years.

The attributes in the dataset are:
- **Area**: Country or region where the crop is produced
- **Item**: Type of crop (e.g., maize, wheat, rice)
- **Year**: Year of observation
- **Yield**: Crop yield measured in hectograms per hectare (hg/ha)
- **Rainfall**: Average annual rainfall (mm)
- **Pesticides**: Amount of pesticide usage (tonnes)
- **Temp**: Average annual temperature (°C)

### 2. Preprocessing
The following preprocessing steps were applied:
- Removed unnecessary metadata columns (Area Code, Domain, Element Code, etc.)
- Renamed column for better readability and understanding.
- Handled missing values by removing incomplete rows
- Data formatting
- Combined yield, rainfall, temperature, and pesticide dataframe by year and country
- Data trimming by identify the value of the 95th percentile and remove outliers
- Encoded categorical variables (country, crop type) using one-hot encoding

### 3. Data Exploration
- Data Distribution
    - Histograms and boxplots were used to analyze the distributions of crop yield, rainfall, temperature, and pesticide usage.
    - #histograms for each variable
        - Yield & Pesticide is right skewed
- Correlation Analysis
    - A correlation heatmap was used to identify relationships between numerical variables.
        - There are correlation between Area and pesticides_tonnes, followed by Area and average rainfall
        - There are correlation between Item and hg/ha_yield
- Trend Analysis
    - Time series plots were created to analyze crop yield trends across years.
        - The yield and pesticides used increases graduallly over time
- Descriptive Analysis
    - Top 10 Countries by Total Yield (log scale)

        - xxx
    - Top 20 Total Yields by Item
        - xxx

### 4. Modelling
The dataset was split into training and testing sets (80:20). The following models were evaluated:
- Linear Regression
- Decision Tree
- Random Forest

**Evaluation**
    - Tree-based models performed better than linear regression, indicating the presence of nonlinear relationships.
    - Residual Plots
        - identify the distribution and changing spread of residuals. As a good residual plot,
        - Residuals should be normally distributed, and there should be no patterns or trends
        - The result is not heteroscedasticity, meaning that the spread of residuals remains relatively constant across different levels of the fitted values.
        - #image
    - Feature Importance
        - Bootstrap resampling was applied. Feature importance values were calculated across multiple random resampled datasets


## Findings
- Model with the best performance is Random Forest , with good residual plot result presented and high accuracy (R²) as 98.13%
- Low MAD values were observed across multiple resamples, suggesting that the feature importance estimates are stable and consistent.
- Among all predictors,  rainfall demonstrated the highest mean importance, followed by temperature, indicating that these variables consistently contribute the most to crop yield predictions.
- Results highlighted that rainfall and temperature were the strongest predictors of yield, offering insights for sustainable agriculture and food security. 

## References
- *World Food Program USA*. (2024, April 29). *How Climate Change Is Causing World Hunger*.  https://wfpusa.org/news/how-climate-change-is-causing-world-hunger/