<?php
$result = mysqli_query($conn, "SELECT pays, count(strategie_national) FROM Documents;");
$output = array();

while ($row = mysqli_fetch_assoc($result, MYSQL_NUM)) {
    array_push($output, $row);
}

print (json_encode($output)); 
?>