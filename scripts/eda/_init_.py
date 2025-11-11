# scripts/eda/eda.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno

def run_eda(df):
    """
    Analyse exploratoire automatique :
    - Statistiques descriptives
    - Visualisation des distributions et corrélations
    """
    if df is None:
        return None
    
    print("🔹 Statistiques descriptives :")
    print(df.describe(include='all'))
    
    # Heatmap de corrélation
    plt.figure(figsize=(10,8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title("Corrélation entre variables")
    plt.savefig("reports/corr_matrix.png")
    plt.close()
    
    # Visualisation des valeurs manquantes
    msno.matrix(df)
    plt.savefig("reports/missing_values.png")
    plt.close()
    
    # Histogrammes pour toutes les colonnes numériques
    for col in df.select_dtypes(include=['float', 'int']).columns:
        plt.figure()
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribution de {col}")
        plt.savefig(f"reports/hist_{col}.png")
        plt.close()
    
    return {"columns": df.columns.tolist()}
