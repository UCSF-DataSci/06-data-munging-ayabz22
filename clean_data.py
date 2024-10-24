 z_scores_age = np.abs(stats.zscore(df_messy_cleaned['age'].dropna()))
    df_clean_age = df_messy_cleaned[z_scores_age < 3]
    print(f"Number of rows after removing outliers in 'age': {df_clean_age.shape[0]}")