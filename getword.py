from lxml import html
import requests
page = requests.get("http://urbandictionary.com/random.php")
tree = html.fromstring(page.content)
print (tree.xpath('//a[@class="word"]/text()')[0])