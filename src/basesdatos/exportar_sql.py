import pandas as pd
from sqlalchemy import create_engine
import urllib

server = "SERVER_NAME"   # Servidor base en DQL Server
database = "DATABASE_NAME"  # Nombre de la base de datos

# String para la conexión con el servidor
connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
)

params = urllib.parse.quote_plus(connection_string)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")


# Cargar CSVs
df_main = pd.read_csv("../../data/processed/comentarios_principales_sql.csv")
df_reply = pd.read_csv("../../data/processed/comentarios_replies_sql.csv")

# Exportar a SQL Server
df_main.to_sql(
    "comments_main",
    engine,
    if_exists="replace",
    index=False
)

df_reply.to_sql(
    "comments_reply",
    engine,
    if_exists="replace",
    index=False
)

# Mensaje de verificación al terminar de exportar
print("Datos exportados correctamente a SQL Server")
