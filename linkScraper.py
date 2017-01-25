from bs4 import BeautifulSoup
import requests
import re

def linkScraper():
    """Use case specific function for extracting the location of .csv files for the MHSDS dataset  on NHS Digital."""
    print('Starting data scrape of NHS Digital')
    data_for_frames = []
    result = requests.get('http://content.digital.nhs.uk/mhldsreports')
    c = result.content
    soup = BeautifulSoup(c, 'lxml')
    href_list = []
    for a in soup.find_all('a', href=True):
        href_list.append(a['href'])
    dataset_links = href_list[27:50]
    for i, x in enumerate(dataset_links):
        print('Starting scrape for csv file at URL: ', x ,'Index: ', i+1 ,'/',len(dataset_links))
        try:
            result = requests.get(x)
            c = result.content
            soup_2 = BeautifulSoup(c, 'lxml')
            href_list_2 = []
            for a in soup_2.find_all('a', href=True):
                href_list_2.append(a['href'])
            csv_list = []
            regex=re.compile(r"[a-zA-Z0-9]*\/[a-zA-Z0-9]*\/[-[a-zA-Z0-9]*\.csv")
            csv_list.append([m.group(0) for l in href_list_2 for m in [regex.search(l)] if m])
            print('http://content.digital.nhs.uk/' + csv_list[0][0])
            data_for_frames.append('http://content.digital.nhs.uk/' + csv_list[0][0])
            print('Status: Successful\n')
        except:
            print('Status: 404, please check URL for more details.\n')
    return data_for_frames
