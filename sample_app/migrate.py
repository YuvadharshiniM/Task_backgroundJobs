import frappe

def before_migrate():
    frappe.logger().info("===== BEFORE MIGRATE TEST =====")
    print("BEFORE MIGRATE EXECUTED")


def after_migrate():
    frappe.logger().info("===== AFTER MIGRATE TEST =====")
    print("AFTER MIGRATE EXECUTED")


def before_tests():
    print("🔥 BEFORE TESTS HOOK IS RUNNING!")