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
	
	function printOneRecord($record)
	{
		$dateTime = new DateTime($record["DateTime"]);
		$dateTime = $this->fixTime($dateTime);
		$stringDateTime = $dateTime->format('d.m.Y H:i');
		//The temperature at the station is under Temp2nd in our case
		echo $stringDateTime . " - Temp: " . $record["Temp2nd"] . "<br>";
	}
	
	function sendQuery($query)
	{
		$result = $this->conn->query($query);
		if (!$result) 
			echo("Error: ".$this->conn->error);
		return $result;
	}
	
	function printResult($result)
	{
		if ($result->num_rows > 0)
			while($row = $result->fetch_assoc()) 
				$this->printOneRecord($row);
		else 
			echo "Nothing to print.";
	}
	
	function printLatestData($count=1)
	{
		$sql = "SELECT * FROM WeatherHistory ORDER BY DateTime desc LIMIT ".$count;
		$result = $this->sendQuery($sql);
		$this->printResult($result);
	}
	
	function printDays($firstDate, $lastDate)
	{
		$sql = "SELECT * FROM WeatherHistory WHERE DateTime BETWEEN '".$firstDate."' AND '".$lastDate."' ORDER BY DateTime desc";
		$result = $this->sendQuery($sql);
		$this->printResult($result);
	}
}
ini_set('display_errors', '1');
ini_set('display_startup_errors', '1');
error_reporting(E_ALL);
$reporter = new Reporter();
$reporter->printLatestData();
$reporter->printDays("2023-01-01", "2023-02-20");
?>
