<?php

$lib = scraperWiki::scrape("http://www.ruralfinance.org/library/en/");

require 'scraperwiki/simple_html_dom.php';           
$dom = new simple_html_dom();
$dom->load($lib);
foreach($dom->find("table.contenttable a") as $data){
    $sectionlinks[] = $data->href;
}

$i = 0;
foreach($sectionlinks as $link){
    $sections[] = scraperWiki::scrape("http://www.ruralfinance.org/" . $link);    
    $dom = new simple_html_dom();
    $dom->load(end($sections));
    foreach($dom->find("div[@id='navNext'] a") as $data){
        $pagetwolinks[] = htmlspecialchars_decode($data->href);
    }
}

$i = 0;
foreach($pagetwolinks as $link){
    $it = "";
    $pagetwos[] = scraperWiki::scrape("http://www.ruralfinance.org/" . $link);    
    $dom = new simple_html_dom();
    $dom->load(end($pagetwos));
    $j = 0;
    foreach($dom->find("table.ab tr") as $data){
        if($j != 0){
            $as = $data->find("td a");
            if(strpos($as[0], "http://www.ruralfinance.org/discussion/") > 0)
                $it .= $as[0] . "<br>";
        }
        $j++;
    }

    scraperwiki::save_var($i, $it);
    $i++;
}
?>
<?php

$lib = scraperWiki::scrape("http://www.ruralfinance.org/library/en/");

require 'scraperwiki/simple_html_dom.php';           
$dom = new simple_html_dom();
$dom->load($lib);
foreach($dom->find("table.contenttable a") as $data){
    $sectionlinks[] = $data->href;
}

$i = 0;
foreach($sectionlinks as $link){
    $sections[] = scraperWiki::scrape("http://www.ruralfinance.org/" . $link);    
    $dom = new simple_html_dom();
    $dom->load(end($sections));
    foreach($dom->find("div[@id='navNext'] a") as $data){
        $pagetwolinks[] = htmlspecialchars_decode($data->href);
    }
}

$i = 0;
foreach($pagetwolinks as $link){
    $it = "";
    $pagetwos[] = scraperWiki::scrape("http://www.ruralfinance.org/" . $link);    
    $dom = new simple_html_dom();
    $dom->load(end($pagetwos));
    $j = 0;
    foreach($dom->find("table.ab tr") as $data){
        if($j != 0){
            $as = $data->find("td a");
            if(strpos($as[0], "http://www.ruralfinance.org/discussion/") > 0)
                $it .= $as[0] . "<br>";
        }
        $j++;
    }

    scraperwiki::save_var($i, $it);
    $i++;
}
?>
