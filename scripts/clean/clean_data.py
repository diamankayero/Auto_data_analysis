# scripts/clean/clean_data.py
import pandas as pd

def clean_data(df):
    """
    Nettoie le DataFrame :
    - Supprime les doublons
    - Remplit ou signale les valeurs manquantes
    """
    if df is None:
        return None
    
    df_clean = df.drop_duplicates()
    missing = df_clean.isnull().sum()
    print("🔹 Valeurs manquantes par colonne :")
    print(missing[missing > 0])
    
    # Optionnel : remplir les NaN par la moyenne si numérique
    for col in df_clean.select_dtypes(include=['float', 'int']).columns:
        df_clean[col].fillna(df_clean[col].mean(), inplace=True)
    
    return df_clean
