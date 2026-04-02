import os
from dotenv import load_dotenv

# 1. On charge les variables du fichier .env dans la mémoire du script
load_dotenv()

# 2. On les stocke dans des constantes Python
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 3. Test de sécurité (Le Check-point interne) smoke test pour vérifier que les clés sont bien chargées
if __name__ == "__main__":
    if all([SUPABASE_URL, SUPABASE_KEY, GEMINI_API_KEY]):
        print("✅ Le coffre-fort est ouvert : Toutes les clés sont chargées !")
        print(f"Connexion vers : {SUPABASE_URL}")
    else:
        print("❌ Erreur : Il manque une ou plusieurs clés dans le fichier .env")
        