import frappe

logger = frappe.logger("override")
logger.setLevel("WARNING")

@frappe.whitelist()
def get_events(start, end, user=None, for_reminder=False, filters=None):
    logger.warning("CUSTOM get_events() EXECUTED")

    return {
        "message": "MY CUSTOM get_events() IS RUNNING"
    }