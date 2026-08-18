import frappe
from frappe.model.document import Document

logger = frappe.logger("File_hook")
logger.setLevel("INFO")

class uninstall(Document)
    def before_uninstall():
        logger.info("BEFORE UNINSTALL HOOK EXECUTED")


    def after_uninstall():
        logger.info("AFTER UNINSTALL HOOK EXECUTED")


