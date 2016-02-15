from lxml import html
import requests
web_page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
dta = html.fromstring(page.content)
div title="buyer-name">Carson Busses</div>
<span class = "item-price">29.95</span>
buyers = dta.xpath('//div[@title="buyer-name"]/text()')
prices = dta.xpath('//span[@class="item-price"]/text()')
print 'Buyers: ', buyers
print 'Prices: ', prices
