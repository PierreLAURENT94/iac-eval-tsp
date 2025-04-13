import csv
import json

results = [
    {
        "file_name": "evaluation-dataset-for-data_phi4_en.csv",
        "llm": "Phi-4 (14B)",
        "variante": "en"
    },
    {
        "file_name": "evaluation-dataset-for-data_phi4_short.csv",
        "llm": "Phi-4 (14B)",
        "variante": "short"
    },
    {
        "file_name": "evaluation-dataset-for-data_phi4_fr.csv",
        "llm": "Phi-4 (14B)",
        "variante": "fr"
    },
    {
        "file_name": "evaluation-dataset-for-data_deepseek-r1_en.csv",
        "llm": "DeepSeek-R1 (7B)",
        "variante": "en"
    },
    {
        "file_name": "evaluation-dataset-for-data_deepseek-r1_short.csv",
        "llm": "DeepSeek-R1 (7B)",
        "variante": "short"
    },
    {
        "file_name": "evaluation-dataset-for-data_deepseek-r1_fr.csv",
        "llm": "DeepSeek-R1 (7B)",
        "variante": "fr"
    },
]

# Ce qui va contenir toutes les données
all_data = []

for res in results:
    with open(res["file_name"], newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            entry = {
                "llm": res["llm"],
                "difficulty": row["Difficulty"],
                "variant": res["variante"],
                "correct": row["LLM Correct? #0"].strip().lower() == "true"
            }
            all_data.append(entry)

# Écriture du fichier JSON
with open('benchmark_results.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, indent=2, ensure_ascii=False)
