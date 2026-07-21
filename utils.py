import re
def clean_text(text):
    """
    Cleans extracted resume text.
    """
    # Remove extra spaces and tabs
    text = re.sub(r"\s+", " ", text)
    # Remove leading and trailing spaces
    text = text.strip()
    return text