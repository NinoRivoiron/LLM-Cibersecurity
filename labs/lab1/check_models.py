import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

print(f"Test avec la clé : {api_key[:5]}...")

try:
    print("\n--- Liste des modèles disponibles pour ton compte ---")
    # On récupère tout sans filtrer pour éviter les bugs
    for m in client.models.list():
        # On affiche juste le nom technique (le champ 'name' existe toujours)
        print(f"NOM: {m.name}")
        
except Exception as e:
    print(f"\n❌ Erreur critique : {e}")