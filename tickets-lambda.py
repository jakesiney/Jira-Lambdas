import os
from atlassian import JIRA
from dotenv import load_dotenv


load_dotenv()

os.getenv('API_KEY')

jira = JIRA(url='https://jira.atlassian.com',
            basic_auth=('username', os.getenv('API_KEY')))


def create_ticket(project, summary, description, issue_type):
    fields = {
        'project': {'key': project},
        'summary': summary,
        'description': description,
        'issuetype': {'name': issue_type},
    }
    new_issue = jira.create_issue(fields=fields)
    print(f"Created new ticket: {new_issue.key}")
    return new_issue


def update_ticket(ticket_id, summary, description):
    issue = jira.issue(ticket_id)
    issue.update(
        summary=summary,
        description=description,
    )
    print(f"Ticket: {issue.key} successfully updated")
    return issue
