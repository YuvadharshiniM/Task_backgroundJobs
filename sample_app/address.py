import frappe


class AddressMixin:

    def before_save(self):
        frappe.msgprint("Extend Doctypes - before_save() is running!")

    # def sample(self):
    #     frappe.msgprint("Hello")