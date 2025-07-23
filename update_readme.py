import requests
from datetime import datetime, UTC # Import UTC for modern datetime handling

HANDLE = "mh_promit"
README_FILE = "README.md"
NUM_SUBMISSIONS_TO_DISPLAY = 10 # <--- Set this to 5 or 10 as desired

def fetch_submissions(count=NUM_SUBMISSIONS_TO_DISPLAY):
    """Fetches the latest 'count' submissions for the specified handle."""
    url = f"https://codeforces.com/api/user.status?handle={HANDLE}&from=1&count={count}"
    res = requests.get(url).json()
    if res["status"] != "OK":
        raise Exception(f"Failed to fetch submissions: {res.get('comment', 'Unknown error')}")

    submissions_data = []
    for submission in res["result"]:
        # Skip non-problem submissions (e.g., contest registrations if they appear)
        if "problem" not in submission:
            continue

        problem = submission["problem"]
        verdict = submission.get("verdict", "N/A")
        lang = submission.get("programmingLanguage", "Unknown")

        # Use timezone-aware datetime for creation time (modern approach)
        creation_time = submission.get("creationTimeSeconds")
        if creation_time:
            # Convert to a timezone-aware UTC datetime object
            dt_object = datetime.fromtimestamp(creation_time, UTC) # Use datetime.UTC
            # Format as desired. Consider shortening for sleekness, e.g., "YYYY-MM-DD HH:MM"
            time_str = dt_object.strftime("%Y-%m-%d %H:%M UTC")
        else:
            time_str = "N/A"

        name = f'{problem["index"]}. {problem["name"]}'
        link = f'https://codeforces.com/contest/{problem["contestId"]}/problem/{problem["index"]}'
        submission_link = f'https://codeforces.com/contest/{problem["contestId"]}/submission/{submission["id"]}'

        # Enhanced verdict icons for sleekness
        if verdict == "OK":
            verdict_icon = "✔ Accepted" # A simpler checkmark
        elif "WRONG_ANSWER" in verdict:
            verdict_icon = "✘ WA"      # Shorter for wrong answer
        elif "TIME_LIMIT_EXCEEDED" in verdict:
            verdict_icon = "⏳ TLE"     # Shorter for time limit exceeded
        elif "COMPILATION_ERROR" in verdict:
            verdict_icon = "⚙ CE"      # Shorter for compilation error
        elif "RUNTIME_ERROR" in verdict:
            verdict_icon = "💥 RE"      # Shorter for runtime error
        elif "IDLENESS_LIMIT_EXCEEDED" in verdict:
            verdict_icon = "😴 ILLE" # Idleness limit exceeded
        elif "MEMORY_LIMIT_EXCEEDED" in verdict:
            verdict_icon = "🧠 MLE" # Memory limit exceeded
        elif "PRESENTATION_ERROR" in verdict:
            verdict_icon = "💡 PE" # Presentation Error
        else:
            verdict_icon = f"❓ {verdict.replace('_', ' ')}" # Fallback for others

        # Shorten language names if they are too long for the table
        if "C++" in lang:
            lang_short = "C++"
        elif "Python" in lang:
            lang_short = "Python"
        elif "Java" in lang:
            lang_short = "Java"
        elif "Kotlin" in lang:
            lang_short = "Kotlin"
        elif "JavaScript" in lang:
            lang_short = "JS"
        elif "C#" in lang:
            lang_short = "C#"
        elif "Go" in lang:
            lang_short = "Go"
        elif "Rust" in lang:
            lang_short = "Rust"
        else:
            lang_short = lang.split()[0] # Take the first word, e.g., "GNU" from "GNU C++"

        submissions_data.append({
            "name": name,
            "link": link,
            "verdict": verdict_icon,
            "lang": lang_short, # Use shortened language
            "time": time_str,
            "submission_link": submission_link
        })
    return submissions_data

def update_readme(submissions_list):
    # Header for the new table
    header = "## 🚀 Latest Codeforces Submissions"
    # Adjusted table header for better alignment and potential sleekness
    table_header = "| Problem | Verdict | Lang | Time (UTC) | Submission |\n|---|---|---|---|---|"

    # Generate table rows for each submission
    table_rows = []
    if not submissions_list:
        table_rows.append("| _No submissions found._ | | | | |")
    else:
        for info in submissions_list:
            # Ensure proper Markdown linking for problem and submission
            problem_link_md = f'[{info["name"]}]({info["link"]})'
            submission_link_md = f'[Link]({info["submission_link"]})'
            row = f'| {problem_link_md} | {info["verdict"]} | {info["lang"]} | {info["time"]} | {submission_link_md} |'
            table_rows.append(row)

    new_content_block = f"{header}\n\n{table_header}\n" + "\n".join(table_rows) + "\n" # Add a final newline for neatness

    # Read the current content of README.md
    with open(README_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Find the start of the existing Codeforces submissions section
    start_index = -1
    for i, line in enumerate(lines):
        # Look for lines that start with "## 🚀" (your current heading)
        if line.strip().startswith("## 🚀"):
            start_index = i
            break

    updated_content = []
    if start_index != -1:
        # Keep all lines before the target section
        updated_content = lines[:start_index]
        # Add the new content block
        updated_content.append(new_content_block)
    else:
        # If the marker is not found, append the new block at the end
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
        # Ensure the action fails if there's an error in the script
        raise

if __name__ == "__main__":
    main()
