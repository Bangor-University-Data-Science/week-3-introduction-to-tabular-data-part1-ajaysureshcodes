import pandas as pd
def create_summary_table(df):
    summary = {
        'Feature Name': df.columns,
        'Data Type': df.dtypes.values,
        'Number of Unique Values': df.nunique().values,
        'Has Missing Values?': df.isnull().any().values
    } 
    summary_data = pd.DataFrame(summary)
    return summary_data
