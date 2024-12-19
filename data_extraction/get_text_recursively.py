def get_text_from_span_element(element):
    """outcome1: there is another span ---> make a recursively call to dig deeper
    outcome2: this span contains the text element --> get the text element and return
    outcome3: this span is a None --> return
"""
    if element == None:
        return ""
    if element.name == 'span':
        text = element.get_text(strip=True)
        if text:
            return text
        
    for child in element.children:
        if isinstance(child, str):
            continue
        result = get_text_from_span_element(child)
        if result:
            return result
    # if no string is found 
    return ""