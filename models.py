from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class JobOffer(BaseModel):
    """Le schéma strict que chaque offre d'emploi doit respecter."""
    title: str = Field(..., min_length=2) # l'ellipse "..." indique que ce champ est obligatoire, sans valeur par défaut, et min_length=2 
    company: str
    location: str
    salary_range: Optional[str] = "Non spécifié"
    stack_tech: List[str] = []
    remote_policy: str 
    url: str
    created_at: datetime = Field(default_factory=datetime.now)

# Test local pour vérifier que la validation fonctionne
if __name__ == "__main__":
    try:
        test = JobOffer(
            title="Data Engineer",
            company="Ma Boîte",
            location="Paris",
            remote_policy="Remote",
            url="https://test.com"
        )
        print("✅ Pydantic est bien installé et le modèle est valide !")
    except Exception as e:
        print(f"❌ Erreur : {e}")