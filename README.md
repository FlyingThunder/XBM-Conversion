# XBM-Conversion
Full procedure to convert Data from an SQL Server into an image template and saving that template as a .h file ready to upload on an esp32.



How to use the script:
- Create an SQL Database and fill in your SQL Connection data (DB Name, user, password, ip/port) into ImageEdit.py 
- Create a table with three columns
- Start the script
- run a querry for your database to add values to the three columns - the values will now be pasted into the preset (Vorlage.png) and the final image will be converted into .h and copied into the respective folder
