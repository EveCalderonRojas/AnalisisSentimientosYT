from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from tqdm import tqdm
import emoji
import time


# CONFIGURACIÓN
API_KEY = "AIzaSyC_XnAhIySqjsA8CZVaUkjr9drecE0iPjU"
VIDEO_ID = "9flte56erE8"

youtube = build(
    serviceName="youtube",
    version="v3",
    developerKey=API_KEY
)


# UTILIDADES
def extraer_emojis(text):
    return [char for char in text if char in emoji.EMOJI_DATA]



# EXTRACCIÓN DE COMENTARIOS
def extraer_comentarios(video_id):
    comments = []
    next_page_token = None

    while True:
        try:
            request = youtube.commentThreads().list(
                part="snippet,replies",
                videoId=video_id,
                maxResults=100,
                pageToken=next_page_token,
                textFormat="plainText"
            )

            response = request.execute()

            for item in response["items"]:
                snippet = item["snippet"]["topLevelComment"]["snippet"]

                base_comment = {
                    "video_id": video_id,
                    "comment_id": item["id"],
                    "text": snippet["textDisplay"],
                    "emojis": extraer_emojis(snippet["textDisplay"]),
                    "author": snippet["authorDisplayName"],
                    "likes": snippet["likeCount"],
                    "published_at": snippet["publishedAt"],
                    "is_reply": False,
                    "raw": snippet
                }

                comments.append(base_comment)

                # =========================
                # RESPUESTAS
                # =========================
                if "replies" in item:
                    for reply in item["replies"]["comments"]:
                        r = reply["snippet"]
                        comments.append({
                            "video_id": video_id,
                            "comment_id": reply["id"],
                            "parent_id": item["id"],
                            "text": r["textDisplay"],
                            "emojis": extraer_emojis(r["textDisplay"]),
                            "author": r["authorDisplayName"],
                            "likes": r["likeCount"],
                            "published_at": r["publishedAt"],
                            "is_reply": True,
                            "raw": r
                        })

            next_page_token = response.get("nextPageToken")

            if not next_page_token:
                break

            time.sleep(0.1)  # cuidamos cuota

        except HttpError as e:
            print(f"Error API: {e}")
            break

    return comments

if __name__ == "__main__":
    comments = extraer_comentarios(VIDEO_ID)
    print(f"Total de comentarios extraídos: {len(comments)}")
    print(comments[:2])