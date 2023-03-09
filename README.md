
# Project description

***Introducing you website parser with web interface for received results.***

Microsoft's website was chosen as the website to collect the data.
Parser works with Selenium and initially collects all information about application cards of the ***"Business"*** category into an HTML file 
***(by default parser script collects 200 product cards).*** 
Then the script extracts the ID of each card from the received file and writes it to a TXT file, edits the ID to the desired form, substitutes it in the specified URL and traverses it, collecting the following data:
  * Product name;
  * Publisher;
  * Release date;
  * Contact info;
  
Collected information is recorded to a JSON file and imported into the database.


Web interface for recieved results allows to view data in a convenient format, apply filters, use searchbar.
The parser architecture described above was chosen because the website is dynamic and the content required for collection is given back by website as a JSON file, from which content is extracted.

***Applied technologies:*** *Python, Selenium, PostgreSQL, Django, HTML, CSS, JavaScript.*

###### NOTES:
 > * *You can familiarize with deployed version of the project by the following [link](https://almond.pythonanywhere.com/parsing_results).*
 > By clicking the link you will find a page with parsed results *(200 products from "Business" category)* where you can check described above web interface.
 
 
 # How to start? <sub>(Installation and Launch)</sub>
 
 **1. Clone current repository:**
 ```
 git clone https://github.com/LeatherDiamond/parser_selenium-django.git
 ```
 
 **2. Install all requirements from "requirements.txt":**
 ```
 pip install -r requirements.txt
 ```
 
 **3. Create PostgreSQL database on your local machine:**
 
 * Familiarize with the information on the [website](https://www.postgresql.org/download/) (running the database on different operating systems) and if necessary         download the PostgreSQL installer for your operating system or follow the steps described on the website to launch the database.
  
  ***Below you will find instructions on how to start and configure the database on Windows operating system:***
  
  > ###### **Launching PostgreSQL on Windows:**
  
  * Download PostgreSQL installer from the [website](https://www.postgresql.org/download/);
  * Install all the components from the list:
  
  ![components installation](https://github.com/LeatherDiamond/parser_selenium-django/blob/master/README%20images/PostgreSQL%20components%20installation.png)
  
  * After the isnstallation is finished, laucn Stack Builder at exit and install Database Drivers in accordance with bitness of your Windows system.
  
  ![drivers installation](https://github.com/LeatherDiamond/parser_selenium-django/blob/master/README%20images/PostgreSQL%20drivers%20installation.png)
  
  * Launch pgAdmin4 application and set a master password for the application.
  
  * Click "PostgreSQL" and insert your password in appeared window to connect the DB server.
  
  ![connection to the server](https://github.com/LeatherDiamond/parser_selenium-django/blob/master/README%20images/PostgreSQL%20connection%20to%20the%20server.png)
  
  * 
