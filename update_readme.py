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
    # This is the new content block that will replace the existing one in README.md
    new_content_block = f"""\
## 🚀 Latest Codeforces Submission

| Problem | Verdict | Language | Time | Link |
|--------|---------|----------|------|------|
| [{info["name"]}]({info["link"]}) | {info["verdict"]} | {info["lang"]} | {info["time"]} | [Submission]({info["submission_link"]}) |
"""
    # Read the current content of README.md
    with open(README_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Find the line where the existing Codeforces submission section starts
    # Based on your README.md, it starts with "## 🚀 Last 10 Codeforces Submissions"
    start_index = -1
    for i, line in enumerate(lines):
        # We'll look for any line starting with "## 🚀" to be flexible
        if line.strip().startswith("## 🚀"):
            start_index = i
            break

    # Reconstruct the README content
    if start_index != -1:
        # Keep all lines before the found heading
        updated_lines = lines[:start_index]
        # Add the new content block
        updated_lines.append(new_content_block)
        # Join all lines to form the complete new content for README.md
        updated_content = "".join(updated_lines)
    else:
        # If the marker "## 🚀" is not found, append the new block at the end
        # This is a fallback, ideally the marker should always be there.
        print("Warning: Existing Codeforces section heading not found in README.md. Appending new content.")
        updated_content = "".join(lines) + "\n" + new_content_block # Add a newline for separation

    # Write the updated content back to README.md (this overwrites the file)
    with open(README_FILE, "w", encoding="utf-8") as
