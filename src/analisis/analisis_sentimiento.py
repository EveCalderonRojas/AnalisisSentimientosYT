from textblob import TextBlob


# SENTIMIENTO
def clasificar_sentimiento(texto):

    if not texto or texto.strip() == "":
        return 0.0, "neutral"

    blob = TextBlob(texto)
    polaridad = blob.sentiment.polarity

    if polaridad > 0.1:
        etiqueta = "positivo"
    elif polaridad < -0.1:
        etiqueta = "negativo"
    else:
        etiqueta = "neutral"

    return polaridad, etiqueta



# TEMAS
def detectar_tema(texto):
    texto = texto.lower()

    temas = {
        "precio": [
            "price", "cost", "expensive", "cheap", "money",
            "worth", "overpriced", "usd", "$"
        ],
        "mejoras": [
            "upgrade", "improvement", "better", "performance",
            "hardware", "specs", "fps", "power", "graphics", "add", "yahoo", "pls"
        ],
        "hype": [
            "hype", "excited", "cant wait", "love", "amazing",
            "awesome", "finally", "🔥", "😍"
        ],
        "decepcion": [
            "disappointed", "meh", "bad", "worst", "fail",
            "boring", "nothing new", "trash", "🤡", "worst", "hate"
        ],
        "opinion": [
            "agree", "disagree"
        ]
    }

    for tema, palabras in temas.items():
        for palabra in palabras:
            if palabra in texto:
                return tema

    return "otros"
