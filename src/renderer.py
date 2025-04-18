def render_element(elem):
    t = elem.get("type")

    if t == "header":
        return f"<h1>{elem.get('text')}</h1>\n"
    elif t == "paragraph":
        return f"<p>{elem.get('text')}</p>\n"
    elif t == "comment":
        return f"<!--{elem.get('text')}-->\n"
    elif t == "hyperlink":
        return f"<a href=\"{elem.get('url')}\">{elem.get('text')}</a>\n"
    elif t == "abbreviation":
        return f"<abbr>{elem.get('text')}</abbr>\n"
    elif t == "script":
        return f"<script src=\"{elem.get('src')}\"></script>\n"
    elif t == "button":
        return f"<button onclick=\"{elem.get('on_click')}\">{elem.get('text')}</button>\n"
    elif t == "link":
        return f"<link rel=\"{elem.get('rel')}\" href=\"{elem.get('href')}\">"
    else:
        print(f"Skipping unknown element type: {t}")
        return ""


def render_page(data):
    head = f"<title>{data['page'].get('title')}</title>"
    body_elements = data['page'].get('body', [])

    for elem in body_elements:
        print(f"Rendering: {elem}")

    body = "\n".join([render_element(e) for e in body_elements])

    return f"<html>\n<head>\n{head}\n</head>\n<body>\n{body}\n</body>\n</html>"
