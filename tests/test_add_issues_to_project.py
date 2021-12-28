from github_issues_to_project import add_issues_to_project

def test_sum():
  assert sum([1, 2, 3]) == 6, "should be 6"

def test_add_issues():
    assert add_issues_to_project.add_issues(12, 3) == 15
