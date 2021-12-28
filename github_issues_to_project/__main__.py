from optparse import OptionParser
from getpass import getpass

from retrieve_project import retrieve_project
from list_issues import list_issues
import os

def main():
  parser = OptionParser(usage='Usage: %prog [-o] [-p] [-l] [-s]') # TODO: add version dynamically
  parser.add_option("-o", "--org", dest="organization_name", help="The organization name where the project lives")
  parser.add_option("-r", "--repo", dest="repository", help="The repository name where the issues live")
  parser.add_option("-p", "--project", dest="project_number", help="The ID number of the project (found in the URL bar)")
  parser.add_option("-l", "--label", dest="label", help="[Optional] The label to filter issues by")
  parser.add_option("-s", "--status", dest="status", help="[Optional] The status to filter issues by: open, closed [default: %default]", default="open")
  (options, args) = parser.parse_args()

  token = os.getenv('GITHUB_TOKEN') if os.getenv('GITHUB_TOKEN') != None else getpass() # TODO: or get environment variable
  org = options.organization_name
  project = options.project_number
  repo = options.repository
  status = options.status
  label = options.label

  project = retrieve_project(org=org, project=project, token=token)
  issues = list(map(print_issue, list_issues(token=token, org=org, repo=repo, status=status, label=label)))

  print("\nThe following issues will be moved: \n", *issues, sep="\n")


  confirmation = input("\nAre you sure you want to add these issues to project \"%s\"? [Y/N] " % project['title'])

  if confirmation == "Y" or confirmation == "y":
    # TODO: loop through issues and move 'em
    # TODO: pagination
    print("Gonna do this thing")
  else:
    print("No issues will be added to \"%s\".  Exiting." % project['title'])

def print_issue(issue: dict) -> None:
  return "[%s] %s (%s) - [%s]" % (issue['number'], issue['title'], issue['id'], issue['state'])

if __name__ == '__main__':
    main()