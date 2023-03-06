# Github Public Repositories Downloader

This Python script allows you to download all the public repositories of a given user from GitHub and extract them into individual directories in a specified directory.

## Prerequisites

This script requires the following:

Python 3.x
bs4 module (for parsing HTML)
requests module (for making HTTP requests)
zipfile module (for extracting ZIP files)

You can install these modules using pip:

```bash 
pip install bs4 requests
```
## Usage

To use this script, simply replace the username variable with the GitHub username of the user whose public repositories you want to download.

Then, run the script using the following command:

``` bash
python github_repos_downloader.py
```

This will create a new directory called githubprojects (if it doesn't already exist) and download all the public repositories of the specified user into individual ZIP files in that directory. It will then extract each ZIP file into its own directory within the githubprojects directory.

## Note

This script only works for public repositories. If you want to download private repositories, you will need to provide your GitHub username and password or a personal access token with the repo scope.
