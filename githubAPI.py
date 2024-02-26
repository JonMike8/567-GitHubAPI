import requests

def getUserHistory(user_id):
    if not isinstance(user_id, str):
        print("Input must be a string")
        return []
    user_id.strip()

    url = "https://api.github.com/users/{}/repos".format(user_id)
    response = requests.get(url)
    if response.status_code != 200:
        print("Can't fetch user data")
        return []        
    repos = response.json()
    commitsCount = []

    for repo in repos:
        repoName = repo['name']
        commitUrl = "https://api.github.com/repos/{}/{}/commits".format(user_id, repoName)
        commitResponse = requests.get(commitUrl)
        if(commitResponse.status_code != 200):
            print("Can't fetch user commit data")
            return []
        commits = commitResponse.json()
        numCommits = len(commits)
        commitsCount.append((repoName, numCommits))
    return commitsCount
