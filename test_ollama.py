import requests

print("Testing Ollama Connection...")

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5:1.5b",
        "prompt": "Hello! Introduce yourself.",
        "stream": False
    }
)

if response.status_code == 200:
    result = response.json()
    print("\nOllama Response:")
    print(result["response"])
else:
    print("Error:", response.text)