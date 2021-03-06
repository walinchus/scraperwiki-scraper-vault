#Esempio recupero elenco aziende

import scraperwiki
import lxml.html
from urllib import urlencode
import json
import re

# Tutorial Data Extraction

def get_text(el, class_name):
    els = el.find_class(class_name)
    if els:
        return els[0].text_content()
    else:
        return ''

def get_href(el, class_name):
    els = el.find_class(class_name)
    if els:
        return els[0].get('href')
    else:
        return ''

def get_value(el):
    return get_text(el, 'value') or el.text_content()

def get_all_texts(el, class_name):
    return [e.text_content() for e in els.find_class(class_name)]

def parse_addresses(el):
    return el.find_class('adr')


html = scraperwiki.scrape("http://www.paginegialle.it/pgol/4-web%20agency?mr=50")
print html
root = lxml.html.fromstring(html)

li = {}

companies = []
name = []
url = []
address = []
locality = []
website = []
tel = []
email = []
category = []


for el in root.xpath("//a[@class='_lms _noc']/@href"):url.append(el)

for el in root.cssselect("div.org"):
    name.append (get_text (el,"rgs"))

for el in root.cssselect("div.address"):
    address.append (get_text (el,"street-address"))

for el in root.cssselect("div.address"):
    locality.append (get_text (el,"locality"))

for el in root.cssselect("div.tel"):
    tel.append (get_text (el,"tel") )

for el in root.cssselect("div.link"):
    website.append (get_href (el,"_noc") )  

for el in root.cssselect("div.text"):
    category.append (get_text (el,"snippet") )  

i = 0
for el in root.cssselect("div.org"):
    print 'Name ', name[i]
    print 'Address ', address[i]
    print 'Locality ', locality[i]
    print 'Tel', tel[i]    
    print 'Website', website[i]
    print 'Category', category[i]
    urlemail = ''.join(( url[i], '/contatto?lt=frag'))
    print urlemail
    htmlEmail =  scraperwiki.scrape(urlemail)
    print htmlEmail
    rootEmail = lxml.html.fromstring(htmlEmail)
    for el in rootEmail.xpath("//input[@name='multimail']/@value"):email.append (el)
    print 'Email', email[i]
    li['CompanyName'] = name[i].upper().replace("\n","")
    li['Address'] = address[i].upper().replace("\n","")
    li['Locality'] = locality[i].upper().replace("\n","")
    li['Tel'] = tel[i].upper().replace("\n","")
    li['WebSite'] = website[i].lower().replace("\n","")
    li['Category'] = category[i].upper().replace("\n","")
    li['Email'] = email[i].upper().replace("\n","")
    scraperwiki.sqlite.save(unique_keys=['CompanyName'], data=li)
    i = i + 1

#Fine Recupero elenco aziende
#Esempio recupero elenco aziende

import scraperwiki
import lxml.html
from urllib import urlencode
import json
import re

# Tutorial Data Extraction

def get_text(el, class_name):
    els = el.find_class(class_name)
    if els:
        return els[0].text_content()
    else:
        return ''

def get_href(el, class_name):
    els = el.find_class(class_name)
    if els:
        return els[0].get('href')
    else:
        return ''

def get_value(el):
    return get_text(el, 'value') or el.text_content()

def get_all_texts(el, class_name):
    return [e.text_content() for e in els.find_class(class_name)]

def parse_addresses(el):
    return el.find_class('adr')


html = scraperwiki.scrape("http://www.paginegialle.it/pgol/4-web%20agency?mr=50")
print html
root = lxml.html.fromstring(html)

li = {}

companies = []
name = []
url = []
address = []
locality = []
website = []
tel = []
email = []
category = []


for el in root.xpath("//a[@class='_lms _noc']/@href"):url.append(el)

for el in root.cssselect("div.org"):
    name.append (get_text (el,"rgs"))

for el in root.cssselect("div.address"):
    address.append (get_text (el,"street-address"))

for el in root.cssselect("div.address"):
    locality.append (get_text (el,"locality"))

for el in root.cssselect("div.tel"):
    tel.append (get_text (el,"tel") )

for el in root.cssselect("div.link"):
    website.append (get_href (el,"_noc") )  

for el in root.cssselect("div.text"):
    category.append (get_text (el,"snippet") )  

i = 0
for el in root.cssselect("div.org"):
    print 'Name ', name[i]
    print 'Address ', address[i]
    print 'Locality ', locality[i]
    print 'Tel', tel[i]    
    print 'Website', website[i]
    print 'Category', category[i]
    urlemail = ''.join(( url[i], '/contatto?lt=frag'))
    print urlemail
    htmlEmail =  scraperwiki.scrape(urlemail)
    print htmlEmail
    rootEmail = lxml.html.fromstring(htmlEmail)
    for el in rootEmail.xpath("//input[@name='multimail']/@value"):email.append (el)
    print 'Email', email[i]
    li['CompanyName'] = name[i].upper().replace("\n","")
    li['Address'] = address[i].upper().replace("\n","")
    li['Locality'] = locality[i].upper().replace("\n","")
    li['Tel'] = tel[i].upper().replace("\n","")
    li['WebSite'] = website[i].lower().replace("\n","")
    li['Category'] = category[i].upper().replace("\n","")
    li['Email'] = email[i].upper().replace("\n","")
    scraperwiki.sqlite.save(unique_keys=['CompanyName'], data=li)
    i = i + 1

#Fine Recupero elenco aziende
