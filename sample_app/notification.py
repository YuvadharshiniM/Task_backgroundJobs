def get_notification_config():
    print("Notification configuration called")

    return {
        "for_doctype": {
            "ToDo": {
                "status": "Open"
            }
        }
    }