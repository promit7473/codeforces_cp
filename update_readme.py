import requests
from datetime import datetime

HANDLE = "mh_promit"
README_FILE = "README.md"
COUNT = 10

def fetch_submissions():
    url = f"https://codeforces.com/api/user.status?handle={HANDLE}&from=1&count={COUNT}"
    res = requests.get(url).json()
    if res["status"] != "OK":
        raise Exception("Failed to fetch submissions")
    return res["result"]

def format_submission(sub):
    problem = sub["problem"]
    verdict = sub.get("verdict", "N/A")
    lang = sub.get("programmingLanguage", "Unknown")
    time = datetime.utcfromtimestamp(sub["creationTimeSeconds"]).strftime("%Y-%m-%d %H:%M UTC")

    name = f'{problem["index"]}. {problem["name"]}'
    link = f'https://codeforces.com/contest/{problem["contestId"]}/problem/{problem["index"]}'
    submission_link = f'https://codeforces.com/contest/{problem["contestId"]}/submission/{sub["id"]}'

    verdict_icon = "✅ Accepted" if verdict == "OK" else f"❌ {verdict.replace('_', ' ')}"

    return f"| [{name}]({link}) | {verdict_icon} | {lang} | {time} | [Link]({submission_link}) |"

def update_readme(submissions):
    table_header = """\
## 🚀 Last 10 Codeforces Submissions

| Problem | Verdict | Language | Time | Submission |
|---------|---------|----------|------|------------|
"""
    table_rows = [format_submission(sub) for sub in submissions]
    table = table_header + "\n".join(table_rows) + "\n"

    with open(README_FILE, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        start = 0
        for i, line in enumerate(lines):
            if line.strip().startswith("## 🚀 Last 10 Codeforces Submissions"):
                start = i
                break
        else:
            lines.append("\n" + table)
            f.seek(0)
            f.writelines(lines)
            return

        # Find where the current table ends
        end = start
        while end < len(lines) and lines[end].strip() != "":
            end += 1

        lines[start:end] = table.splitlines(keepends=True)
        f.seek(0)
        f.writelines(lines)
        f.truncate()

if __name__ == "__main__":
    submissions = fetch_submissions()
    update_readme(submissions)

