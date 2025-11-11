# main.py
from scripts.load.load_data import load_data
from scripts.clean.clean_data import clean_data
from scripts.eda.eda import run_eda
from scripts.report.report_generator import generate_report


def main():
    # 1️⃣ Choisir le fichier à analyser
    file_path = "data/products-100.csv"  # ← change le nom de ton fichier ici
    df = load_data(file_path)

    # 2️⃣ Nettoyer les données
    df_clean = clean_data(df)

    # 3️⃣ Analyse exploratoire
    eda_results = run_eda(df_clean)

    # 4️⃣ Génération du rapport
    output_path = "reports/rapport_final.html"
    generate_report(df_clean, eda_results, output_path)

    print("🎉 Analyse terminée ! Rapport généré dans reports/")

if __name__ == "__main__":
    main()
