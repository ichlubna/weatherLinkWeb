# Web upload and presentation tools for WeatherLink weather station

This project contains scripts and sample pages that demonstrate a safe way to update a web-based MYSQL database with the new weather records from the station. This project was made for the station model Vantage Pro Plus. This projects solves the unsafe FTP upload problem and the inability to update the whole weather history with the WeatherLink software by Davis Instruments or similar alternatives such as Cumulus.

## How to use
The `scripts` directory contains tools for MYSQL upload.

1. Create an empty MYSQL database
2. Fill the login information in the `credentials.py`
3. Setup the WeatherLink software to store the data in Setup - Internet settings - Local transfer (The 1 Week Data Archive file needs to be set to transfer in the Data Upload - Profile)
4. Export the current station history in Browse the station data (icon) - Browse - Export records and change the header of the file to be the same as in the Report in step 3.
5. Create a new database table and import the current history by running `python init.py historyFile.txt`
6. Start the update script which will run forever, check the new records, and add them to the database as `python update.py path/to/the/local/reports/downld08.txt` (the path is the same as in step 3 in the Local transfer settings)

The update script can be set up to run after computer startup along with the WeatherLink Software. Both need to be running. The WeatherLink software will update the local folder with new records and the script will check the records and send them to the database. Make sure to set the desired update interval in both tools.

If the total history file is too big, the connection might get aborted. Then upload the data via Phpmyadmin or comment the table creating in the script and upload by smaller files.

## Web example
The `web` directory contains a simple presentation of the results uploaded to the database. Fill the database credentials in `credentials.php` and run the index.php on the web.
