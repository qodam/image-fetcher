# Random Images API

A simple Python project to fetch random images from Pexels and Unsplash APIs.

## 📋 Prerequisites

- Python 3.7+
- Pexels account (to get a free API key)
- Unsplash account (to get a free API key)

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/qodam/image-fetcher.git
cd image-fetcher
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `config.py` file from the template:
```bash
cp config.example.py config.py
```

4. Add your API keys in `config.py`:
   - Get your Pexels API key at [https://www.pexels.com/api/](https://www.pexels.com/api/)
   - Get your Unsplash API key at [https://unsplash.com/developers](https://unsplash.com/developers)

## 📖 Usage

### With Pexels

```python
from pexels_image import get_random_image_pexels

image_url = get_random_image_pexels()
print(f"Image URL: {image_url}")
```

### With Unsplash

```python
from unsplash_image import get_random_image

image_url = get_random_image()
print(f"Image URL: {image_url}")
```

### Demo Script

```bash
python main.py
```

## 📁 Project Structure

```
random-tree-images/
│
├── pexels_image.py          # Pexels API module
├── unsplash_image.py        # Unsplash API module
├── config.py                # Your API keys (not tracked)
├── config.example.py        # Config template
├── main.py                  # Demo script
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## 🔑 API Keys

Both APIs offer free tiers:

- **Pexels**: 200 requests per hour
- **Unsplash**: 50 requests per hour (demo), 5000/hour (production)

## 🖼️ Image Specifications

- **Dimensions**: 720x1280 pixels (portrait orientation)
- **Format**: JPEG/PNG
- **Query**: Oak trees and general images

## 🛡️ Error Handling

Both modules include:
- Request timeout handling (10 seconds)
- HTTP error handling
- Fallback to placeholder images if API fails

## ⚠️ Important Notes

- Never commit your `config.py` file with real API keys
- Respect API rate limits
- Images are subject to their respective licenses (Pexels License / Unsplash License)
