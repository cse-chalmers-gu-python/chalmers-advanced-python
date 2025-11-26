# Parser which finds all content inside <strong> tags

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  def __init__(self):
    super().__init__()
    self.strongs = []
    self.in_strong = False
    self.buffer = ""

  def handle_starttag(self, tag, attrs):
    if tag == "strong":
      self.in_strong = True

  def handle_endtag(self, tag):
    if tag == "strong":
      self.in_strong = False
      if self.buffer:
        self.strongs.append(self.buffer)
        self.buffer = ""

  def handle_data(self, data):
    if self.in_strong:
      self.buffer += data

with open('basic.html') as f:
  parser = MyHTMLParser()
  parser.feed(f.read())
  print(parser.strongs)
