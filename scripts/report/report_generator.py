# scripts/report/report_generator.py

def generate_report(df, eda_results, output_path):
    """
    Génère un rapport HTML simple avec les statistiques et graphiques
    """
    if df is None:
        print("❌ Pas de données à analyser")
        return
    
    html = "<html><head><title>Rapport EDA</title></head><body>"
    html += "<h1>Rapport d'Analyse Exploratoire</h1>"
    
    html += "<h2>Colonnes</h2>"
    html += "<ul>"
    for col in eda_results["columns"]:
        html += f"<li>{col}</li>"
    html += "</ul>"
    
    html += "<h2>Graphiques</h2>"
    html += '<h3>Heatmap Corrélation</h3><img src="../reports/corr_matrix.png" width="600">'
    html += '<h3>Valeurs manquantes</h3><img src="../reports/missing_values.png" width="600">'
    
    for col in df.select_dtypes(include=['float', 'int']).columns:
        html += f'<h3>Histogramme {col}</h3><img src="../reports/hist_{col}.png" width="600">'
    
    html += "</body></html>"
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"✅ Rapport généré : {output_path}")
