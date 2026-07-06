import os
import requests
from dotenv import load_dotenv

load_dotenv()


class GeminiProvider:
    def __init__(self, api_key=None, model="gemini-2.5-flash"):
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        self.model = model

    def generate(self, prompt: str) -> str:
        if not self.api_key:
            return "Missing API Key"

        url = (
            f"https://generativelanguage.googleapis.com/v1beta/models/"
            f"{self.model}:generateContent?key={self.api_key}"
        )

        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }

        try:
            r = requests.post(url, json=payload, timeout=60)
            r.raise_for_status()

            data = r.json()

            return data["candidates"][0]["content"]["parts"][0]["text"]

        except Exception as e:
            return f"Error: {e}"
