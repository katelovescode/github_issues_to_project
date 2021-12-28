import requests

def add_issues_to_project(org: str, projectnum: str, token: str) -> str:
    """
    Sum two numbers together
    :param var1: any integer
    :param var2: any integer
    :return: sum of the passed paramters
    """
    url = 'https://api.github.com/graphql'
    json = { 'query' : '{ organization(login: "%s") { projectNext(number: %s){id} } }' %(org, projectnum) }
    headers = {'Authorization': 'token %s' % token}
    r = requests.post(url=url, json=json, headers=headers)
    project_id = r.json()['data']['organization']['projectNext']['id']
    print(org)
    print(projectnum)
    print(project_id)