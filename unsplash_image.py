import requests
import config


def get_random_image(query=None):
    """
    Fetches a random "query" image in 720x1280 from Unsplash via official API.
    
    Returns:
        str: Final URL of the image
    """
    width = 720
    height = 1280

    url = f"https://api.unsplash.com/photos/random?query={query}&orientation=portrait&client_id={config.UNSPLASH_ACCESS_KEY}"

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        
        # Get regular size URL
        image_url = data.get("urls", {}).get("regular")
        
        if image_url:
            # Add exact dimensions
            # Unsplash supports resizing via URL parameters
            image_url = f"{image_url}&w={width}&h={height}&fit=crop"
            return image_url
            
    except requests.exceptions.RequestException as e:
        print(f"Unsplash API Error: {e}")

    # Fallback if API fails
    return f"https://via.placeholder.com/{width}x{height}.png?text=query"