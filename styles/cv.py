from pygments.style import Style
from pygments.token import Name, Comment, String, Number, Operator, Punctuation

class CVStyle(Style):
    default_style = ""
    
    black_color = "#2F2F2F"
    grey_color = "#CFCFCF"
    
    styles = {
        Comment: 'italic ' + grey_color
    }

