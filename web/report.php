<?php 
include("./mysql.php");
class Reporter extends Credentials
{
	private $conn;
	
	function __construct()
	{
		$this->conn = new mysqli($this->host, $this->userName, $this->password, $this->database);
		if ($this->conn->connect_error) 
			die("Connection failed: " . $this->conn->connect_error);
	}
	
	function __destruct() 
	{
		$this->conn->close();
	}
	
	//The time might be different on the station so the corrections can be made here
	function fixTime($dateTime)
	{
		$dateTime->add(new DateInterval('PT5H25M0S'));
		return $dateTime;
	}
	
	function printLatestData()
	{
		$sql = "SELECT * FROM WeatherHistory ORDER BY DateTime desc LIMIT 1";
		$result = $this->conn->query($sql);

		if ($result->num_rows > 0)
			while($row = $result->fetch_assoc()) 
			{
				$dateTime = new DateTime($row["DateTime"]);
				$dateTime = $this->fixTime($dateTime);
				$stringDateTime = $dateTime->format('d.m.Y H:i');
				//The temperature at the station is under Temp2nd in our case
				echo $stringDateTime . " - Temp: " . $row["Temp2nd"] . "<br>";
			}
		else 
		  echo "Nothing to print.";
	}
}
ini_set('display_errors', '1');
ini_set('display_startup_errors', '1');
error_reporting(E_ALL);
$reporter = new Reporter();
$reporter->printLatestData();
?>
