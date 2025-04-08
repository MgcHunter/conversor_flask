def split_text(text, max_length=250):
    """Splits the text into chunks smaller than the specified maximum length.

    Args:
        text (str): The text to be split.
        max_length (int): The maximum length of each chunk (default: 250).

    Returns:
        list: A list of strings, where each string is a chunk of the original text.
    """
    chunks = []
    while text:
        if len(text) <= max_length:
            chunks.append(text)
            text = ""
        else:
            cut_point = text[:max_length].rfind(' ')
            if cut_point == -1:
                chunks.append(text[:max_length])
                text = text[max_length:]
            else:
                chunks.append(text[:cut_point])
                text = text[cut_point + 1:]
    return chunks