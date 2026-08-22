### Heads up! In the next video we will learn about selectors and we are going to use the Hackernews website to select some stories. Hackernews now uses the .titleline class instead of the .storylink class so you just need to make sure you enter .titleline in the next video when you see me use .storylink ###

### Finally, in the code attached I use .titleline > a because the link is now inside the first <a> tag under the titleline element. ###

import requests

from bs4 import  BeautifulSoup

import pprint

# you can think of res like a webbrowser without the actual window. like how type google.com on a browser and enter it to navigate to. this does the same. 


res = requests.get('https://news.ycombinator.com/news')
# convert from string to something you can use. this the act of parsing
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')



def next_page()


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

pprint.pprint(create_custom_hn(links, subtext), sort_dicts=False)














###################################################
# first challange
###################################################

# this is how i first made it by making it without watching the following video. 

# def create_custom_hn(links, subtext):
#     hn = []
#     for idx, item in enumerate(links):
#         title = links[idx].getText()
#         href = links[idx].get("href", None)
#         try:
#             min_points = 100
#             points = int(subtext[idx].getText().split(" points by")[0].strip())
#             if points >= min_points:
#                 hn.append({
#                     "title": title,
#                     "link": href,
#                     "votes": points
#                     })
#         except ValueError:
#             print("error")
#         except Exception:
#             print(Exception)
#     return hn

# print(create_custom_hn(links, subtext))

#########################################################################