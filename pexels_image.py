import requests
import random
import config


def get_random_image_pexels(query=None):

    """
    Fetches a random portrait 'query' image from Pexels.
    
    Returns:
        str: URL of the image (720x1280 pixels)
    """
    url = f"https://api.pexels.com/v1/search?query={query}&orientation=portrait&per_page=80"

    headers = {
        "Authorization": config.PEXELS_API_KEY
    }

    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        photos = data.get("photos", [])
        
        if not photos:
            raise Exception("No photos found on Pexels")
        
        # Choose a random photo
        photo = random.choice(photos)
        
        # Get large image URL
        image_url = photo["src"]["large2x"]
        
        # Force 720x1280 size using Pexels CDN transformation
        image_url = f"{image_url}?w=720&h=1280&fit=crop"
        
        return image_url
        
    except requests.exceptions.RequestException as e:
        print(f"Pexels API Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

    # Fallback if Pexels fails
    return "https://via.placeholder.com/720x1280.png?text=query"