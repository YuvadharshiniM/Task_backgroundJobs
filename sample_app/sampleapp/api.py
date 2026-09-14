# import time
# def sample_job():
#     print("Sample Job Started")
#     time.sleep(5)
#     print("Sample Job Completed")

import frappe


@frappe.whitelist(allow_guest=True, rate_limit=5)
def limited_greeting():
    logger = frappe.logger()
    logger.info("Endpoint called.")

    frappe.response["message"] = "Hello, Rate Limited World!"