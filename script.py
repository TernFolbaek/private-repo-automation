import requests

# Your GitHub username and Personal Access Token
username = 'TernFolbaek'
token = 'PAT'

# List of repositories to make private
repositories = ['repo1','repo2','repo3']

# API URL
api_url = 'https://api.github.com/repos/'

# Headers for authentication
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Loop through each repository and change its visibility
for repo in repositories:
    data = {'private': True}
    response = requests.patch(f'{api_url}{username}/{repo}', json=data, headers=headers)
    if response.status_code == 200:
        print(f'Repository {repo} is now private.')
    else:
        print(f'Failed to change repository {repo}. Status code: {response.status_code}')
