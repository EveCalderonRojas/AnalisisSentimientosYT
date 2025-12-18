import pandas as pd


# Cargar dataset procesado
df = pd.read_csv("../../data/processed/analisis_procesado.csv")


# Separar comentarios principales y replies
df_principal = df[df["is_reply"] == False].copy()
df_reply = df[df["is_reply"] == True].copy()


# Procesar IDs de replies
# comment_id = parent.reply
df_reply["parent_id"] = df_reply["comment_id"].apply(lambda x: x.split(".")[0])
df_reply["reply_id"] = df_reply["comment_id"].apply(lambda x: x.split(".")[1])


# Selección de columnas para SQL
cols_principal = [
    "comment_id",
    "video_id",
    "author",
    "text_translated",
    "likes",
    "published_at",
    "sentiment_score",
    "sentiment_label",
    "tema"
]

cols_reply = [
    "reply_id",
    "parent_id",
    "video_id",
    "author",
    "text_translated",
    "likes",
    "published_at",
    "sentiment_score",
    "sentiment_label",
    "tema"
]

df_principal = df_principal[cols_principal]
df_reply = df_reply[cols_reply]

# Guardar datasets listos para SQL
df_principal.to_csv("../../data/processed/comentarios_principales_sql.csv", index=False)
df_reply.to_csv("../../data/processed/comentarios_replies_sql.csv", index=False)

print("Datasets preparados para SQL Server:")
print(f"- Comentarios principales: {len(df_principal)}")
print(f"- Comentarios replies: {len(df_reply)}")
