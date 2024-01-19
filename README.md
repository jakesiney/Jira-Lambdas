# JIRA Ticket Management with Python

This project contains a Python script that interacts with the JIRA API to create and update tickets.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have the Python Jira library installed.

### Installing

1. Clone the repository:
    ```
    git clone <repository_url>
    ```

2. Navigate to the project directory:
    ```
    cd <project_directory>
    ```

3. Install the project dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage

The script `tickets-lambda.py` contains two main functions:

- `create_ticket(project, summary, description, issue_type)`: This function creates a new JIRA ticket.
- `update_ticket(ticket_id, summary, description)`: This function updates an existing JIRA ticket.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License.

