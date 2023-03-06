import bs4
import requests
import os
import zipfile
#ur user or useron github
username = "liad07"
page = 1
repos = []
while True:
    url = f"https://api.github.com/users/{username}/repos?page={page}&per_page=100"
    response = requests.get(url)

    if response.status_code == 200:
        page_repos = response.json()
        if len(page_repos) == 0:
            break
        repos += page_repos
        page += 1
    else:
        print("Failed to retrieve user's repositories from GitHub.")
        break

# Create the directory if it doesn't exist
if not os.path.exists("githubprojects"):
    os.makedirs("githubprojects")

for project in repos:
    download_url = f"https://github.com/{username}/{project['name']}/archive/refs/heads/main.zip"
    print(f"Downloading {project['name']}...")
    response = requests.get(download_url)
    if response.status_code == 200:
        with open(f"githubprojects/{project['name']}.zip", "wb") as f:
            f.write(response.content)
        print(f"{project['name']} downloaded successfully.")

        # Extract the downloaded ZIP file
        with zipfile.ZipFile(f"githubprojects/{project['name']}.zip", "r") as zip_ref:
            zip_ref.extractall(f"githubprojects/{project['name']}")
        print(f"{project['name']} extracted successfully.")

        # Delete the original ZIP file
        os.remove(f"githubprojects/{project['name']}.zip")
        print(f"{project['name']}.zip deleted successfully.")
    else:
        print(f"Failed to download {project['name']}.")
