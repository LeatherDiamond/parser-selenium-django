from . import local_settings
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import random
import json
import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "X-KL-Ajax-Request": "Ajax_Request"
}


def get_source_html(url):
    driver = webdriver.Chrome(
        # Path to the folder with your webdriver that should in one directory with the script.
        executable_path=local_settings.executable_path
    )
    driver.maximize_window()
    try:
        driver.get(url=url)
        time.sleep(10)
        while True:
            find_more_element = driver.find_element(By.XPATH, "//footer[@id='uhf-footer-container']")
            if driver.find_elements(By.XPATH, "//button[@id='getOrRemoveButton-9NBLGGH41XJP']"):
                # Saving parsing results to HTML file and indicating the path where we woul like to save the file.
                with open(local_settings.html_save, "w", encoding="utf-8") as file:
                    file.write(driver.page_source)
                break
            else:
                actions = ActionChains(driver)
                actions.move_to_element(find_more_element).perform()
                time.sleep(3)
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


def get_items_urls(file_path):
    with open(file_path, encoding="utf-8") as file:
        src = file.read()
        
    soup = BeautifulSoup(src, "lxml")
    items_divs = soup.find_all("div", class_="product-card")
    
    id_list = []
    for item in items_divs:
        item_id = item.find("button").get("id")
        id_list.append(item_id)
    # Saving results to TXT file and indicating the path where we woul like to save the file.
    with open(local_settings.txt_save, "w", encoding="utf-8") as file:
        for id in id_list:
            file.write(f"{id}\n")
    
    return "[INFO] Urls collected successfully!"


def get_data(file_path):
    with open(file_path) as file:
        id_correct = [id.replace("getOrRemoveButton-", "").strip() for id in file.readlines()]

    result_list=[]
    urls_count = len(id_correct)
    count = 1
    for id in id_correct:
        s = requests.Session()
        response = s.get(url=f"https://apps.microsoft.com/store/api/ProductsDetails/GetProductDetailsById/{id}?hl=en-gb&gl=US", headers=headers)
        data = response.json()

        product_name = data.get("title")
        publisher_name = data.get("publisherName")
        release_date = data.get("releaseDateUtc")[0:4]
        contact_info = data.get("supportUris")[0].get("uri")
        contact_info_full = "" if contact_info is None else contact_info

        result_list.append(
            {
                "model": "result_view.resultview",
                "pk": count,
                "fields": {
                    "product_name": product_name,
                    "publisher": publisher_name,
                    "release_date": release_date,
                    "contact_info": contact_info_full
                }
            }
        )

        time.sleep(random.randrange(2,5))
        print(f"[+] Processed: {count}/{urls_count}")
        count += 1
    # Saving results to JSON file and indicating the path where we woul like to save the file.
    with open(local_settings.json_save, "w", encoding="utf-8") as file:
        json.dump(result_list, file, indent=4, ensure_ascii=False)

    return "[INFO] Data collected successfully!"

def main():
    # get_source_html(url="https://apps.microsoft.com/store/category/Business") # Link that is necessary to run selenium to collect data from website.
    # print(get_items_urls(file_path=local_settings.html_save)) # Path for working with data in HTML and further converting updated data to TXT.
    get_data(file_path=local_settings.txt_save) # Path that is necessary to run the second part of the script, read collected to TXT data and write results to JSON file.


if __name__ == "__main__":
    main()
