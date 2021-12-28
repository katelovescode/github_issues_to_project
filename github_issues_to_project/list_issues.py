import requests

def list_issues(token: str, org: str, repo: str, cursor: str = None, status: str = None, label: str = None) -> list:
    """
    Retrieve a list of issues from the Github API filtered by status or label or both
    :param status: string, status to filter issues by, [open, close], [default: open]
    :param label: string, label to filter issues by
    :param token: string, authentication token from the user
    :param org: string, organization name
    :param repo: string, repository name
    :param cursor: string, issue ID from which to start the next search
    :return: list, issue IDs matching the filtered parameters
    """
    url = 'https://api.github.com/graphql'

    filtered = label != None or status != None

    if filtered:
      label_filter = "%s" %("labels: [%s]" % label if label != None else "")
      states_filter = "%s" %("states: [%s]" % status.upper() if status != None else "")
      filter_value = "filterBy: {%s%s}, " % (label_filter, states_filter)
    
    cursor_value = "%s" %(", after: %s" % cursor if cursor != None else "")

    json = { 'query' : '{ organization(login: "%s") { repository(name: "%s") { issues(%sfirst: 30%s) { nodes { id title number state } } } } }' %(org, repo, filter_value, cursor_value) }
    headers = {'Authorization': 'token %s' % token}
    r = requests.post(url=url, json=json, headers=headers)
    return r.json()['data']['organization']['repository']['issues']['nodes']