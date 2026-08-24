
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

