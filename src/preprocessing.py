import pandas as pd

def load_data(file_path):
    """Load the dataset from a Parquet file."""
    return pd.read_parquet(file_path)

def extract_navigation_details(df):
    """Extract navigation details from the DataFrame."""
    return pd.DataFrame(df['navigation'].tolist())

def extract_vessel_details(df):
    """Extract vessel details from the DataFrame."""
    return pd.DataFrame(df['vesselDetails'].tolist())

def preprocess_main_details(df):
    """Preprocess the main details in the DataFrame."""
    df = df[['epochMillis', 'mmsi']].copy()  # Ensure we are working with a copy
    df.loc[:, 'timestamp'] = pd.to_datetime(df['epochMillis'], unit='ms')
    return df

def calculate_lead_time(df):
    """Calculate lead time for each group of navigation codes."""
    df = df.sort_values(by=['mmsi', 'timestamp'])
    df.loc[:, 'lead_time'] = df.groupby('navCode')['timestamp'].diff().shift(-1).dt.total_seconds() / 60  # minutes
    return df

def remove_outliers(df):
    """Remove outliers based on the lead time."""
    Q1 = df['lead_time'].quantile(0.25)
    Q3 = df['lead_time'].quantile(0.75)
    IQR = Q3 - Q1

    condition = (df['lead_time'] >= (Q1 - 1.5 * IQR)) & (df['lead_time'] <= (Q3 + 1.5 * IQR))
    df = df[condition].copy()
    return df

def merge_details(df, nav_details, vessel_details):
    """Merge navigation and vessel details into the main DataFrame."""
    df = df.copy()  # Ensure we are working with a copy
    df.loc[:, 'typeName'] = vessel_details['typeName']
    df.loc[:, 'navDesc'] = nav_details['navDesc']
    df.loc[:, 'courseOverGround'] = nav_details['courseOverGround']
    df.loc[:, 'speedOverGround'] = nav_details['speedOverGround']

    df = df.dropna(subset=['lead_time'])
    return df

def preprocess_data(file_path):
    """Complete preprocessing pipeline."""
    df = load_data(file_path)
    nav_details = extract_navigation_details(df)
    vessel_details = extract_vessel_details(df)
    
    df = preprocess_main_details(df)
    df.loc[:, 'navCode'] = nav_details['navCode']
    
    df = calculate_lead_time(df)
    df = remove_outliers(df)
    df = merge_details(df, nav_details, vessel_details)
    
    return df