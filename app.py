import requests


subdomain = 'fairplay9941'
user = 'codesaljones@gmail.com' + '/token'
password = 'wLPLp51AIhoU7aA7rnDuJebw3vd8dXIrFClAAWAb'

base_url = f'https://{subdomain}.zendesk.com/api/v2'

def create_ticket():
    url = base_url + '/tickets'

    ticket_data = {
        'ticket': {
            'subject': 'Ejemplo de integración',
            'comment': {
                'body': 'Este es un ejemplo de creación de un ticket desde Python'
            },
            'requester': {
                'name': 'John Doe',
                'email': 'johndoe@example.com'
            }
        }
    }

    creation_response = requests.post(url, auth=(user, password), json=ticket_data)

    if creation_response.status_code != 201:
        print('Unable to create ticket')
    else:
        print('Ticket created successfully')

def list_tickets():
    url = base_url + '/tickets'
    response = requests.get(url, auth=(user, password))

    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()

    data = response.json()

    tickets = ['{0}: {1}'.format(ticket['id'],ticket['subject']) for ticket in data['tickets']]

    print(str(tickets))

def respond():
    url = base_url + '/tickets/1'
    comment_data = {
        'ticket': {
            'comment': {
                'body': 'Esta es una respuesta random 2 al ticket desde Python'
            }
        }
    }

    creation_response = requests.put(url, auth=(user, password), json=comment_data)

    if creation_response.status_code != 200:
        print('Unable to create comment')
    else:
        print('Comment created successfully')

while True:
    command = input('Command: ')        
        
    if command == 'list':
        list_tickets()
        continue

    if command == 'create':
        create_ticket()
        continue

    if command == 'respond':
        respond()
        continue

    if command == 'exit':
        exit()

    print('Invalid Command: {0}'.format(command))
        



