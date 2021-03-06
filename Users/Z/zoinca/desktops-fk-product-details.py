import scraperwiki

# Blank Python

import re
import urllib2

#url = "http://www.flipkart.com/samsung-np300e5z-s08in-laptop-2-gen-ci5-4gb-750gb-1gb/p/itmd8dhnybfbngtu?pid=COMD8DHN7KUCHY33&ref=75e3ea45-0bfa-417d-a7b3-a4e7ad95924d"
#url="http://www.flipkart.com/dell-inspiron-5050-laptop-2nd-gen-ci3-4gb-500gb-win7-hb/p/itmd9pf6f7rhvjhe?pid=COMD9PEWRZA4H2VZ&ref=12dde97b-50e4-4e90-8065-a9fd1e819bc2"
#url = "http://www.flipkart.com/sony-vaio-sve15113en-laptop-2nd-gen-ci3-2gb-320gb-win7-hb/p/itmdatb5fzya689a?pid=COMDATB57ER5ZRBH&ref=12dde97b-50e4-4e90-8065-a9fd1e819bc2"

scraperwiki.sqlite.attach('laptops-fk-products-urls_1',"urls")
urls = scraperwiki.sqlite.select('* from urls.swdata')

for url in urls:
 listurl = url.values()
 pagelink = listurl[0]
 open = urllib2.urlopen(pagelink)
 lines = str(open.read())

 match_title = re.search(r'(h1\s+itemprop="name"\s+title=")(\w+)([+.,\\\'\(\)\"\w\d\s&-/]+)(">)',lines)
 if match_title:
  print match_title.group(2)
  brand = match_title.group(2)
  print match_title.group(2)+match_title.group(3)
  title = match_title.group(2)+match_title.group(3)

 match_rating = re.search(r'(ratingCount".{0,5}>)(\d+)',lines)
 if match_rating:
  print match_rating.group(2)
  rating = match_rating.group(2)

 match_reviews = re.search(r'(reviewCount.{0,5}>)(\d+)',lines)
 if match_reviews:
  print match_reviews.group(2)
  reviews = match_reviews.group(2)

 match_price = re.search(r'(<span class="price final-price our fksk-our" id="fk-mprod-our-id">Rs.<span class="small-font"> </span>)(\d+)',lines)
 if match_price:
  print match_price.group(2)
  price = match_price.group(2)

 match_stock = re.search(r'(id="fk-stock-info-id">)(\w+)',lines)
 if match_stock:
  print match_stock.group(2)
  stock = match_stock.group(2)
  if stock=='Available':
   stock = 'In'

 match_delivery = re.search(r'(<span class="boldtext">)(\d-\d)',lines)
 if match_delivery:
  print match_delivery.group(2)
  delivery =  match_delivery.group(2)

 match_specs_processor = re.search(r'(specs-key">Processor[\W]+.{0,100})([\W]+)(.{0,100}">)([\(\)\w\s\d-]+)(</td>)',lines)
 if match_specs_processor:
  print match_specs_processor.group(4)
  specs_processor = match_specs_processor.group(4)
 
 match_specs_variant = re.search(r'(specs-key">Variant[\W]+.{0,100})([\W]+)(.{0,100}">)([\(\)\w\s\d-]+)(</td>)',lines)
 if match_specs_variant:
  print match_specs_variant.group(4)
  specs_variant = match_specs_variant.group(4)

 match_specs_processorbrand = re.search(r'(specs-key">Brand[\W]+.{0,100})([\W]+)(.{0,100}">)([\(\)\w\s\d-]+)(</td>)',lines)
 if match_specs_processorbrand:
  print match_specs_processorbrand.group(4)
  specs_processorbrand = match_specs_processorbrand.group(4)

 match_specs_clockspeed = re.search(r'(specs-key">Clock Speed[\W]+.{0,100})([\W]+)(.{0,100}">)([.\(\)\w\s\d-]+)(</td>)',lines)
 if match_specs_clockspeed:
  print match_specs_clockspeed.group(4)
  specs_clockspeed = match_specs_clockspeed.group(4)
  match_clockspeed = re.findall('[.\d]+',specs_clockspeed)
  for match in match_clockspeed:
   clockspeed = match

 match_specs_ram = re.search(r'(specs-key">System Memory[\W]+.{0,100})([\W]+)(.{0,100}">)([.\(\)\w\s\d-]+)(</td>)',lines)
 if match_specs_ram:
  print match_specs_ram.group(4)
  ram = match_specs_ram.group(4)
  match_ram = re.search(r'\d+',ram)
  if match_ram:
   ram = match_ram.group()

 match_specs_hd = re.search(r'(specs-key">HDD Capacity[\W]+.{0,100})([\W]+)(.{0,100}">)([.\(\)\w\s\d-]+)(</td>)',lines)
 if match_specs_hd:
  print match_specs_hd.group(4)
  hd = match_specs_hd.group(4)
  match_hd = re.search(r'\d+',hd)
  if match_hd:
   hd = match_hd.group()
 

 match_specs_os = re.search(r'(specs-key">Operating System[\W]+.{0,100})([\W]+)(.{0,100}">)([.\(\)\w\s\d-]+)(</td>)',lines)
 if match_specs_os:
  print match_specs_os.group(4)
  os = match_specs_os.group(4)

 match_specs_backup = re.search(r'(specs-key">Battery Backup[\W]+.{0,100})([\W]+)(.{0,100}">)([.\(\)\w\s\d-]+)(</td>)',lines)
 if match_specs_backup:
  print match_specs_backup.group(4)
  specs_backup = match_specs_backup.group(4)

 scraperwiki.sqlite.save(['url'],data={'url':pagelink,'brand':brand,'title':title,'rating':rating,'reviews':reviews,'price':price,'stock':stock,'delivery':delivery,'specs-processor':specs_processor,'variant':specs_variant,'procband':specs_processorbrand,'clockspeed':clockspeed,'ram':ram,'hd':hd,'os':os})


