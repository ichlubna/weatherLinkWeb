<?php 
include("./mysql.php");
$conn = new mysqli($host, $userName, $password, $database);
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM WeatherHistory ORDER BY DateTime desc LIMIT 1";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  while($row = $result->fetch_assoc()) {
	
    $dateTime = date( 'd.m.Y H:i', strtotime($row["DateTime"]));
    echo $dateTime . " - Temp: " . $row["Temp2nd"] . "<br>";
  }
} else {
  echo "Nothing to print.";
}
$conn->close();
?>
