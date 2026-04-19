import requests
from datetime import datetime
import os


TOKEN = os.getenv("TOKEN")

print("TOKEN CHECK:", TOKEN[:10] if TOKEN else "NO TOKEN")


if not TOKEN:
    print("KEIN TOKEN GESETZT!")
    exit(1)

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

query = """
{
  repository(owner: "IPROBA-Group7", name: "Github") {
    issues(first: 20) {
      nodes {
        number
        title
        createdAt
        closedAt
      }
    }
  }
}
"""

response = requests.post(
    "https://api.github.com/graphql",
    json={"query": query},
    headers=headers
)

data = response.json()
print("DEBUG:", data)

cycle_times = []

print("\nCycle Time (Pro):\n")


if "data" not in data:
    print("API ERROR:", data)
    exit(1)

for issue in data["data"]["repository"]["issues"]["nodes"]:
    if issue["closedAt"]:
        start = datetime.strptime(issue["createdAt"], "%Y-%m-%dT%H:%M:%SZ")
        end = datetime.strptime(issue["closedAt"], "%Y-%m-%dT%H:%M:%SZ")

        hours = (end - start).total_seconds() / 3600
        cycle_times.append(hours)

        print(f"Issue #{issue['number']}: {hours:.2f} Stunden")

if cycle_times:
    avg = sum(cycle_times) / len(cycle_times)
    print(f"\nDurchschnitt Cycle Time: {avg:.2f} Stunden")
else:
    print("Keine Daten")
