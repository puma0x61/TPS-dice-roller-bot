import re


### parse_text(text)
# takes a string, return a list of strings with the matching groups

def parse_text_regex(text, regex):
    try:
        compiled_regex = re.compile(regex)
        if compiled_regex is None:
            raise Exception(f"String {text} doesn't match {regex}")
    except TypeError as te:
        raise Exception(te)
    except Exception as e:
        raise e
    match = compiled_regex.match(text)
    return match.groups()
