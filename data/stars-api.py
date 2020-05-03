import json
import os
import time
from tqdm import tqdm
import requests
import pandas as pd


# STARGAZERS - GET /repos/:owner/:repo/stargazers
def get_repo_stargazers(owner, repo):
    """
    Params
    
        INPUT:
            owner: github user-name
            repo: repository-name
            
        OUTPUT:
            stargazers: list of users who have star this repo
            
    """
    
    # start with page one
    page = 1
    
    # get the url
    url = f"http://api.github.com/repos/{owner}/{repo}/stargazers?page={page}"
    response = requests.get(url)
    
    # total number of pages
    pages = int(response.links["last"]["url"].split("=")[-1])
    
    # total github user-names
    stargazers = []
    
    for page in range(1, pages + 1):
        url = f"http://api.github.com/repos/{owner}/{repo}/stargazers?page={page}"
        response = requests.get(url)
        data = response.json()
        
        # get the github-username of users
        sg = [s["login"] for s in data]
        stargazers.extend(sg)
        time.sleep(0.75)
        
    return stargazers


# STARRED REPOS
def parse_repo(repo, user):
    return {
        "user": user,
        "repo": repo["full_name"],
        "description": repo["description"],
        "language": repo["language"],
        "stargazers": repo["stargazers_count"],
    }


# List of star's repo of listed users
def get_user_stars(user):
    """
    Params

        INPUT:
            user: github-username of users

        OUTPUT:
            stars: list of star's repo of that user
    """
    page = 1
    url = f"https://api.github.com/users/{user}/starred?page={page}"
    response = requests.get(url)

    try:
        pages = int(response.links["last"]["url"].split("=")[-1])
        pages = min(pages, 10)
    except KeyError:
        pages = 1

    stars = []

    for page in range(1, pages + 1):
        url = f"https://api.github.com/users/{user}/starred?page={page}"
        response = requests.get(url)
        data = response.json()
        s = [parse_repo(r, user) for r in data]
        stars.extend(s)
        time.sleep(0.75)

    return stars



if __name__ == "__main__":

    owner = "freeCodeCamp"
    repo = "freeCodeCamp"
    stargazers = get_repo_stargazers(owner, repo)

    all_stars = []

    # for user in tqdm(stargazers):
    for user in tqdm(stargazers[:3]):
        all_stars.extend(get_user_stars(user))
        time.sleep(0.75)

    # store it in CSV format
    df = pd.DataFrame(all_stars)
    df.to_csv("data/stars.csv", encoding="utf-8", index=False)