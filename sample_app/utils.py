# def before_job():
#     print("Before Job Hook Executed")

# def after_job():
#     print("After Job Hook Executed")


import frappe
from frappe.utils import now_datetime
def before_request():
    print("\n====================================")
    print("NEW REQUEST RECEIVED")
    print(f"Time   : {now_datetime()}")
    print(f"URL    : {frappe.request.path}")
    print(f"Method : {frappe.request.method}")
    print("====================================\n")
def after_request(response):
    print("\n====================================")
    print("REQUEST COMPLETED")
    print(f"Time : {now_datetime()}")
    print("====================================\n")
    return response




def greet_user(name):
    return f"Hello {name}!"



from frappe import _

def test_translation():
    return _("Hello Yuva")

