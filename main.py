from api.youtube_comments import extraer_comentarios
from basesdatos.conexion_mongodb import MongoDBClient

VIDEO_ID = "9flte56erE8"

def main():
    print("Extrayendo comentarios desde YouTube...")
    comments = extraer_comentarios(VIDEO_ID)
    print(f"Comentarios extraídos: {len(comments)}")

    print("Conectando a MongoDB...")
    mongo = MongoDBClient()

    print("Insertando comentarios en MongoDB...")
    mongo.insertar_comentarios(comments)

    print(f"Total de documentos en MongoDB: {mongo.contar_totales()}")

if __name__ == "__main__":
    main()
