# Navigation

* ***[Project description](#project-description)***
   * ***[Notes](#notes)***
* ***[How to start? <sub>(Installation and Launch)</sub>](#how-to-start-installation-and-launch)***
   * ***[Installation](#installation)***
     * ***[Launching PostgreSQL on Windows](#launching-postgresql-on-windows)***
   * ***[Launch](#launch)***
     * ***[Script launch](#script-launch)***
     * ***[Web Interface launch](#web-interface-launch)***
* ***[Why should you try it?](#why-should-you-try-it)***
* ***[License](#license)***


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


Web interface for received results allows to view data in a convenient format, apply filters, use searchbar.
The parser architecture described above was chosen because the website is dynamic and the content required for collection is given back by website as a JSON file, from which content is extracted.

***Applied technologies:*** *Python, Selenium, PostgreSQL, Django, HTML, CSS, JavaScript.*

###### NOTES:
 > *You can familiarize with deployed version of the project by the following [link](https://almond.pythonanywhere.com/parsing_results).*
 > By clicking the link you will find a page with parsed results *(200 products from "Business" category)* where you can check described above web interface.
 
 
 # How to start? <sub>(Installation and Launch)</sub>
 
 ### ***Installation***
 **1. Clone current repository:**
 ```
 git clone https://github.com/LeatherDiamond/parser_selenium-django.git
 ```
 
 **2. Install all requirements from "requirements.txt":**
 ```
 pip install -r requirements.txt
 ```
 
 
 **3. Add Web Driver to the directory with the project.**
 
  > In parser source code Selenium is used with Chrome browser. To launch script with selenium you should download correct version of Web Driver (Chromedriver). It depends on what version of Chrome you are using on your local machine and can be downloaded by the following [link](https://chromedriver.chromium.org/).
  >
  > * ***Chromedriver should be located in the folder "chromedriver" in the main directory of the project (/parser_selenium-django/chromedriver/chromedriver.exe).***
 
 **4. Create PostgreSQL database on your local machine:**
 
 * Familiarize with the information on the [website](https://www.postgresql.org/download/) (running the database on different operating systems) and if necessary         download the PostgreSQL installer for your operating system or follow the steps described on the website to launch the database.
  
  *Below you will find instructions on how to start and configure the database on* ***Windows operating system:***
  
  > ###### **Launching PostgreSQL on Windows:**
  >
  > * Download PostgreSQL installer from the [website](https://www.postgresql.org/download/);
  > * Install all the components from the list:
  >
  > ![components installation](https://github.com/LeatherDiamond/parser_selenium-django/blob/master/README%20images/PostgreSQL%20components%20installation.png)
  >
  > * After the isnstallation is finished, laucn Stack Builder at exit and install Database Drivers in accordance with bitness of your Windows system.
  >
  > ![drivers installation](https://github.com/LeatherDiamond/parser_selenium-django/blob/master/README%20images/PostgreSQL%20drivers%20installation.png)
  >
  > * Launch pgAdmin4 application and set a master password for the application.
  >
  > * Click "PostgreSQL" and insert your password in appeared window to connect the DB server.
  >
  > ![connection to the server](https://github.com/LeatherDiamond/parser_selenium-django/blob/master/README%20images/PostgreSQL%20connection%20to%20the%20server.png)
  >
  > * Create the DB which will be used for the project (it can be done with desktop application "pgAdmin4" or with interactive PostgreSQL terminal "SQL Shell".
  > ***Below will be instruction how to do it with SQL Shell):***
  > 
  > ***NOTE:*** During Postgres installation, a "postgres" user (PostgreSQL administrator) was created in the OS automatically. This user should be used to perform       > administrative tasks. Password to "postgres" user was provided earlier when "pgAdmin4" application was launched first time after installation.
  >
  > 1. Launch SQL Shell (psql) (interactive terminal PostgreSQL) and provide data to connect the default DB that was created automatically:
  > 
  > ![connection to default DB](https://github.com/LeatherDiamond/parser_selenium-django/blob/master/README%20images/SQL%20Shell%20connection%20to%20BD.png)
  >
  > 2. Create the DB for the project:
  > ```
  > CREATE DATABASE database_name;
  > ```
  > 3. Create a DB user:
  > ```
  > CREATE username USER WITH PASSWORD 'password';
  > ```
  > 4. Give the created user superuser rights:
  > ```
  > ALTER ROLE username SUPERUSER;
  > ```
  > ![DB ready for use](https://github.com/LeatherDiamond/parser_selenium-django/blob/master/README%20images/DB%20and%20user%20created%20and%20ready.png)
   
  **5. Provide mandatory data in ***settings.py*** and ***parser_script.py*** files:**
  
   - [x] settings.py:
   
   - Django SECRET_KEY;
   - DATABASES:
   ```
   DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  
        'NAME': 'database_name',  
        'USER': 'user_name',  
        'PASSWORD': 'user_password',  
        'HOST': '127.0.0.1',  
        'PORT': '5432'
        }  
}
   ```

   - [x] parser_script.py:

   - line 22 ***"executable_path"*** - Path to your Web Driver;
   - line 32 ***"local_settings.html_save"*** - Should be replaced with path where your HTML file with parsed data will be saved ("/parser_selenium-django/source-page.html");
   - line 58 ***local_settings.txt_save*** - Should be replaced with path where your TXT file with extracted product card IDs will be saved ("/parser_selenium-django/items-id.txt")
   - line 100 ***local_settings.json_save*** - Should be replaced with path where your JSON file with final parsing results will be saved.
   > IMPORTANT: JSON file with results should be located in ***"fixtures"*** folder for further import in database ***(/parser_selenium-django/src/result_view/fixtures/parsing_results.json)***
 
 **6. Apply all migrations:***
 ```
 python manage.py migrate
 ```
 
 ### ***Launch***
  
  ###### Script launch
  > Script is working in 3 steps:
  > * ***Step 1*** - Collection of product cards data in "Business" category website page with Selenium and saving results to HTML;
  > * ***Step 2*** - Collection of item IDs from HTML page and saving them to TXT file;
  > * ***Step 3*** - Substituion of collected IDs to specified URL, following it, extracting data and saving results to JSON file;
  >
  > To launch ***Step 1***, **parser_script.py** should have the following structure:
  > * ***Uncommented lines*** - 2-43, 105, 106, 111, 112;
  > * ***Other lines should be commented (Ctrl + /)***
  >
  > To launch ***Step 2***, **parser_script.py** should have the following structure:
  > * ***Uncommented lines*** - 2-16, 46-62, 105, 107, 111, 112;
  > * ***Other lines should be commented (Ctrl + /)***
  >
  > To launch ***Step 3***, **parser_script.py** should have the following structure:
  > * ***Uncommented lines*** - 2-16, 65-105, 108, 111, 112;
  > * ***Other lines should be commented (Ctrl + /)***
  
  
  ###### Web interface launch
  > * Import collected on ***Step 3*** data into the previously created database:
  > ```
  > python manage.py loaddata parsing_results.json
  > ```
  > * Launch the Django server (All steps in the [Installation](#installation) section should be completed before launching):
  > ```
  > python manage.py runserver
  > ```
  
  
  # Why should you try it?
  
***Accurate Data Collection:*** *With the help of Selenium, this program collects all the necessary data about the products in a specific category, ensuring accurate and up-to-date information.*

***Customizable ID Extraction:*** *The program allows you to customize the format of the IDs extracted from the HTML file, enabling you to fit the extracted IDs into your specific requirements.*

***Comprehensive Data Collection:*** *The program extracts a range of important information about the products, including their name, publisher, release date, and contact information, making it an invaluable tool for anyone looking to gather comprehensive data on a large number of products.*

***Easy Data Access:*** *The web interface included in the program allows you to easily view the collected data in a convenient format, apply filters, and use the search bar to find the information you need quickly and easily.*

***Flexible settings:*** *The program can be adapted to your needs by collecting data from sites you are interested in, it can be used in conjunction with Selenium and other browsers if Chrome is not suitable for you.*

***Proven Technologies:*** *The program uses a range of proven technologies, including Python, PostgreSQL, Django, HTML, CSS, and JavaScript, ensuring that you can rely on the program to work smoothly and efficiently.*


# License

***This project is licensed under the MIT License - see the [LICENSE](https://github.com/LeatherDiamond/parser_selenium-django/blob/master/LICENCE) file for details.***

