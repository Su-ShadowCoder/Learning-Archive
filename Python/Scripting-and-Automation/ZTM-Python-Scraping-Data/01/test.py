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


from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

base_url1 = "https://news.ycombinator.com/news"


def scrape_pages(base_url):
    print(f"URL: {base_url}")
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, "html.parser")
    #
    get_data(soup)
    #
    special_link = soup.find('a', attrs={'rel': 'next'})
    print(special_link)
    extracted_link = special_link.get('href')
    print(extracted_link)

    if extracted_link is not None:


        absolute_url = urljoin(response, extracted_link)
        print(absolute_url)
        # this will result in: http://example.com/product/1
        item_response = requests.get(absolute_url)
        
        scrape_pages(item_response)
    else:
        print("Done")




goal_url = 'https://news.ycombinator.com/news?p=2'


def get_data(content):
    pass




def main():
    scrape_pages(base_url1)


if __name__=="__main__":
    main()
