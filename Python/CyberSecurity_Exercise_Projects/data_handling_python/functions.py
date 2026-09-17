
# validates single event
def validate_security_event(event):
    try:
        if event["username"] and event["ip"] and event["status"]:
            if event['status'] == "Success" or event['status'] == "Failed":
                return True
            else:
                return False
        else:
                    return False

    except KeyError:
        return False


# sort the events in two dict list, one in valid and one in invalid
def sort_valid_events(events):

    valid = []
    invalid = []
    for event in events:
        validated_event = validate_security_event(event)
        if validated_event == True:
            valid.append(event)
        else:
            invalid.append(event)
    return valid, invalid


# counts the totals events 
def count_total_events(events):
    return len(events)


# Counts all valid events that are Failed events
def count_failed_events(events):
    sorted_ev = sort_valid_events(events)
    return len(sorted_ev[1])


# Counts all valid events that are Successful events
def count_success_events(events):
    sorted_ev = sort_valid_events(events)
    return len(sorted_ev[0])


events3 = [
    {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
    {"username": "admin", "ip": "10.0.0.5", "status": "Success"},
    {"username": "shadow", "status": "Failed"},
    {"username": "guest", "ip": "172.16.5.10", "status": "Failed"},
    {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
    {"username": "", "ip": "192.168.1.30", "status": "Failed"},
    {"username": "shadow", "ip": "192.168.1.20", "status": "Failed"},
    {"username": "backup", "ip": "10.0.0.8", "status": "Success"},
]

# Represents how many times a failed login user has attempted to attempt. 
def failed_users_attempts(events):
    sorted_evs = sort_valid_events(events)
    valid_evs = sorted_evs[0]
    failed_attempts = []
    for event in valid_evs:
        if event["status"] == "Failed":
            failed_attempts.append(event)

    unclean_results = {}
    for event in failed_attempts:
        username_value = event["username"]
        if username_value not in unclean_results:
            unclean_results[username_value] = 1
        else:
            unclean_results[username_value] += 1
    return unclean_results


# give complete analysis
def analyze_valid_events(events):

    value1 = count_total_events(events)
    value2 = count_failed_events(events)
    value3 = count_success_events(events)
    value4 = failed_users_attempts(events)
    
    analyze_result = {
        "total_events": value1,
        "failed_events": value2,
        "successful_events": value3,
        "failed_users": value4
    }
    
    return analyze_result


# find suspisious users in events with a threshold
def find_sus_users(events, threshold):
    failed_events = []
    for event in events:
        if event["status"] == "Failed":
            failed_events.append(event)
    # print(failed_events)


    unclean_results = {}
    for event in failed_events:
        username_value = event["username"]
        if username_value not in unclean_results:
            unclean_results[username_value] = 1
        else:
            unclean_results[username_value] += 1
    # print(unclean_results)


    results = {}
    for sus in unclean_results:
        if unclean_results[sus] >= threshold:
            results[sus] = unclean_results[sus]
    return results