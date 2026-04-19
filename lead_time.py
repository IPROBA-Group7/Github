import requests
from datetime import datetime

REPO = "DEIN_USERNAME/DEIN_REPO"

url = f"https://api.github.com/repos/{REPO}/pulls?state=closed&per_page=100"
response = requests.get(url)
prs = response.json()

lead_times = []

print("PR Lead Times:\n")

for pr in prs:
    if pr["merged_at"]:
        created = datetime.strptime(pr["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        merged = datetime.strptime(pr["merged_at"], "%Y-%m-%dT%H:%M:%SZ")

        hours = (merged - created).total_seconds() / 3600
        lead_times.append(hours)

        print(f"PR #{pr['number']}: {hours:.2f} Stunden")

if lead_times:
    avg = sum(lead_times) / len(lead_times)
    print(f"\nDurchschnitt: {avg:.2f} Stunden")
