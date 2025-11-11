# scripts/eda/eda.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno
import os

def run_eda(df, reports_dir="reports"):
    """
    Analyse exploratoire automatique d'un DataFrame.
    
    Paramètres :
        df : pandas.DataFrame
        reports_dir : dossier où sauvegarder les graphiques
    
    Retour :
        dict avec informations utiles pour le rapport
    """
    if df is None:
        print("❌ DataFrame vide")
        return None

    # Créer le dossier reports s'il n'existe pas
    os.makedirs(reports_dir, exist_ok=True)

    # --- Statistiques descriptives ---
    print("🔹 Statistiques descriptives :")
    print(df.describe(include='all'))

    # --- Heatmap de corrélation uniquement sur colonnes numériques ---
    numeric_df = df.select_dtypes(include=['float', 'int'])
    if not numeric_df.empty:
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
        plt.title("Corrélation entre variables numériques")
        plt.tight_layout()
        plt.savefig(os.path.join(reports_dir, "corr_matrix.png"))
        plt.close()
        print("✅ Heatmap corrélation générée")
    else:
        print("⚠️ Pas de colonnes numériques pour la corrélation")

    # --- Valeurs manquantes ---
    plt.figure(figsize=(10, 6))
    msno.matrix(df)
    plt.title("Valeurs manquantes")
    plt.tight_layout()
    plt.savefig(os.path.join(reports_dir, "missing_values.png"))
    plt.close()
    print("✅ Matrice des valeurs manquantes générée")

    # --- Histogrammes des colonnes numériques ---
    for col in numeric_df.columns:
        plt.figure(figsize=(6, 4))
        sns.histplot(numeric_df[col], kde=True, bins=20)
        plt.title(f"Distribution de {col}")
        plt.tight_layout()
        plt.savefig(os.path.join(reports_dir, f"hist_{col}.png"))
        plt.close()
    if numeric_df.columns.any():
        print("✅ Histogrammes générés pour toutes les colonnes numériques")

    # Retour d'infos utiles pour le rapport
    return {
        "columns": df.columns.tolist(),
        "numeric_columns": numeric_df.columns.tolist(),
        "categorical_columns": df.select_dtypes(exclude=['float', 'int']).columns.tolist()
    }
