import pywhatkit

# Read contacts from contacts.txt
with open('contacts.txt', 'r') as f:
    contacts = [line.strip() for line in f if line.strip()]

# Read message from message.txt
with open('message.txt', 'r') as f:
    message = f.read().strip()

# Send the message to each contact
for number in contacts:
    pywhatkit.sendwhatmsg_instantly(
        number,
        message,
        wait_time=10,
        tab_close=True
    )
    print(f'Message sent to {number}')
