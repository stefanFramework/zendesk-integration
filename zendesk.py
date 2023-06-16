from api_client import ApiClient, ApiClientConfig
class ZendeskClient:

    def __init__(self, subdomain, user, password):
        self.base_url = f'https://{subdomain}.zendesk.com/api/v2'
        self.client = ApiClient(self._get_config(user, password))

    def _get_config(self, user, password):
        return ApiClientConfig({
            'user': user + '/token',
            'password': password
        })

    def get(self, ticket_id):
        url = self.base_url + '/tickets/' + ticket_id
        return self.client.get(url)

    def list_tickets(self):
        url = self.base_url + '/tickets'
        return self.client.get(url)
        
    def create_ticket(self, ticket_data):
        url = self.base_url + '/tickets'
        self.client.post(url, body=ticket_data)
        

    def respond_ticket(self, ticket_id, comment_data):
        url = self.base_url + '/tickets/' + ticket_id
        self.client.put(url, body=comment_data)


class ZendeskIntegrationService:
    def __init__(self,subdomain, user, password):
        self.zendesk_client = ZendeskClient(subdomain, user, password)

    def get_ticket(self, ticket_id):
        return self.zendesk_client.get(ticket_id)

    def list_tickets(self):
        return self.zendesk_client.list_tickets()
    
    def create_ticket(self, subject, body):
        ticket_data = {
            'ticket': {
                'subject': subject,
                'comment': {
                    'body': body
                }
            }
        }

        self.zendesk_client.create_ticket(ticket_data)
    
    def add_comment(self, ticket_id, comment):
        comment_data = {
            'ticket': {
                'comment': {
                    'body': comment
                }
            }
        }

        self.zendesk_client.respond_ticket(ticket_id, comment_data)
    