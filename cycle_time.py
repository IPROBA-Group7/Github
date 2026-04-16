from github import Github
from datetime import datetime

g = Github("TOKEN")
repo = g.get_repo("IPROBA-Group7/Github")

issues = repo.get_issues(state="closed")

for issue in issues:
    created = issue.created_at
    closed = issue.closed_at
    
    lead_time = (closed - created).days
    
    print(f"Issue #{issue.number}: {lead_time} days")
