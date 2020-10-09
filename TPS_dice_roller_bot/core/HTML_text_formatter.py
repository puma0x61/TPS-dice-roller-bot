
### Currently supperted formatting styles:
#   bold
#   italic
#   underline
#   strikethrough

STYLES = {
        'bold': [
            '<b>',
            '</b>'
            ],
        'italic': [
            '<i>',
            '</i>'
            ],
        'underline': [
            '<u>',
            '</u>'
            ],
        'strikethrough': [
            '<s>',
            '</s>'
            ]
        }
        
        
### HTML_text_formatter(text, style)
#   takes an input text and formats it in the given style for use with HTML parse mode

def HTML_text_formatter(text, style):
    formatted_text = STYLES[style][0] + text + STYLES[style][1]
    return formatted_text

