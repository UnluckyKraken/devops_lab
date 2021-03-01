import requests

per_page = {'per_page': '100'}
token = {'Authorization': 'access_token TOKEN'}
repo_url = 'https://api.github.com/repos/alenaPy/devops_lab/pulls'
search_url_acpt = 'https://api.github.com/search/issues?q=is:pr%20label:"accepted"\
                   %20repo:alenaPy/devops_lab&per_page=100'
search_url_nw = 'https://api.github.com/search/issues?q=is:pr%20label:"needs%20work"\
                 %20repo:alenaPy/devops_lab&per_page=100'


def get_pulls(state):
    pull = requests.get(repo_url, headers=token)

    if state == "closed" or state == "open":
        pull = requests.get(repo_url, headers=token,
                            params={'state': '{0}'.format(state), 'per_page': '100'})

    if state == "needs work":
        pull = requests.get(search_url_nw, headers=token, params=per_page)
        return pull.json()["items"]

    if state == "accepted":
        pull = requests.get(search_url_acpt, headers=token, params=per_page)
        return pull.json()["items"]

    return pull.json()
