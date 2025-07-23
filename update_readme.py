import requests
from datetime import datetime

HANDLE = "mh_promit"
README_FILE = "README.md"
NUM_SUBMISSIONS_TO_DISPLAY = 10 # Set this to 5 or 10 as desired

def fetch_submissions(count=NUM_SUBMISSIONS_TO_DISPLAY):
    """Fetches the latest 'count' submissions for the specified handle."""
    url = f"https://codeforces.com/api/user.status?handle={HANDLE}&from=1&count={count}"
    res = requests.get(url).json()
    if res["status"] != "OK":
        raise Exception(f"Failed to fetch submissions: {res.get('comment', 'Unknown error')}")

    submissions_data = []
    for submission in res["result"]:
        # Skip non-problem submissions (e.g., contest registrations, or if problem info is missing)
        if "problem" not in submission:
            continue

        problem = submission["problem"]
        verdict = submission.get("verdict", "N/A")
        lang = submission.get("programmingLanguage", "Unknown")

        # Ensure creationTimeSeconds exists before converting
        creation_time = submission.get("creationTimeSeconds")
        time_utc_str = datetime.utcfromtimestamp(creation_time).strftime("%Y-%m-%d %H:%M UTC") if creation_time else "N/A"

        # Convert UTC time to UTC+6 (Dhaka time)
        # This is an approximation as datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=6)))
        # would be more precise for current time, but for historical API data, just adding hours is fine.
        # However, for consistency with Codeforces display, we'll keep it simple as UTC and let user convert.
        # If you *really* want UTC+6 converted from UTC timestamp:
        # from pytz import timezone # you'd need to pip install pytz
        # from datetime import timedelta
        # utc_dt = datetime.utcfromtimestamp(creation_time).replace(tzinfo=timezone('UTC'))
        # bst_dt = utc_dt.astimezone(timezone('Asia/Dhaka'))
        # time_bst_str = bst_dt.strftime("%Y-%m-%d %H:%M UTC+6")
        # For simplicity, we'll just show UTC time or rely on the browser to convert.
        # Let's stick to UTC for now as it's directly from API and less dependency.

        execution_time_ms = submission.get("timeConsumedMillis", "N/A")
        memory_consumed_bytes = submission.get("memoryConsumedBytes", "N/A")

        # Format memory to KB, or keep as N/A
        memory_kb = f"{int(memory_consumed_bytes / 1024)} KB" if isinstance(memory_consumed_bytes, (int, float)) else "N/A"
        execution_time_str = f"{execution_time_ms} ms" if isinstance(execution_time_ms, (int, float)) else "N/A"

        problem_name = f'{problem["index"]}. {problem["name"]}'
        problem_link = f'https://codeforces.com/contest/{problem["contestId"]}/problem/{problem["index"]}'
        submission_link = f'https://codeforces.com/contest/{problem["contestId"]}/submission/{submission["id"]}'

        verdict_icon = "✅ Accepted" if verdict == "OK" else f"❌ {verdict.replace('_', ' ')}"

        # Use handle for 'Who' column
        who = HANDLE # This will always be your handle

        submissions_data.append({
            "id": submission["id"], # Submission ID
            "time_utc": time_utc_str, # Submission Time
            "who": who, # Your handle
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
    # Header for the new table
    header = f"## 🚀 Latest {NUM_SUBMISSIONS_TO_DISPLAY} Codeforces Submissions for {HANDLE}"

    # New table header based on your desired format
    table_header = (
        "| ID | Time (UTC) | Who | Problem | Language | Verdict | Time (ms) | Memory |\n"
        "|----|------------|-----|---------|----------|---------|-----------|--------|"
    )

    # Generate table rows for each submission
    table_rows = []
    if not submissions_list:
        table_rows.append("| _No submissions found._ | | | | | | | |") # Ensure enough cells for the header
    else:
        for info in submissions_list:
            row = (
                f'| {info["id"]} '
                f'| {info["time_utc"]} '
                f'| {info["who"]} '
                f'| [{info["problem_name"]}]({info["problem_link"]}) '
                f'| {info["lang"]} '
                f'| {info["verdict"]} '
                f'| {info["execution_time"]} '
                f'| {info["memory"]} |'
            )
            table_rows.append(row)

    new_content_block = f"{header}\n\n{table_header}\n" + "\n".join(table_rows) + "\n"

    # Read the current content of README.md
    with open(README_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Find the start of the existing Codeforces submissions section
    start_index = -1
    for i, line in enumerate(lines):
        if line.strip().startswith("## 🚀"): # Find the heading
            start_index = i
            break

    updated_content = []
    if start_index != -1:
        updated_content = lines[:start_index] # Keep all lines before the heading
        updated_content.append(new_content_block) # Add the new content block
    else:
        print("Warning: Existing Codeforces section heading not found in README.md. Appending new content.")
        updated_content = lines # Keep existing lines
        updated_content.append("\n") # Add a newline for separation
        updated_content.append(new_content_block)

    # Write the updated content back to README.md
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write("".join(updated_content))

def main():
    try:
        submissions = fetch_submissions()
        update_readme(submissions)
        print("README.md updated successfully with latest submissions!")
    except Exception as e:
        print(f"Error: {e}")
        raise # Ensure the action fails if there's an error

if __name__ == "__main__":
    main()
