### Heads up! In the next video we will learn about selectors and we are going to use the Hackernews website to select some stories. Hackernews now uses the .titleline class instead of the .storylink class so you just need to make sure you enter .titleline in the next video when you see me use .storylink ###

### Finally, in the code attached I use .titleline > a because the link is now inside the first <a> tag under the titleline element. ###
### Heads up! In the next video we will learn about selectors and we are going to use the Hackernews website to select some stories. Hackernews now uses the .titleline class instead of the .storylink class so you just need to make sure you enter .titleline in the next video when you see me use .storylink ###

# you can think of res like a webbrowser without the actual window. like how type google.com on a browser and enter it to navigate to. this does the same. 


# res = requests.get('https://news.ycombinator.com/news')
# # convert from string to something you can use. this the act of parsing
# soup = BeautifulSoup(res.text, "html.parser")
# links = soup.select('.titleline > a')
# subtext = soup.select('.subtext')


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



# refresshing enumerate 

# Exercise 1 — Beginner: enumerate()

# events = [
#     "LOGIN_SUCCESS",
#     "LOGIN_FAILED",
#     "LOGIN_FAILED",
#     "LOGIN_SUCCESS"
# ]

# for index, event in enumerate(events):
#     print(index, event)



# Exercise 2 — Intermediate: enumerate() + if

# for index, event in enumerate(events):
#     if "LOGIN_FAILED" in event:
#         print(index, event)

# Exercise 3 — Advanced: understand the (index, object) pair

# users = ["bob", "alice", "admin", "bob"]

# for user in enumerate(users):

#     index, clean_user = user

#     if clean_user == "bob":
#         print(f"{index} {clean_user} -> FOUND")
#     else:
#         print(f"{index} {clean_user} -> NOT FOUND")



# # test 1 is 13, test 2 is "age", test 3 is 

# # def get_age(users)
# #     for user in users:
# #         return user["age"]

# # test 4. 

# # it gives the reverse of the ordered results or not ordered results if possible

# # test 5.

# events = [
#     {"event": "LOGIN", "failed": 5},
#     {"event": "LOGIN", "failed": 12},
#     {"event": "LOGIN", "failed": 3}
# ]

# if forgot can you explain to me how sorted works agani



# round2

# q1 = [10, 8, 3, 1]

# q2 = so with the key in mind of the items, take the value(key=) because you asigned that to the thing you want to manipulate, and sort that. 

# q3 = 


# def get_failed_event():
#     return event["failed"]


# q4 


# events = [
#     {"event": "LOGIN", "failed": 5},
#     {"event": "LOGIN", "failed": 12},
#     {"event": "LOGIN", "failed": 3}
# ]

# result = sorted(events, key="failed", reverse=True)


#  q5

# sort trough the events list of dicts, and get the value of get_failed, and sort trough those value in reverse, where the highest number to the lowest numbber in decending order. 





# challenge 1

# events = [
#     {"event": "LOGIN", "failed": 5, "severity": 2},
#     {"event": "LOGIN", "failed": 12, "severity": 5},
#     {"event": "LOGIN", "failed": 3, "severity": 4}
# ]


# def get_severity(event):
#     return event["severity"]



# get_severitys = lambda events: event[severity]



# 1. 

# use x and do x times 2, and give me that x

# 2. 

# lamba = anounymous function, event = parameter: event["severity"] get the value of this key

# 3. 

# sorted(events, key=lambda event: event["failed"])

# sort whatever is within the brackets(from this list parameter, for this function parameter: parameter[key] - get the value of this parameter key)

# and key= siginifies what key you want to use in events to have the value out of it. 


# from bs4 import BeautifulSoup
# import requests
# from urllib.parse import urljoin

# base_url1 = "https://news.ycombinator.com/news"


# def scrape_pages(base_url):
#     print(f"URL: {base_url}")
#     response = requests.get(base_url)
#     soup = BeautifulSoup(response.content, "html.parser")
    
#     # scraping the website
#     get_data(soup)
    
#     print("End of page")

#     next_element = soup.find('a', attrs={'rel': 'next'})
    
#     # pagination till None
#     while next_element != None:   
        
#         extracted_link = next_element.get('href')
    
#         absolute_url = urljoin(base_url, extracted_link)

#         new_page_response = requests.get(absolute_url)

#         soup = BeautifulSoup(new_page_response.content, "html.parser")

#         get_data(soup)

#         print("Next page.")

#         next_element = soup.find('a', attrs={'rel': 'next'})
    

#     print("Done") 


# def get_data(content):
#     pass


# def main():
#     scrape_pages(base_url1)


# if __name__=="__main__":
#     main()




# explain the difference between base url and respons varaibale value, or hw should i call this again statement? no i am trying use the word for the value they have. either way. the base url is the string of the website, while the response variale value is the execution that python does to go to that website. like in the browser but without the gui. so you use the base url plus the relative to get the absolute. 

# so what happens if soup.find doesnt get anything ? you get None and error

import time


print("Starting...")
time.sleep(5)
print("Continueing...")