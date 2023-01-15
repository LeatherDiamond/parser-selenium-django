Microsoft website parser with web interface for received results.

Applied technologies: Python, Selenium, PostgreSQL, Django, Booststrap, JavaScript.


"parser_script.py" works with Selenium and initially collects all information about application cards of the "Business" category into an HTML file. 
Then the script extracts the ID of each card from the received file and writes it to a TXT file, edits the ID to the desired form, substitutes it in the specified URL and traverses it, collecting the necessary information.
Collected information is recorded to a JSON file and imported into the database.
Web interface for recieved results allows to view data in a convenient format and filter it if it's necessary.
