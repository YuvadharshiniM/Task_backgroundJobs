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



from frappe.utils.pdf import get_pdf
@frappe.whitelist()
def test_get_pdf():
    html = """
        <html>
            <body>
                <h1>Test PDF</h1>
                <p>This PDF was generated using Frappe get_pdf().</p>
            </body>
        </html>
    """

    pdf = get_pdf(html)

    frappe.local.response.filename = "test.pdf"
    frappe.local.response.filecontent = pdf
    frappe.local.response.type = "download"



import frappe

# @frappe.whitelist()
# def test_response():
#     return "Hello from Frappe"

@frappe.whitelist()
def test_response():
    return "Hello"




def test_send_email():

    frappe.sendmail(
        recipients=["yuvadharshini@tridotstech.com"],
        subject="Frappe Test",
        message="Hello from Frappe!"
    )