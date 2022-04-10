import pywhatkit

# Send a WhatsApp Message to a Contact at 00:00 AM (default delay is 15 seconds)
pywhatkit.sendwhatmsg('<Receiver WhatsApp number with country code>','<your message>', 00, 00)

# Send a WhatsApp Message to a Contact at 00:00 AM with 30 seconds delay and Closes the Tab in 2 Seconds after Sending the Message
pywhatkit.sendwhatmsg("<Receiver WhatsApp number with country code>", "<your message>", 00, 00, 30, True, 2)

# Send an Image to a Contact with the Caption in 30 seconds delay
pywhatkit.sendwhats_image("<Receiver WhatsApp number with country code>", "images/sample.jpg", "<caption>", 30)



