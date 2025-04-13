import pandas as pd
from tqdm import tqdm
from llm import to_french, to_short
import os

# Importer le fichier CSV dans un DataFrame

file_path = "data.csv"
df = pd.read_csv(file_path)

# Statistiques sur le DataFrame

nb_difficulty_1 = df[df["Difficulty"] == 1].shape[0]
print(f"[INFO] Nombre de défis avec une difficulté de 1 : {nb_difficulty_1}")

nb_difficulty_2 = df[df["Difficulty"] == 2].shape[0]
print(f"[INFO] Nombre de défis avec une difficulté de 2 : {nb_difficulty_2}")

nb_difficulty_1et2 = nb_difficulty_1 + nb_difficulty_2
print(f"[INFO] Nombre de défis avec une difficulté de 1 et 2 : {nb_difficulty_1et2}")

total_rows = df.shape[0]
print(f"[INFO] Nombre total de défis : {total_rows}")

# Choix de l'utilisateur pour le mode de génération

print("Choisissez une option :")
print("1 - Générer le dataset EN")
print("2 - Générer le dataset FR")
print("3 - Générer le dataset Short")
choice = input("Entrez votre choix (1, 2 ou 3) : ")

if choice not in ["1", "2", "3"]:
    print("Choix invalide. Veuillez relancer le script et entrer 1, 2 ou 3.")
    exit()

match choice:
    case "1":
        mode = "en"
    case "2":
        mode = "fr"
    case "3":
        mode = "short"
    case _:
        print("Choix invalide. Veuillez relancer le script et entrer 1, 2 ou 3.")
        exit()

# Filtrer uniquement les lignes avec une difficulté de 1 ou 2
filtered_df = df[df["Difficulty"] <= 2]

# Boucler sur les indices filtrés
for index in tqdm(filtered_df.index, total=filtered_df.shape[0], desc="Progression"):
    # Vérifier si le prompt est valide
    if pd.notna(filtered_df.loc[index, "Prompt"]):
        match mode:
            case "en":
                # pas de traitement nécessaire
                pass
            case "fr":
                print(f"\n\nSource : {filtered_df.loc[index, 'Prompt']}")
                filtered_df.loc[index, "Prompt"] = to_french(filtered_df.loc[index, "Prompt"])
                print(f"Traduction : {filtered_df.loc[index, 'Prompt']}")
            case "short":
                print(f"\n\nSource : {filtered_df.loc[index, 'Prompt']}")
                filtered_df.loc[index, "Prompt"] = to_short(filtered_df.loc[index, "Prompt"])
                print(f"Version courte : {filtered_df.loc[index, 'Prompt']}")

# Sauvegarder le fichier filtré
nom_fichier = "_" + mode + "-niv1et2.csv"
os.makedirs("out", exist_ok=True)

filtered_df.to_csv("out/data" + nom_fichier, index=False, encoding="utf-8")

# Sauvegarder une version rapide du fichier pour test
filtered_df_copy = filtered_df.head(2)
filtered_df_copy.to_csv("out/data-quick-test" + nom_fichier, index=False, encoding="utf-8")