import requests
from datetime import datetime

HANDLE = "mh_promit"
README_FILE = "README.md"
NUM_SUBMISSIONS_TO_DISPLAY = 10 

def fetch_submissions(count=NUM_SUBMISSIONS_TO_DISPLAY):
    url = f"https://codeforces.com/api/user.status?handle={HANDLE}&from=1&count={count}"
    res = requests.get(url).json()
    if res["status"] != "OK":
        raise Exception(f"Failed to fetch submissions: {res.get('comment', 'Unknown error')}")

    submissions_data = []
    for submission in res["result"]:
        if "problem" not in submission:
            continue

        problem = submission["problem"]
        verdict = submission.get("verdict", "N/A")
        lang = submission.get("programmingLanguage", "Unknown")

        creation_time = submission.get("creationTimeSeconds")
        time_utc_str = datetime.utcfromtimestamp(creation_time).strftime("%Y-%m-%d %H:%M UTC") if creation_time else "N/A"

        execution_time_ms = submission.get("timeConsumedMillis", "N/A")
        memory_consumed_bytes = submission.get("memoryConsumedBytes", "N/A")

        memory_kb = f"{int(memory_consumed_bytes / 1024)} KB" if isinstance(memory_consumed_bytes, (int, float)) else "N/A"
        execution_time_str = f"{execution_time_ms} ms" if isinstance(execution_time_ms, (int, float)) else "N/A"

        problem_name = f'{problem["index"]}. {problem["name"]}'
        problem_link = f'https://codeforces.com/contest/{problem["contestId"]}/problem/{problem["index"]}'
        submission_link = f'https://codeforces.com/contest/{problem["contestId"]}/submission/{submission["id"]}'

        verdict_icon = "✅ Accepted" if verdict == "OK" else f"❌ {verdict.replace('_', ' ')}"

        who = HANDLE

        submissions_data.append({
            "id": submission["id"],
            "time_utc": time_utc_str,
            "who": who,
            "problem_name": problem_name,
            "problem_link": problem_link,
            "lang": lang,
            "verdict": verdict_icon,
            "execution_time": execution_time_str,
            "memory": memory_kb,
            "submission_link": submission_link
        })
    return submissions_data

def update_readme(submissions_list):
    # The graph_section variable is removed, so it won't be included in the README.md

    submission_header = f"""\
<p align="center">
  ## 🚀 Latest {NUM_SUBMISSIONS_TO_DISPLAY} Codeforces Submissions for {HANDLE}
</p>
"""

    table_header = (
        "| Time (UTC) | Who | Problem | Language | Verdict | Time (ms) | Memory | Submission |\n"
        "|------------|-----|---------|----------|---------|-----------|--------|------------|"
    )

    table_rows = []
    if not submissions_list:
        table_rows.append("| _No submissions found._ | | | | | | | |")
    else:
        for info in submissions_list:
            row = (
                f'| {info["time_utc"]} '
                f'| {info["who"]} '
                f'| [{info["problem_name"]}]({info["problem_link"]}) '
                f'| {info["lang"]} '
                f'| {info["verdict"]} '
                f'| {info["execution_time"]} '
                f'| {info["memory"]} '
                f'| [Link]({info["submission_link"]}) |'
            )
            table_rows.append(row)

    # *** new_content_block no longer includes graph_section ***
    new_content_block = (
        f"{submission_header}\n\n"
        f"{table_header}\n" + "\n".join(table_rows) + "\n"
    )

    with open(README_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    start_index = -1
    for i, line in enumerate(lines):
        # The script will still find the "## 🚀" heading to replace the block
        if line.strip().startswith("## 🚀"):
            start_index = i
            break

    updated_content = []
    if start_index != -1:
        updated_content = lines[:start_index]
        updated_content.append(new_content_block)
    else:
        print("Warning: Existing Codeforces section heading not found in README.md. Appending new content.")
        updated_content = lines
        updated_content.append("\n")
        updated_content.append(new_content_block)

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write("".join(updated_content))

def main():
    try:
        submissions = fetch_submissions()
        update_readme(submissions)
        print("README.md updated successfully with latest submissions!")
    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == "__main__":
    main()
