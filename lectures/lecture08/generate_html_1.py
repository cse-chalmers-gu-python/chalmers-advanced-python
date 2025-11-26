# String-based HTML generation

def in_tag(tag, elem, attrs=''):
  return f'<{tag} {attrs}>{elem}</{tag}>'

def a(elem, href, attrs=''):
  return in_tag('a', elem, f'href="{href}"' + attrs)

# ---

doc = \
  in_tag('h3', '9.2 URLs') + '\n' +\
  in_tag('p',
    'You know what a URL is!' +
    in_tag('strong', 'URL') +
    'stands for' +
    in_tag('strong',
      in_tag('u', 'U') + 'niform ' +
      in_tag('u', 'R') + 'esource ' +
      in_tag('u', 'L') + 'ocator.'
    )
  )

doc += in_tag('pre', in_tag('code', 'https://www.example.com/cat/?foo=bar+hex', 'class="language-plain"'))

doc += in_tag('p', 
  'A more complete desription can be found at ' +
  a('Wikipedia', href='https://en.wikipedia.org/wiki/URL')
)

print(doc)
