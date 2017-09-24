# NBAJSON2CSV
Convert the JSON data on NBAs Site to easy to use CSV format!

How to get JSON data:
1. Go to the stats.nba.com
2. Select a page of particular statistics you might want (example: http://stats.nba.com/players/isolation/)
3. Right click on the page, then select inspect
4. On the new box that popped on on the right of the screen, select the Network tab
5. Under the network bar, select XHR, then there should be a link that says something like "leaguedashplayer"
  5a. If you don't see it, refresh the page
6. Click it, and copy the "Request URL" into another tab
7. Save the data to a .json file
8. You're done!


How to convert JSON to CSV
1. Save the jsoncsv.py script into a folder
2. Save the JSON dataset(s) into the same folder as the script
3. Open terminal, and make the directory the folder all the datafiles and scripts are in
4. For each file, type "python3 jsoncsv.py jsonfile", with jsonfile being the file name
5. A new csv file with the same name as the json file should be in the folder
6. You're done!
