#!/usr/bin/env python3
"""
Main demo script to test both Pexels and Unsplash APIs
"""

from pexels_image import get_random_image_pexels
from unsplash_image import get_random_image


def main():
    print("=" * 60)
    print("Random Query Images - Demo")
    print("=" * 60)
    
    # Test Pexels API
    print("\n📸 Fetching image from Pexels...")
    pexels_url = get_random_image_pexels()
    print(f"✅ Pexels Image URL: {pexels_url}")
    
    print("\n" + "-" * 60)
    
    # Test Unsplash API
    print("\n📸 Fetching image from Unsplash...")
    unsplash_url = get_random_image()
    print(f"✅ Unsplash Image URL: {unsplash_url}")
    
    print("\n" + "=" * 60)
    print("Demo completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()