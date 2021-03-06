<?php

require 'scraperwiki/simple_html_dom.php';
print "Hello world! Running...";
$html = scraperWiki::scrape("http://www.osha.gov/pls/imis/industry.search?p_logger=1&naics=23&State=All&officetype=All&Office=All&endmonth=01&endday=01&endyear=2010&startmonth=12&startday=31&startyear=2012&p_sort=open_date&p_desc=DESC");
//print $html . "\n";

$dom = new simple_html_dom();
$dom->load($html);
foreach($dom->find("div tr") as $data){
    $tds = $data->find("td");
    if(count($tds)==12){
        $record = array(
           'activity number' => $tds[2]->plaintext,
           'opened' => $tds[3]->plaintext,
           'report id' => $tds[4]->plaintext,
           'state' => $tds[5]->plaintext,
           'type' => $tds[6]->plaintext,
           'scope' => $tds[7]->plaintext,
           'SIC' => $tds[8]->plaintext,
           'NAICS' => $tds[9]->plaintext,
           'violation' => $tds[10]->plaintext,
           'establishment name' => $tds[11]->plaintext
      );
       //print json_encode($record) . "\n";
       scraperwiki::save(array('activity number'), $record);
  }}

for ($i=1;$i<100;$i++){
    $html=scraperWiki::scrape("http://www.osha.gov/pls/imis/industry.search?sic=&sicgroup=&naicsgroup=&naics=23&state=All&officetype=All&office=All&startmonth=12&startday=31&startyear=2012&endmonth=01&endday=01&endyear=2010&opt=&optt=&scope=&fedagncode=&owner=&emph=&emphtp=&p_start=".(($i-1)*20)."&p_finish=".($i*20)."&p_direction=Next&p_show=20&p_sort=open_date&p_desc=DESC");
    $dom = new simple_html_dom();
    $dom->load($html);
    foreach($dom->find("div tr") as $data){
        $tds = $data->find("td");
        if(count($tds)==12){
        $record = array(
           'activity number' => $tds[2]->plaintext,
           'opened' => $tds[3]->plaintext,
           'report id' => $tds[4]->plaintext,
           'state' => $tds[5]->plaintext,
           'type' => $tds[6]->plaintext,
           'scope' => $tds[7]->plaintext,
           'SIC' => $tds[8]->plaintext,
           'NAICS' => $tds[9]->plaintext,
           'violation' => $tds[10]->plaintext,
           'establishment name' => $tds[11]->plaintext
      );
       //print json_encode($record) . "\n";
       scraperwiki::save(array('activity number'), $record);
  }
}
}

?>
<?php

require 'scraperwiki/simple_html_dom.php';
print "Hello world! Running...";
$html = scraperWiki::scrape("http://www.osha.gov/pls/imis/industry.search?p_logger=1&naics=23&State=All&officetype=All&Office=All&endmonth=01&endday=01&endyear=2010&startmonth=12&startday=31&startyear=2012&p_sort=open_date&p_desc=DESC");
//print $html . "\n";

$dom = new simple_html_dom();
$dom->load($html);
foreach($dom->find("div tr") as $data){
    $tds = $data->find("td");
    if(count($tds)==12){
        $record = array(
           'activity number' => $tds[2]->plaintext,
           'opened' => $tds[3]->plaintext,
           'report id' => $tds[4]->plaintext,
           'state' => $tds[5]->plaintext,
           'type' => $tds[6]->plaintext,
           'scope' => $tds[7]->plaintext,
           'SIC' => $tds[8]->plaintext,
           'NAICS' => $tds[9]->plaintext,
           'violation' => $tds[10]->plaintext,
           'establishment name' => $tds[11]->plaintext
      );
       //print json_encode($record) . "\n";
       scraperwiki::save(array('activity number'), $record);
  }}

for ($i=1;$i<100;$i++){
    $html=scraperWiki::scrape("http://www.osha.gov/pls/imis/industry.search?sic=&sicgroup=&naicsgroup=&naics=23&state=All&officetype=All&office=All&startmonth=12&startday=31&startyear=2012&endmonth=01&endday=01&endyear=2010&opt=&optt=&scope=&fedagncode=&owner=&emph=&emphtp=&p_start=".(($i-1)*20)."&p_finish=".($i*20)."&p_direction=Next&p_show=20&p_sort=open_date&p_desc=DESC");
    $dom = new simple_html_dom();
    $dom->load($html);
    foreach($dom->find("div tr") as $data){
        $tds = $data->find("td");
        if(count($tds)==12){
        $record = array(
           'activity number' => $tds[2]->plaintext,
           'opened' => $tds[3]->plaintext,
           'report id' => $tds[4]->plaintext,
           'state' => $tds[5]->plaintext,
           'type' => $tds[6]->plaintext,
           'scope' => $tds[7]->plaintext,
           'SIC' => $tds[8]->plaintext,
           'NAICS' => $tds[9]->plaintext,
           'violation' => $tds[10]->plaintext,
           'establishment name' => $tds[11]->plaintext
      );
       //print json_encode($record) . "\n";
       scraperwiki::save(array('activity number'), $record);
  }
}
}

?>
