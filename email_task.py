class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
    def mark_as_read(self):
        self.has_been_read = True
    def show_state(self):
        self.has_been_read = False
inbox = []
def populate_inbox():
    sample_emails = [
        ("nolonwabo@gmail.com", "Please use this email to send me messages"),
        ("nolo@gmail.com", "Please use this email to send me memes"),
        ("nm@flash.co.za", "Please uise this email to send me Professional messages")
    ]
    inbox.extend(sample_emails)
    print(sample_emails)

def list_emails():
    for i, email in enumerate(inbox):
        print(f"{i}: {email.subject_line}")
        
def read_email(index):
    try:
        email = inbox[index]
        email.mark_as_read()
        print(f"\nFrom: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")
        print(f"\nEmail from {email.email_address} marked as read.\n")
    except IndexError:
        print("Invalid index. Please try again.\n")

def view_unread_emails():
    print("\nUnread Emails:")
    has_been_read = False
    for i, email in enumerate(inbox):
        if not email.has_been_read:
            print(f"{i}: {email.subject_line}")
            has_been_read = True
    if not has_been_read:
        print("No unread emails.\n")
print(read_email)