#<span class="boldtext">2-4 business days.</span>
#<div class="stock-status instock" id="fk-stock-info-id">In Stock.</div>
#<span class="price final-price our fksk-our" id="fk-mprod-our-id">Rs.<span class="small-font"> </span>37588</span>
#<a href="#read-reviews"><span itemprop="reviewCount">64</span> Reviews</a>
#<span itemprop="ratingCount">171</span>
#<h1 itemprop="name" title="Samsung NP300E5Z-S08IN Laptop 2 Gen Ci5/4GB/750GB/1GB">Samsung NP300E5Z-S08IN Laptop 2 Gen Ci5/4GB/750GB/1GB</h1>import scraperwiki

# Blank Python

import re
import urllib2

#url = "http://www.flipkart.com/samsung-np300e5z-s08in-laptop-2-gen-ci5-4gb-750gb-1gb/p/itmd8dhnybfbngtu?pid=COMD8DHN7KUCHY33&ref=75e3ea45-0bfa-417d-a7b3-a4e7ad95924d"
#url="http://www.flipkart.com/dell-inspiron-5050-laptop-2nd-gen-ci3-4gb-500gb-win7-hb/p/itmd9pf6f7rhvjhe?pid=COMD9PEWRZA4H2VZ&ref=12dde97b-50e4-4e90-8065-a9fd1e819bc2"
#url = "http://www.flipkart.com/sony-vaio-sve15113en-laptop-2nd-gen-ci3-2gb-320gb-win7-hb/p/itmdatb5fzya689a?pid=COMDATB57ER5ZRBH&ref=12dde97b-50e4-4e90-8065-a9fd1e819bc2"

scraperwiki.sqlite.attach('laptops-fk-products-urls_1',"urls")
urls = scraperwiki.sqlite.select('* from urls.swdata')

