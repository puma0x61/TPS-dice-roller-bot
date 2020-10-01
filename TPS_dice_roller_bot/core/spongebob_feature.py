### spongebob_sentence(message)
# take the message text and returns a sentence with alternating upper and lowercase chars

def spongebob_sentence(message_text):
    message_split = message_text.split()

    if '/spongebob' in message_split:
        message_split = message_split[message_split.index('/spongebob') + 1:len(message_split)]
    elif '/sp' in message_split:
        message_split = message_split[message_split.index('/sp') + 1:len(message_split)]
    else:
        message_split = message_split[0:len(message_split)]

    new_message = ""

    # takes every string in the list
    for string in message_split:
        i = 0
        # takes every char in string and iterate counting the element index
        for char in string:
            if i % 2 == 0:
                new_message += char.upper()
            else:
                new_message += char.lower()
            i += 1
        new_message += ' '

    return new_message