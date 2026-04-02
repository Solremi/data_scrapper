import httpx
from bs4 import BeautifulSoup

def fetch_page_content(url: str) -> str:
    """Récupère le contenu d'une page sans avoir besoin de navigateur lourd."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        print(f"🌐 Appel (léger) vers : {url}...")
        # On fait une requête HTTP classique
        response = httpx.get(url, headers=headers, follow_redirects=True) #permet de suivre les redirections et d'arriver à la page finale
        response.raise_for_status() # Vérifie que la requête a réussi (code 200) sinon go except 
        
        # On utilise BeautifulSoup pour extraire uniquement le texte
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # On supprime les balises inutiles (scripts, styles)
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()
            
        return soup.get_text(separator=' ', strip=True) # On récupère le texte brut, en séparant les éléments par des espaces et en supprimant les espaces superflus
        
    except Exception as e:
        print(f"❌ Erreur de récupération : {e}")
        return ""

if __name__ == "__main__":
    # Test avec une URL simple (ex: une page de blog ou une annonce)
    test_url = "https://www.google.com" 
    content = fetch_page_content(test_url)
    print(f"✅ Succès ! Extrait : {content[:200]}...")
