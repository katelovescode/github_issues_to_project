import requests

def retrieve_project(org: str, project: str, token: str) -> str:
    """
    Retrieve the project ID from the Github API
    :param org: string, organization name
    :param project: string, number of the project (found in the URL bar)
    :param token: string, authentication token from the user
    :return: string, project ID
    """
    url = 'https://api.github.com/graphql'
    json = { 'query' : '{ organization(login: "%s") { projectNext(number: %s){id title} } }' %(org, project) }
    headers = {'Authorization': 'token %s' % token}
    r = requests.post(url=url, json=json, headers=headers)
    return r.json()['data']['organization']['projectNext']