# CURRENTLY ADDED TAGS
# <h1>
# <p>
# <!-- --> (Comment)
# <a> (Link)
# <abbr> (Abbreviation)

def render_element(elem):
    t = elem.get("type")

    if t == "header":
        return f"<h1>{elem.get('text')}</h1>\n"
    elif t == "paragraph":
        return f"<p>{elem.get('text')}</p>\n"
    elif t == "comment":
        return f"<!--{elem.get('text')}-->\n"
    elif t == "link":
        return f"<a href={elem.get('url')}>{elem.get('text')}</a>\n"
    elif t == "abbreviation":
        return f"<abbr>{elem.get('text')}</abbr>"
    else:
        print(f"Skipping element with type {t}.")

def render_page(data):
    head = f"<title>{data['page'].get('title')}</title>"
    body_elements = data['page'].get('body', [])
    for elem in body_elements:
        print(f"Rendering {elem}")
    
        body = "\n".join([render_element(e) for e in body_elements])

    return f"<html>\n<head>\n{head}\n</head>\n<body>\n{body}\n</body>\n</html>"