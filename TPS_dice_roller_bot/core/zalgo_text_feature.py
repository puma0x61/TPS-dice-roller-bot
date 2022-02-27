from .constants import ZALGO_CLEANER_REGEX
from .parse import clean_string_with_regex
from zalgo_text import zalgo

### zalgo_sentence(message)
# take the message text and returns a cursed sentence


def zalgo_sentence(message_text):
    message = clean_string_with_regex(message_text, ZALGO_CLEANER_REGEX)
    new_message = zalgo.zalgo().zalgofy(message)
    return new_message

