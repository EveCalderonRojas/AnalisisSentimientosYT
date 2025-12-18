from pymongo import MongoClient
import pandas as pd
from pathlib import Path


# Resolver rutas del proyecto

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = RAW_DIR / "youtube_comments_raw.csv"


# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["sentiment_analysis"]
collection = db["youtube_comments"]


# Extraer datos de MongoDB
print("Extrayendo datos desde MongoDB")
data = list(collection.find({}, {"_id": 0}))  # Excluimos _id

df = pd.DataFrame(data)


# Guardar CSV
df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

print(f"Archivo CSV generado correctamente en:\n{OUTPUT_FILE}")
print(f"Total de registros exportados: {len(df)}")
