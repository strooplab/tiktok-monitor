from playwright.sync_api import sync_playwright
from config import TIKTOK_USERNAME

def get_latest_videos(browser, context, max_videos: int = 5) -> list:
    """
    Obtiene los últimos videos de TikTok.
    
    Args:
        max_videos: Número máximo de videos a obtener
    
    Returns:
        Lista de IDs de videos únicos
    """
    videos = []
    
    try:
            page = context.new_page()
            
            # Navegar al perfil
            url = f"https://www.tiktok.com/@{TIKTOK_USERNAME}"
            print(f"Navegando a {url}")
            page.goto(url, wait_until="networkidle") 
            print(page.title())
            # Esperar a que carguen los videos
            try:
                page.wait_for_selector('a[href*="/video/"]', timeout=10000)
                print("Videos encontrados")
            except:
                print("No se encontraron videos")
                return []
            
            # Scroll para cargar más videos
            for _ in range(2):  # Scroll 2 veces
                page.mouse.wheel(0, 1000)
                page.wait_for_timeout(2000)
            
            # Obtener videos
            video_links = page.query_selector_all('a[href*="/video/"]')
            print(f"Encontrados {len(video_links)} links de video")
            
            # Procesar
            for link in video_links[:max_videos]:
                href = link.get_attribute("href")
                if href and "/video/" in href:
                    try:
                        video_id = href.split("/video/")[1].split("?")[0]
                        videos.append(video_id)
                        print(f"Video encontrado: {video_id}")
                    except IndexError:
                        print(f"Error extrayendo ID de: {href}")
                        continue
            
            browser.close()
            
    except Exception as e:
        print(f"Error general: {e}")
        return []
    
    # Eliminar duplicados y retornar
    return list(set(videos))
