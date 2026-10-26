# Class-based HTML generation

class Node:
  def __init__(self, tag, elems=[], attrs={}):
    self._tag = tag
    self._elems = elems
    self._attrs = attrs

  def render(self):
    if attrs := self._attrs:
        attrs = f" {' '.join([f'{key}={value}' for key, value in attrs.items()])}"
    else:
        attrs = ""
    start = f'<{self._tag}{attrs}>'
    content = "\n".join([
      elem.render() if isinstance(elem, Node) else elem
      for elem in self._elems
    ])
    end = f'</{self._tag}>'
    return start + content + end

class Anchor(Node):
  def __init__(self, url, elems=[], attrs={}):
    self._tag = 'a'
    self._elems = elems
    self._attrs = {**attrs, 'href': url}

doc = Node('html', [
  Node('h3', ['9.2 URLs']),
  Node('p', [
    'You know what a',
    Node('strong', ['URL']),
    'is!',
    'A more complete desription can be found at ',
    Anchor('https://en.wikipedia.org/wiki/URL', ['Wikipedia'])
  ])
])
print(doc.render())
