import google.generativeai as genai
import os 
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")

def optimize_bullet(bullet):
    #Configurer l'API avec la clé d'API
    genai.configure(api_key=api_key)
    #Créer une instance du modèle génératif
    model = genai.GenerativeModel("gemini-3.8-flash")
    #Generer une version optimisée du bullet point
    response = model.generate_content("You are a professional resume writer. Improve the following resume bullet point to make it more impactful and quantifiable. Use strong action verbs. Return ONLY the improved bullet point, nothing else, no explanation. Bullet point: " + bullet)
    #Retourner le texte de la réponse
    return response.text
