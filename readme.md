# Data Cleaning Project: Population Dataset

## 1. Initial State Analysis 

### Dataset Overview
- **Name**: messy_population_data.csv
- **Rows**: 125,718
- **Columns**: 5

### Column Details

| Column Name     | Data Type | Non-Null Count | Unique Values | Mean           |
|-----------------|-----------|----------------|---------------|----------------|
| income_groups   | object    | 119,412        | 8             | N/A            |
| age             | float     | 119,495        | 101           | 50.001         |
| gender          | float     | 119,811        | 3             | N/A            |
| year            | object    | 125,718        | 170           | N/A            |
| population      | object    | 125,718        | 114926        | 1.579          |

### Identified Issues

1. **Missing Values**
   - Description: There are missing values as NaN
   - Affected Column(s): income groups (6306), age (6223), gender (5907)
   - Example: Row 6306 has NaN in income_groups, Row 6223 has a NaN in age
   - Potential Impact: If left uncleaned they can affect our conclusions because it can result in a skew 

2. **Duplicates**
   - Description: there are 2950 duplicate rows
   - Affected Column(s): All columns 
   - Potential impact: duplicate rows may over represent which can affect our conclusions thus they need to be removed

3. **Data Types**
   - Description: Some of the data types are incorrect 
   - Affected Column(s): All columns
   - Example: Age is a float but should ideally be integer, and gender is a float which should ideally be catgeorical and year is an object but should be integer and population is object and should be integer
   - Potential Impact: If left uncleaned they can affect our conclusions because it can result in a skew 

4. **Inconsistent Values**
   - Description: There are typos and unexpected values
   - Affected Column(s): income_groups and gender
   - Example: Income_groups has typose like upper_middle_income_typo and gender column has values like 3.0
   - Potential Impact: If left uncleaned they can lead to unclear data


## 2. Data Cleaning Process

### Issue 1: Missing Values
- **Cleaning Method**: Handle missing values by either filling them with mean or removing rows
- **Implementation**:
    ```python
    df_cleaned = df_messy.dropna(subset=['income_groups', 'age', 'gender'])
    df_cleaned['age'].fillna(df_cleaned['age'].mean(), inplace=True)
    ```
- **Justification**: Filling missing values in `age` with the mean ensures that we don’t lose too much data
- **Impact**:
    - **Rows affected**: [Number of rows removed or filled]
    - **Data distribution change**: Minimal change in distribution as filling is done with mean values.


### Issue 2: Duplicated Rows

- **Cleaning Method**: use the `drop_duplicates()` function to remove all duplicated rows in the dataset
- **Implementation**:
```python
df_messy_cleaned = df_messy.drop_duplicates()

-**Justification**: Duplicates need to be removed because they are not necessary and only will skew the data and lead to misleading conclusions. 
-**Impact**: Duplicated rows can skew analysis by over-representing certain data points. All the means of the columns will also be innaccurate. 
