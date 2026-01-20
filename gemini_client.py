import google.generativeai as genai

def init_gemini(api_key):
    genai.configure(api_key=api_key)
    models = [m for m in genai.list_models()
              if "generateContent" in m.supported_generation_methods]

    if not models:
        raise Exception("No Gemini model available")

    model_name = models[0].name
    print("Using Gemini model:", model_name)
    return genai.GenerativeModel(model_name)
