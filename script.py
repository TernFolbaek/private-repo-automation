import requests

# Your GitHub username and Personal Access Token
username = 'TernFolbaek'
token = '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'

# List of repositories to make private
repositories = ['mental-arithmetic', 'keymaster-backend', 'videos-platform','decision-trees','binary-multiclass-classification','linked-list', 'angry-chatbot','blog-backend','blog-frontend','welcome-to-open-source','linear-and-logistic-regression','language-identifier','salary-prediction-ml','facial-detection','shopping-cart']

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
