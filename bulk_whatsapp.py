import pywhatkit

contacts = ['+918555917481', '+919000408182']
message = "Hello, this is a bulk message!"     # Your message

for number in contacts:
    pywhatkit.sendwhatmsg_instantly(
        number,
        message,
        wait_time=10,      # Wait time before sending each message
        tab_close=True     # Close tab after sending
    )
    print(f'Message sent to {number}')
