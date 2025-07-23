import requests

from datetime import datetime



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



        # Ensure creationTimeSeconds exists before converting

        creation_time = submission.get("creationTimeSeconds")

        time_str = datetime.utcfromtimestamp(creation_time).strftime("%Y-%m-%d %H:%M UTC") if creation_time else "N/A"



        name = f'{problem["index"]}. {problem["name"]}'

        link = f'https://codeforces.com/contest/{problem["contestId"]}/problem/{problem["index"]}'

        submission_link = f'https://codeforces.com/contest/{problem["contestId"]}/submission/{submission["id"]}'



        verdict_icon = "✅ Accepted" if verdict == "OK" else f"❌ {verdict.replace('_', ' ')}"



        submissions_data.append({

            "name": name,

            "link": link,

            "verdict": verdict_icon,

            "lang": lang,

            "time": time_str,

            "submission_link": submission_link

        })

    return submissions_data



def update_readme(submissions_list):

    # Header for the new table

    header = "## 🚀 Latest Codeforces Submissions"

    table_header = "| Problem | Verdict | Language | Time | Submission |\n|---------|---------|----------|------|------------|"



    # Generate table rows for each submission

    table_rows = []

    if not submissions_list:

        table_rows.append("| _No submissions found._ | | | | |")

    else:

        for info in submissions_list:

            row = f'| [{info["name"]}]({info["link"]}) | {info["verdict"]} | {info["lang"]} | {info["time"]} | [Link]({info["submission_link"]}) |'

            table_rows.append(row)



    new_content_block = f"{header}\n\n{table_header}\n" + "\n".join(table_rows) + "\n" # Add a final newline for neatness



    # Read the current content of README.md

    with open(README_FILE, "r", encoding="utf-8") as f:

        lines = f.readlines()



    # Find the start of the existing Codeforces submissions section

    # We'll replace everything from this heading onwards

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


