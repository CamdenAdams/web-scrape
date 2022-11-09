import sys
import requests
import logging

logging.basicConfig(filename='web_scrape.log', level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

# todo: if sold out at tustin store not found, search for in stock string identifier
# todo: setup mail account to send text in case of in stock confirmation
    # todo: in text, include store phone number
# todo: schedule job or loop

def main():
    # main entry function
    is_sold_out()
    return None

def save_webpage(web_content):
    with open('web_to_text.txt', 'w+b') as file:
        file.write(web_content)
    return None

def get_target_urls():
    urls = []
    with open('target_url.txt', 'r') as file:
        for line in file.readlines():
            urls.append(line.strip())
    return urls

def check_html_for_sold_out():
    with open('web_to_text.txt', 'r') as file:
        file_as_text = file.read()
        target_string_placement = file_as_text.find('SOLD OUT<span class="storeName"> at Tustin Store</span>')
        if target_string_placement == -1:
            logging.info('SOLD OUT string not found - assume item in stock -  target_string_placement = {}'.format(target_string_placement))
        else:
            logging.info('SOLD OUT string found - out of stock - target_string_placement = {}'.format(target_string_placement))    
    return None

def is_sold_out():
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"}
    for url in get_target_urls():
        result = requests.get(url=url, headers=headers)
        save_webpage(result.content)
        check_html_for_sold_out()
    return None

if __name__ == '__main__':
    main()






# def get_page_html():
#     headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"}
#     result = requests.get(url=sys.argv[1], headers=headers)
#     print(result.status_code)
#     return result.content