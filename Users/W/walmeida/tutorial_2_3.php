<?php
# Blank PHP
$sourcescraper = '';

scraperwiki::attach("tutorial_1_5");

$data = scraperwiki::select(
    "* from tutorial_1_5.swdata 
    order by years_in_school desc limit 10"
);
#print_r($data);


print "<table>";
print "<tr><th>Country</th><th>Years in school</th>";
foreach($data as $d){
  print "<tr>";
  print "<td>" . $d["country"] . "</td>";
  print "<td>" . $d["years_in_school"] . "</td>";
  print "</tr>";
}
print "</table>";


?>
<?php
# Blank PHP
$sourcescraper = '';

scraperwiki::attach("tutorial_1_5");

$data = scraperwiki::select(
    "* from tutorial_1_5.swdata 
    order by years_in_school desc limit 10"
);
#print_r($data);


print "<table>";
print "<tr><th>Country</th><th>Years in school</th>";
foreach($data as $d){
  print "<tr>";
  print "<td>" . $d["country"] . "</td>";
  print "<td>" . $d["years_in_school"] . "</td>";
  print "</tr>";
}
print "</table>";


?>
