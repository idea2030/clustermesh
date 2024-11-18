#!/bin/bash

import os
import requests
from dotenv import load_dotenv
import json
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

def generate_and_save_image(prompt):
  # Get API key from environment variables
  api_key = os.getenv('OPENAI_API_KEY')
  if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

  # API endpoint
  url = "https://api.openai.com/v1/images/generations"

  # Request headers
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }

  # Request body
  data = {
    "model": "dall-e-3",
    "prompt": prompt,
    "n": 1,
    "size": "1024x1024"
  }

  try:
    # Make the API request
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()  # Raise an exception for bad status codes

    # Parse the response
    result = response.json()

    # Get the image URL from the response
    image_url = result['data'][0]['url']

    # Download the image
    image_response = requests.get(image_url)
    image_response.raise_for_status()

    # Create images directory if it doesn't exist
    if not os.path.exists('images'):
      os.makedirs('images')

    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"images/meshcluster_{timestamp}.png"

    # Save the image
    with open(filename, 'wb') as f:
      f.write(image_response.content)

    print(f"Image successfully saved as {filename}")
    return filename

  except requests.exceptions.RequestException as e:
    print(f"Error during API request: {e}")
    return None
  except KeyError as e:
    print(f"Error parsing API response: {e}")
    return None
  except Exception as e:
    print(f"Unexpected error: {e}")
    return None

if __name__ == "__main__":
  prompt = "MeshCluster a novel distributed system architecture for managing local energy and computing resources, MESH CLUSTER: Adaptive Infrastructure for Critical Situations"
  generate_and_save_image(prompt)
