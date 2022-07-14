class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: " \
               f"{self.content}. Sent: {self.is_sent}"

    def send(self):
        self.is_sent = True


message = input()
emails_data = []
while not message == 'Stop':
    details = message.split(' ')
    sender = details[0]
    receiver = details[1]
    content = details[2]
    all_info = Email(sender, receiver, content)
    emails_data.append(all_info)
    message = input()

sent_emails = list(map(int, input().split(', ')))

for x in sent_emails:
    emails_data[x].send()

for email in emails_data:
    print(email.get_info())


