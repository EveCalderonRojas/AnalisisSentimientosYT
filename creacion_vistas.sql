use AnalisisSentimientosYT

select * from dbo.comments_main
select * from dbo.comments_reply

--CREACIÓN DE VISTAS

--COMENTARIOS Y SENTIMIENTOS
CREATE VIEW comentarios_sentimiento AS
SELECT
    comment_id,
    video_id,
    sentiment_label,
    sentiment_score,
    tema,
    likes,
    CAST(published_at AS DATE) AS fecha
FROM dbo.comments_main;


--DISTRIBUCIÓN SENTIMIENTOS
CREATE VIEW distribucion_sentimiento AS
SELECT
    sentiment_label,
    COUNT(*) AS total_comentarios
FROM dbo.comments_main
GROUP BY sentiment_label;


--SENTIMIENTO POR TEMA
CREATE VIEW sentimiento_por_tema AS
SELECT
    tema,
    sentiment_label,
    COUNT(*) AS total_comentarios
FROM dbo.comments_main
GROUP BY tema, sentiment_label;


--VISTA POR LIKES
CREATE VIEW comentarios_likes AS
SELECT
    comment_id,
    tema,
    sentiment_label,
    likes
FROM dbo.comments_main
WHERE likes > 0;


--VISTA DE EVOLUCIÓN DE TEMAS
CREATE VIEW sentimiento_tiempo_legible AS
SELECT
    YEAR(published_at) AS year,
    DATENAME(MONTH, published_at) AS month_name,
    MONTH(published_at) AS month_num,
    sentiment_label,
    COUNT(*) AS total_comentarios
FROM dbo.comments_main
GROUP BY
    YEAR(published_at),
    DATENAME(MONTH, published_at),
    MONTH(published_at),
    sentiment_label;




--VISTA COMENTARIOS Y REPLIES
CREATE VIEW comentarios_con_replies AS
SELECT
    c.comment_id,
    c.tema,
    c.sentiment_label,
    COUNT(r.reply_id) AS total_replies
FROM dbo.comments_main c
LEFT JOIN dbo.comments_reply r
    ON c.comment_id = r.parent_id
GROUP BY c.comment_id, c.tema, c.sentiment_label;



