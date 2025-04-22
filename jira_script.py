from jira import JIRA

jira = JIRA(server="https://your-domain.atlassian.net", basic_auth=("email", "api_token"))

issue = jira.issue("PROJ-123")
print(issue.fields.summary)

# create a new issue
jira.create_issue(project="PROJ", summary="New bug", description="Something broke", issuetype={'name': 'Bug'})
