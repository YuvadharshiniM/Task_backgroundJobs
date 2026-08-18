import frappe

logger = frappe.logger("uninstall")
logger.setLevel("INFO")

def before_migrate():
    logger.info("===== BEFORE MIGRATE TEST =====")
    print("BEFORE MIGRATE EXECUTED")


def after_migrate():
    logger.info("===== AFTER MIGRATE TEST =====")
    print("AFTER MIGRATE EXECUTED")


# def before_tests():
#     print("BEFORE TESTS HOOK IS RUNNING!")