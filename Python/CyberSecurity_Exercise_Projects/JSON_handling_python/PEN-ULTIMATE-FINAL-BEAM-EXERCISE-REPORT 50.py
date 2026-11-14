from pprint import pprint

events1 = [
    {
        "username": "shadow",
        "ip": "192.168.1.20",
        "status": "Failed",
        "attempts": "3"
    },
    {
        "username": "guest",
        "ip": "10.0.0.15",
        "status": "Success",
        "attempts": "1"
    },
    {
        "username": "shadow",
        "ip": "192.168.1.20",
        "status": "Failed",
        "attempts": "4"
    },
    {
        "username": "ahmed",
        "ip": "172.16.5.10",
        "status": "Failed",
        "attempts": "5"
    },
    {
        "username": "guest",
        "ip": "10.0.0.15",
        "status": "Failed",
        "attempts": "2"
    }
]

# Converts string dict value into int dict value
for event in events1:
    event["attempts"] = int(event["attempts"])


#f1 Validates successful events and failed events and puts them in their clasified lists. 
def status_validation(events):
    f_result = []
    s_result = []
    for event in events:
        if event['status'] == "Failed":
            f_result.append(event)
        else:
            s_result.append(event)
    return f_result, s_result
# Make sure to use the 0 index when calling for a failed event list and 1 for a success event list. 
# example: print(status_validation(events1)[0])

# its more efficenter to save this as objects rather then calling the first function back everytime you need to do something instead of just doing it one time but i need to incorporate this into my final funciton somehow.


# pprint(f_list_result)

f_list_result = status_validation(events1)[0]
s_list_result = status_validation(events1)[1]
######################step 2
#f2 counts the total events using f1 
def total_event_count():
    return len(f_list_result) + len(s_list_result)
# counts the total events

# print(total_event_count())

#f3 count the failed events and succes events using f1. 
def failed_events_count():
    return len(f_list_result) 
# print(failed_events_count())
def success_events_count():
    return len(s_list_result)
# print(success_events_count())


#f4 failed_username_counter, counts the failed attempts of a username and returns the output of the count.
def failed_attempt_username_lst():
    failed_username_attempts = {}
    for event in f_list_result:
        key = event['username']
        if key not in failed_username_attempts:
            failed_username_attempts[key] = event['attempts']
        else:
            failed_username_attempts[key] += event['attempts']
    return failed_username_attempts
# counts the failed attempts of the specific username. 

# print(failed_attempt_username_lst())

#f5 collects unique failed ips
def runique_ip_collector():
    runique_failed_ips = []

    for event in f_list_result:
        runique_failed_ips.append(event['ip'])
    
    result = set(runique_failed_ips)

    return result
# list of unique ips

# print(runique_ip_collector())

#f6 list of failed attempt users that has failed attempts above 1.
def above1_failed_users():
    base_lst = failed_attempt_username_lst()
    result1 = []
    for user, attempt in base_lst.items():
        if attempt > 1:
            result1.append(user)
    return result1

print(above1_failed_users())

######################step 3
# f7 final report in dict
# def final_ultimate_laserbeam_report():
    # pass
# Final FlashhhhhhhHHH!!!!!!!!!!!!!!

# Designing the blueprint of the report in order to gain an idea what ouput i want for my report function:
# final_pen_ultimate_laserbeam_report = {
#     total_attempt: answer,
#     successful_event_attempt: answer,
#     failed_event_attempt: answer,
#     failed_users_and_attempts: {failed_user: attempt, etc: etc},
#     r_unique_failed_ip: [f_r_u_ip, f_r_u_ip, f_r_u_ip, etc],
#     above_1attempt_failed: [failed_user, failed_user, etc],
# }

f_list_result = status_validation(events1)[0]
s_list_result = status_validation(events1)[1]
#make this autoamtic, but the first function in the main function then use the above in a local var manner that its automaic and can call for every other evnts list.  cals it and then uses it for other function, 


######################step 4
# def main():
#     print(final_ultimate_laserbeam_report(events1))


# if __name__=="__main__":
#     main()

