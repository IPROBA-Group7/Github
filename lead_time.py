import requests
from datetime import datetime

REPO = "IPROBA-Group7/Github"

url = f"https://api.github.com/repos/{REPO}/pulls?state=closed&per_page=100"
response = requests.get(url)

if response.status_code != 200:
    print("API Fehler:", response.json())
    exit(1)

prs = response.json()

lead_times = []

print("PR Lead Times:\n")

for pr in prs:
    if isinstance(pr, dict) and pr.get("merged_at"):
        created = datetime.strptime(pr["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        merged = datetime.strptime(pr["merged_at"], "%Y-%m-%dT%H:%M:%SZ")

        hours = (merged - created).total_seconds() / 3600
        lead_times.append(hours)

        print(f"PR #{pr['number']}: {hours:.2f} Stunden")

if lead_times:
    avg = sum(lead_times) / len(lead_times)
    print(f"\nDurchschnitt: {avg:.2f} Stunden")

with open("README.md", "w") as f:
    f.write("# Github Projekt\n\n")
    f.write("## PR Lead Time\n\n")
    
    if lead_times:
        f.write(f"Durchschnitt: {avg:.2f} Stunden\n")
    else:
        f.write("Keine gemergten PRs gefunden\n")
