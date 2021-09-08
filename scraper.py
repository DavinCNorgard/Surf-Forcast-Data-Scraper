from urllib.request import urlopen
from bs4 import BeautifulSoup

def LaPeruse():

    url_to_scrape = "https://www.ndbc.noaa.gov/station_page.php?station=46206&uom=E&tz=STN"

    request_page = urlopen(url_to_scrape)
    page_html = request_page.read()
    request_page.close()

    html_soup = BeautifulSoup(page_html, 'html.parser')

    html_soup = html_soup.find(id="data")
    html_soup = html_soup.find('table')

    #print(html_soup)

    wvht = html_soup.find(text='Wave Height (WVHT):')
    whvt_INFO = wvht.parent.find_next_sibling().text

    dpd = html_soup.find(text="Dominant Wave Period (DPD):")
    dpd_INFO = dpd.parent.find_next_sibling().text

    formatted = [[wvht, whvt_INFO], [dpd, dpd_INFO]] 
    
    return formatted