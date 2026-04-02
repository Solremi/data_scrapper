import os
import json
import google.generativeai as genai
from models import JobOffer
from dotenv import load_dotenv

load_dotenv()

# Configuration de l'API avec la clé dans le .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def extract_job_data(raw_text: str, url: str) -> JobOffer:
    """Prend le texte brut du scraper et le transforme en objet JobOffer propre."""
    
    # Le Prompt : On donne des consignes ultra-strictes à l'IA
    prompt = f"""
    Tu es un expert en recrutement Data Engineering. 
    Analyse le texte de l'offre d'emploi ci-dessous et extrais les informations demandées.
    
    Réponds UNIQUEMENT au format JSON avec cette structure exacte :
    {{
        "title": "Intitulé du poste",
        "company": "Nom de l'entreprise",
        "location": "Ville, Pays ou Remote",
        "salary_range": "Le salaire (ex: 45k-55k) ou 'Non spécifié'",
        "stack_tech": ["Liste", "des", "technos", "clés"],
        "remote_policy": "Full Remote, Hybride ou Présentiel"
    }}

    Texte de l'annonce :
    {raw_text}
    """

    try:
        # Appel à l'API
        response = model.generate_content(prompt)
        
        # Nettoyage de la réponse au cas où l'IA ajoute des balises ```json
        cleaned_response = response.text.strip().replace('```json', '').replace('```', '')
        
        # On transforme le texte JSON en dictionnaire Python
        data_dict = json.loads(cleaned_response)
        
        # On ajoute l'URL (car elle n'est pas forcément dans le texte brut)
        data_dict["url"] = url
        
        # --- LA MAGIE PYDANTIC ---
        # On crée l'objet. Si les données ne respectent pas model.py, ça lève une erreur ici.
        return JobOffer(**data_dict)

    except Exception as e:
        print(f"❌ Erreur lors de la transformation IA : {e}")
        return None
    
if __name__ == "__main__":
faux_texte = "Nous cherchons un Data Engineer chez Google à Paris. Stack: Python, SQL. Salaire 60k. Télétravail possible 2 jours par semaine."
url_test = "[https://google.com/jobs/1](https://google.com/jobs/1)"

resultat = extract_job_data(faux_texte, url_test)

if resultat:
    print("✅ Gemini a compris l'annonce !")
    print(resultat.model_dump_json(indent=2))