for url in urls:
 listurl = url.values()
 pagelink = listurl[0]
 open = urllib2.urlopen(pagelink)
 lines = str(open.read())

 match_title = re.search(r'(h1\s+itemprop="name"\s+title=")(\w+)([+.,\\\'\(\)\"\w\d\s&-/]+)(">)',lines)
 if match_title:
  print match_title.group(2)
  brand = match_title.group(2)
  print match_title.group(2)+match_title.group(3)
  title = match_title.group(2)+match_title.group(3)

 match_rating = re.search(r'(ratingCount".{0,5}>)(\d+)',lines)
 if match_rating:
  print match_rating.group(2)
  rating = match_rating.group(2)

 match_reviews = re.search(r'(reviewCount.{0,5}>)(\d+)',lines)
 if match_reviews:
  print match_reviews.group(2)
  reviews = match_reviews.group(2)

 match_price = re.search(r'(<span class="price final-price our fksk-our" id="fk-mprod-our-id">Rs.<span class="small-font"> </span>)(\d+)',lines)
 if match_price:
  print match_price.group(2)
  price = match_price.group(2)

 match_stock = re.search(r'(id="fk-stock-info-id">)(\w+)',lines)
 if match_stock:
  print match_stock.group(2)
  stock = match_stock.group(2)
  if stock=='Available':
   stock = 'In'

 match_delivery = re.search(r'(<span class="boldtext">)(\d-\d)',lines)
 if match_delivery:
  print match_delivery.group(2)
  delivery =  match_delivery.group(2)

 match_specs_processor = re.search(r'(specs-key">Processor[\W]+.{0,100})([\W]+)(.{0,100}">)([\(\)\w\s\d-]+)(</td>)',lines)
 if match_specs_processor:
  print match_specs_processor.group(4)
  specs_processor = match_specs_processor.group(4)
 
 match_specs_variant = re.search(r'(specs-key">Variant[\W]+.{0,100})([\W]+)(.{0,100}">)([\(\)\w\s\d-]+)(</td>)',lines)
 if match_specs_variant:
  print match_specs_variant.group(4)
  specs_variant = match_specs_variant.group(4)

 match_specs_processorbrand = re.search(r'(specs-key">Brand[\W]+.{0,100})([\W]+)(.{0,100}">)([\(\)\w\s\d-]+)(</td>)',lines)
 if match_specs_processorbrand:
  print match_specs_processorbrand.group(4)
  specs_processorbrand = match_specs_processorbrand.group(4)

 match_specs_clockspeed = re.search(r'(specs-key">Clock Speed[\W]+.{0,100})([\W]+)(.{0,100}">)([.\(\)\w\s\d-]+)(</td>)',lines)
 if match_specs_clockspeed:
  print match_specs_clockspeed.group(4)
  specs_clockspeed = match_specs_clockspeed.group(4)
  match_clockspeed = re.findall('[.\d]+',specs_clockspeed)
  for match in match_clockspeed:
   clockspeed = match

 match_specs_ram = re.search(r'(specs-key">System Memory[\W]+.{0,100})([\W]+)(.{0,100}">)([.\(\)\w\s\d-]+)(</td>)',lines)
 if match_specs_ram:
  print match_specs_ram.group(4)
  ram = match_specs_ram.group(4)
  match_ram = re.search(r'\d+',ram)
  if match_ram:
   ram = match_ram.group()

 match_specs_hd = re.search(r'(specs-key">HDD Capacity[\W]+.{0,100})([\W]+)(.{0,100}">)([.\(\)\w\s\d-]+)(</td>)',lines)
 if match_specs_hd:
  print match_specs_hd.group(4)
  hd = match_specs_hd.group(4)
  match_hd = re.search(r'\d+',hd)
  if match_hd:
   hd = match_hd.group()
 

 match_specs_os = re.search(r'(specs-key">Operating System[\W]+.{0,100})([\W]+)(.{0,100}">)([.\(\)\w\s\d-]+)(</td>)',lines)
 if match_specs_os:
  print match_specs_os.group(4)
  os = match_specs_os.group(4)

 match_specs_backup = re.search(r'(specs-key">Battery Backup[\W]+.{0,100})([\W]+)(.{0,100}">)([.\(\)\w\s\d-]+)(</td>)',lines)
 if match_specs_backup:
  print match_specs_backup.group(4)
  specs_backup = match_specs_backup.group(4)

 scraperwiki.sqlite.save(['url'],data={'url':pagelink,'brand':brand,'title':title,'rating':rating,'reviews':reviews,'price':price,'stock':stock,'delivery':delivery,'specs-processor':specs_processor,'variant':specs_variant,'procband':specs_processorbrand,'clockspeed':clockspeed,'ram':ram,'hd':hd,'os':os})


#<span class="boldtext">2-4 business days.</span>
#<div class="stock-status instock" id="fk-stock-info-id">In Stock.</div>
#<span class="price final-price our fksk-our" id="fk-mprod-our-id">Rs.<span class="small-font"> </span>37588</span>
#<a href="#read-reviews"><span itemprop="reviewCount">64</span> Reviews</a>
#<span itemprop="ratingCount">171</span>
#<h1 itemprop="name" title="Samsung NP300E5Z-S08IN Laptop 2 Gen Ci5/4GB/750GB/1GB">Samsung NP300E5Z-S08IN Laptop 2 Gen Ci5/4GB/750GB/1GB</h1>