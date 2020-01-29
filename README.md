# XBM-Conversion
Full procedure to convert Data from an SQL Server into an image template and saving that template as a .h file ready to upload on an esp32.

Only works for my test case yet, which is:
- test SQL table with three columns that get querried
- three values get pasted into a 640x384 pixel image
- image is converted to xbm
- xbm is then formated to fit the syntax of c++ images under arduino
