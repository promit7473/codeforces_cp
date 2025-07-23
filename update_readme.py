import requests
from datetime import datetime

HANDLE = "mh_promit"
README_FILE = "README.md"

def fetch_latest_submission():
    url = f"https://codeforces.com/api/user.status?handle={HANDLE}&from=1&count=1"
    res = requests.get(url).json()
    if res["status"] != "OK":
        raise Exception("Failed to fetch submissions")

    submission = res["result"][0]
    problem = submission["problem"]
    verdict = submission.get("verdict", "N/A")
    lang = submission.get("programmingLanguage", "Unknown")
    time = datetime.utcfromtimestamp(submission["creationTimeSeconds"]).strftime("%Y-%m-%d %H:%M UTC")
    
    name = f'{problem["index"]}. {problem["name"]}'
    link = f'https://codeforces.com/contest/{problem["contestId"]}/problem/{problem["index"]}'
    submission_link = f'https://codeforces.com/contest/{problem["contestId"]}/submission/{submission["id"]}'
    
    verdict_icon = "✅ Accepted" if verdict == "OK" else f"❌ {verdict.replace('_', ' ')}"

    return {
        "name": name,
        "link": link,
        "verdict": verdict_icon,
        "lang": lang,
        "time": time,
        "submission_link": submission_link
    }

def update_readme(info):
    content = f"""\
## 🚀 Latest Codeforces Submission

| Problem | Verdict | Language | Time | Link |
|--------|---------|----------|------|------|
| [{info["name"]}]({info["link"]}) | {info["verdict"]} | {info["lang"]} | {info["time"]} | [Submission]({info["submission_link"]}) |
"""
    with open(README_FILE, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        start = 0
        for i, line in enumerate(lines):
            if line.strip().startswith("## 🚀 Latest Codeforces Submission"):
                start = i
                break
        else:
            lines.append("\n" + content)
            f.seek(0)
            f.writelines(lines)
            return

        lines[start:start+6] = content.splitlines(keepends=True)
        f.seek(0)
        f.writelines(lines)
        f.truncate()

if __name__ == "__main__":
    info = fetch_latest_submission()
    update_readme(info)
