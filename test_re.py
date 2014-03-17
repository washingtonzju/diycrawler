import re

content = u"<script>\n(adsbygoogle = window.adsbygoogle || []).push({});\n</script>"
ans = re.sub(r"<script>\n.+\n</script>", u"", content, 100, re.MULTILINE)

print content
print ans

