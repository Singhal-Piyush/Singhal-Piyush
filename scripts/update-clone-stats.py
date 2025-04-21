# scripts/update-clone-stats.py
import requests
import os
import re

USERNAME = "Singhal-Piyush"
REPO = "MLOPS_Indian_Flight_Price_Prediction"
TOKEN = os.getenv("GITHUB_TOKEN")

headers = {"Authorization": f"token {TOKEN}"}
url = f"https://api.github.com/repos/{USERNAME}/{REPO}/traffic/clones"

response = requests.get(url, headers=headers)
data = response.json()

clones = data.get("count", 0)
uniques = data.get("uniques", 0)

# Read README
with open("README.md", "r", encoding="utf-8") as file:
    readme = file.read()

# Replace placeholder
new_stats = f"🔁 Repo cloned **{clones} times** by **{uniques} unique users** in the last 14 days 🚀"
updated_readme = re.sub(
    r"(<!-- clone-stats-start -->).*?(<!-- clone-stats-end -->)",
    rf"\1{new_stats}\2",
    readme,
    flags=re.DOTALL,
)

# Save README
with open("README.md", "w", encoding="utf-8") as file:
    file.write(updated_readme)