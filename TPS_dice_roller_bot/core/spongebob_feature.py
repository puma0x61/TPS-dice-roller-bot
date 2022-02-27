from .constants import SPONGEBOB_CLEANER_REGEX
from .parse import clean_string_with_regex


### spongebob_sentence_flow_decider(message)
# take the message and decides the desired behaviour

def spongebob_sentence_flow_decider(message):
    message_text = message_cleaner(message.text)
    if len(message_text) != 0:
        sentence = spongebob_sentence(message_text)
    else:
        message_reply_to_message = message.reply_to_message.text
        sentence = spongebob_sentence(message_reply_to_message)

    return sentence


### spongebob_sentence(message)
# take the message text and returns a sentence with alternating upper and lowercase chars


def spongebob_sentence(message_text):
    message_split = message_cleaner(message_text)
    message_split_list = message_split.split(' ')
    new_message = ""

    # takes every string in the list
    for string in message_split_list:
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


def message_cleaner(message_text):
    cleaned_message = clean_string_with_regex(message_text, SPONGEBOB_CLEANER_REGEX)
    return cleaned_message
