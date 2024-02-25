import requests
#import json

def getUserHistory(user_id):
    if not isinstance(user_id, str):
        print("Input must be a string")
        return []
    user_id.strip

    url = f"https://api.github.com/users/{user_id}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        print("Can't fetch user data")
        return []        
    repos = response.json()
    #print(repos)
    commitsCount = []

    for repo in repos:
        repoName = repo['name']
        commitUrl = f"https://api.github.com/repos/{user_id}/{repoName}/commits"
        commitResponse = requests.get(commitUrl)
        if(response.status_code != 200):
            print("Can't fetch user commit data")
            return []
        commits = commitResponse.json()
        numCommits = len(commits)
        commitsCount.append((repoName, numCommits))
    return commitsCount

