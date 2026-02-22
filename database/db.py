import sqlite3 as sqlite
from contextlib import contextmanager
from config import DB_NAME

@contextmanager
def get_db_connection():
    """Context Manager para administrar conexiones de DB"""
    conn = sqlite.connect(DB_NAME)
    conn.row_factory = sqlite.Row
    try:
        yield conn # Genera la conexion a db cada vez que se llama a la función
        conn.commit()
    except Exception as e:
        conn.rollback() # Rollback en caso de que cualquier consulta falle
        raise e
    finally:
        conn.close()

def init_db(): 
    """Init DB y creación de tabla videos si no existe"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS videos (
                id TEXT PRIMARY KEY,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

def videos_exists(video_id: str) -> bool:
    """Comprueba si el video está en la db por su id"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT 1 FROM videos WHERE id = ?
            """, 
            ((video_id,))
        )
        result = cursor.fetchone()
        return result is not None

def save_video(video_id: str):
    """Guarda el video por su id dentro de la db"""
    if not video_id or not video_id.strip():
        raise ValueError("El id no puede estar vacío") # Salta un error si video_id no tiene el formato correcto o si esta vacío
    with get_db_connection() as conn:
        cursor = conn.cursor()
        try: 
            cursor.execute(
                """
                INSERT INTO videos(id) VALUES (?)
                """,
                (video_id,)
            )
        except sqlite.IntegrityError:
            raise ValueError(f"El video con id {video_id} no es nuevo") # El id del video ya está en la db

def get_all_videos():
    """Obtener todos los videos ordenados por fecha de creación"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.exectute(
            """
            SELECT id, created_at
            FROM videos
            ORDER BY created_at DESC
            """
        )
        return [dict(row) for row in cursor.fetchall()]
