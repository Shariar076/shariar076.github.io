"""Convert LessWrong ```widget[id] fences in a post into iframes backed by assets/widgets/<id>.html."""
import os
import re
import sys

post = sys.argv[1]
out = "assets/widgets"
os.makedirs(out, exist_ok=True)

HEAD = '<!doctype html>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n'
IFRAME = ('<iframe src="/assets/widgets/{id}.html" class="lw-widget" loading="lazy" scrolling="no" '
          'style="width:100%;border:0;height:400px" '
          'onload="var d=this.contentDocument;this.style.height=(d.documentElement.scrollHeight+4)+\'px\'"></iframe>')


def convert(m):
    wid, body = m.group(1), m.group(2)
    with open(f"{out}/{wid}.html", "w") as w:
        w.write(HEAD + body)
    return IFRAME.format(id=wid)


with open(post) as r:
    text = r.read()
text, n = re.subn(r"```widget\[(\w+)\]\n(.*?)\n```", convert, text, flags=re.S)
with open(post, "w") as w:
    w.write(text)
print(f"converted {n} widgets")
