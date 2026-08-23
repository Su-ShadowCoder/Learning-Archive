
import requests

from bs4 import  BeautifulSoup

import pprint

from urllib.parse import urljoin

import time


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k["votes"], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(' points', ""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})

    return sort_stories_by_votes(hn)

def scrape_pages(base_url):
    print(f"URL: {base_url}\n")
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.select('.titleline > a')
    subtext = soup.select('.subtext')

    # scraping the website
    pprint.pprint(create_custom_hn(links, subtext), sort_dicts=False)

    print("End of page 1\n\n")

    next_element = soup.find('a', attrs={'rel': 'next'})


    # pagination till 5 pages
    count = 1
    while count != 3 and next_element != None:   
        
        extracted_link = next_element.get('href')
    
        absolute_url = urljoin(base_url, extracted_link)
        
        print("Next page.\n\n")
        time.sleep(3)
        new_page_response = requests.get(absolute_url)
        soup = BeautifulSoup(new_page_response.content, "html.parser")
        links = soup.select('.titleline > a')
        
        subtext = soup.select('.subtext')

        # scraping the website
        pprint.pprint(create_custom_hn(links, subtext), sort_dicts=False)
        print(f"End of page {count+1}\n")

        print(new_page_response.status_code)
        print(new_page_response.url)

        next_element = soup.find('a', attrs={'rel': 'next'})
        count += 1


    print("Done") 


def main():
    base_url1 = "https://news.ycombinator.com/news"
    scrape_pages(base_url1)


if __name__=="__main__":
    main()



