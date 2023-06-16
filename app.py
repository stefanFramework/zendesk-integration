import os

from dotenv import load_dotenv

from zendesk import ZendeskIntegrationService

load_dotenv()

subdomain = os.getenv('ZENDESK_DOMAIN')
user = os.getenv('ZENDESK_USER')
password = os.getenv('ZENDESK_PASSWORD')

service = ZendeskIntegrationService(
    subdomain,
    user, 
    password
)

while True:
    command = input('Command: ')        
        
    if command == 'list':
        print(service.list_tickets())
        continue

    if command == 'create':
        subject = input('Subject: ')
        body = input('Body: ')
        service.create_ticket(subject=subject, body=body)
        continue

    if command == 'get':
        ticket_id = input('Ticket ID: ')
        print(service.get_ticket(ticket_id))
        continue

    if command == 'respond':
        ticket_id = input('Ticket ID: ')
        comment = input('Comment: ')
        service.add_comment(ticket_id, comment)
        continue

    if command == 'exit':
        exit()

    print('Invalid Command: {0}'.format(command))
        



