import os
from openai import OpenAI

# Initierar klienten (hämtar automatiskt nyckeln från miljövariabler)
client = OpenAI()

def analyze_seo_content(text_content):
    """
    Skickar text till en AI-modell för att analysera on-page SEO 
    och generera optimerade metataggar.
    """
    print("Analyserar innehåll och genererar SEO-förslag...")

    prompt = f"""
    Du är en expert inom teknisk SEO och content-optimering. 
    Analysera följande text och ge förslag på:
    1. En optimerad Title-tagg (max 60 tecken).
    2. En säljande Meta Description (max 160 tecken).
    3. 3 korta förbättringspunkter för struktur och sökordsoptimering.

    Text att analysera:
    {text_content}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Du är en professionell SEO-specialist."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        
        return response.choices[0].message.content

    except Exception as e:
        return f"Ett fel uppstod vid anropet till AI-tjänsten: {e}"

if __name__ == "__main__":
    sample_text = """
    Här är en exempeltext om att köpa hästlastbil. Att välja rätt hästlastbil 
    är viktigt för både din och hästens säkerhet under transporten. 
    Det finns olika modeller beroende på B- eller C-körkort.
    """

    result = analyze_seo_content(sample_text)
    print("\n--- SEO-RESULTAT ---")
    print(result)
