# scripts/load/load_data.py
import pandas as pd

def load_data(file_path):
    """
    Charge un fichier CSV ou Excel et retourne un DataFrame pandas.
    """
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Format de fichier non supporté. Utilisez CSV ou Excel.")
        print(f"✅ Fichier chargé : {file_path}")
        return df
    except Exception as e:
        print(f"❌ Erreur lors du chargement du fichier : {e}")
        return None
