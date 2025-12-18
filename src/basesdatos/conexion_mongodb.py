from pymongo import MongoClient, ASCENDING

# Establecimiento de la conexión con el servidor de MongoDB
class MongoDBClient:
    def __init__(self, uri="mongodb://localhost:27017",
                 db_name="sentiment_analysis",
                 collection_name="youtube_comments"):

        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

        # Índice único para evitar duplicados
        self.collection.create_index(
            [("comment_id", ASCENDING)],
            unique=True
        )

    def insertar_comentarios(self, comments: list):
        if not comments:
            print("No hay comentarios para insertar.")
            return

        inserted = 0
        for comment in comments:
            try:
                self.collection.insert_one(comment)
                inserted += 1
            except Exception:
                # Duplicado u otro error controlado
                pass

        print(f"Comentarios insertados en MongoDB: {inserted}")

    def contar_totales(self):
        return self.collection.count_documents({})
