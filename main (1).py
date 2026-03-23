#This is a API web search program created by Derrick Hobbs it is licensed under the Creative Common Attribution Non Commercial (CC BY -NC) License Copyright(C) 2026 Derrick Hobbs#
import requests

# --- Query Box ---
query = input("Please enter your search information in the query: ")

# --- API Request ---
url = "https://api.duckduckgo.com/"
params = {
    "q": query,
    "format": "json",
    "no_html": 1
}

response = requests.get(url, params=params)
data = response.json()

# --- Output ---
print("\nSearch Query:", query)
print("Title:", data.get("Heading", "No title found"))
print("Summary:", data.get("AbstractText", "No summary available"))
print("Image URL:", data.get("Image", "No image available"))
print("Abstract Source:", data.get("AbstractSource", "No source"))
print("Abstract URL:", data.get("AbstractURL", "No URL"))
print("Definition:", data.get("Definition", "No definition"))
