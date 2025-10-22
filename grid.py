import re
import urllib.request
import html


def _fetch_url(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read().decode(errors="ignore")


def _html_to_text(html_src):
    html_src = re.sub(r"(?is)<(script|style).*?>.*?</\1>", "", html_src)
    html_src = re.sub(r"(?i)</(td|th|tr|p|div|br|li|h[1-6])>", "\n", html_src)
    return html.unescape(re.sub(r"(?s)<.*?>", "", html_src))


def _tokens_from_text(text):
    pattern = re.compile(r"\d+|[^\s\d]", flags=re.UNICODE)
    return pattern.findall(text)


def _triplets_from_tokens(tokens):
    triplets = []
    i = 0
    n = len(tokens)
    while i + 2 < n:
        a, b, c = tokens[i], tokens[i + 1], tokens[i + 2]
        if re.fullmatch(r"\d+", a) and not re.fullmatch(r"\d+", b) and re.fullmatch(r"\d+", c):
            triplets.append((int(a), b, int(c)))
            i += 3
            continue
        i += 1
    return triplets


def print_doc_grid():
    url = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"
    html_src = _fetch_url(url)
    text = _html_to_text(html_src)
    tokens = _tokens_from_text(text)
    triplets = _triplets_from_tokens(tokens)
    if not triplets:
        lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
        for i in range(len(lines) - 2):
            if re.fullmatch(r"\d+", lines[i]) and re.fullmatch(r"\d+", lines[i + 2]) and len(lines[i + 1]) >= 1:
                triplets.append(
                    (int(lines[i]), lines[i + 1][0], int(lines[i + 2])))
    grid = {}
    max_x = max_y = 0
    for x, ch, y in triplets:
        grid[(x, y)] = ch
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    for y in range(max_y + 1):
        row = [grid.get((x, y), " ") for x in range(max_x + 1)]
        print("".join(row))


if __name__ == "__main__":
    print_doc_grid()
