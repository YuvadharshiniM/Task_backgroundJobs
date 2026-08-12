import frappe

def before_validate_test(doc, method):
    frappe.throw("Stopped before_validate")

def before_insert_test(doc, method):
    frappe.throw("Stopped before_insert")