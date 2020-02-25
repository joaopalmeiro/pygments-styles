from pygments.style import Style
from pygments.token import Name, Comment, String, Number, Operator, Punctuation, Keyword

class CVStyle(Style):
    default_style = ""
    
    black_color = "#2F2F2F"
    grey_color = "#CFCFCF"
    
    styles = {
        Comment: 'italic ' + grey_color,

        Punctuation: black_color,
        Number: black_color,
        Operator: black_color,
        Name: black_color,
        String: black_color,
        Keyword: black_color   
    }

