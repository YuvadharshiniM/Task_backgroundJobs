import frappe

def all():
    print("✅ ALL event executed")
    frappe.logger().info("ALL event executed")


def hourly():
    print("🕐 HOURLY event executed")
    frappe.logger().info("HOURLY event executed")


def daily():
    print("📅 DAILY event executed")
    frappe.logger().info("DAILY event executed")


def weekly():
    print("📖 WEEKLY event executed")
    frappe.logger().info("WEEKLY event executed")


def monthly():
    print("📦 MONTHLY event executed")
    frappe.logger().info("MONTHLY event executed")