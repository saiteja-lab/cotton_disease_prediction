
import requests

API_URL = "http://localhost:11434/api/generate"

def get_disease_recommendation(disease_name, percentage_infected):

    if disease_name == "Healthy":
        return "No disease detected. Maintain regular plant care."
    
    prompt = f"Provide a cure recommendation for {disease_name} in cotton farming."

    payload = {
        "model": "cotton",  # Use your model name
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "").strip() 
    
     # Return only the recommendation text
    
    else:
        return f"Error: {response.text}"  
    
    # Return error message if request fails

# print(get_disease_recommendation("Aphides",30))