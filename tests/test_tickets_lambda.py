import unittest
from unittest.mock import patch
from tickets_lambda import create_ticket, update_ticket


class TestTicketsLambda(unittest.TestCase):

    @patch('tickets_lambda.JIRA')
    def test_create_ticket(self, mock_jira):
        # Mock JIRA instance
        mock_issue = mock_jira.return_value.create_issue.return_value
        mock_issue.key = 'TEST-123'

        # Call the create_ticket function
        result = create_ticket(
            'PROJECT-KEY', 'Test Summary', 'Test Description', 'Bug')

        # Assert the expected behavior
        self.assertEqual(result, mock_issue)
        mock_jira.assert_called_once_with(
            url='https://jira.atlassian.com', basic_auth=('username', 'API_KEY'))
        mock_jira.return_value.create_issue.assert_called_once_with(fields={
            'project': {'key': 'PROJECT-KEY'},
            'summary': 'Test Summary',
            'description': 'Test Description',
            'issuetype': {'name': 'Bug'}
        })
        print.assert_called_once_with(
            "New ticket created successfully, ticket id: TEST-123")

    @patch('tickets_lambda.JIRA')
    def test_update_ticket(self, mock_jira):
        # Mock JIRA instance
        mock_issue = mock_jira.return_value.issue.return_value

        # Call the update_ticket function
        result = update_ticket(
            'TEST-123', 'Updated Summary', 'Updated Description')

        # Assert the expected behavior
        self.assertEqual(result, mock_issue)
        mock_jira.assert_called_once_with(
            url='https://jira.atlassian.com', basic_auth=('username', 'API_KEY'))
        mock_jira.return_value.issue.assert_called_once_with('TEST-123')
        mock_issue.update.assert_called_once_with(
            summary='Updated Summary', description='Updated Description')
        print.assert_called_once_with("Ticket: TEST-123 successfully updated")


if __name__ == '__main__':
    unittest.main()
