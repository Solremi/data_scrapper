# data_scrapper + IA + BDD
ETL

instal: 
- dotenv (variable d'environnement)
- .venv (pour contenir)
- pydantic ( force a respecter le typage)

configurer le .env 
configurer le .gitignore

## EXTRACT (python script)
Création de config.py
- utiliser le contenu du .env

Creation de models.py
- paramétrer la récupération du data scraping

Création de scraper.py
- utilisation de BS4 pour parser - nettoyer le bruit du web
- mettre un user-agent en header pour ne pas dire que c'est un scrypt python
- une fonction pour supprimer les résidus html inutiles dans les balises script et style

## TRANSFORM (IA)
- install google-generativeai via pip
- création de processor.py 


## LOAD (supabase)