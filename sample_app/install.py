# import frappe


# def before_install():
#     print("🚀 Before Install Hook Executed")
#     print("Checking prerequisites...")


# def after_install():
#     print("✅ After Install Hook Executed")
#     # Example: Create a ToDo automatically
#     todo = frappe.get_doc({
#         "doctype": "ToDo",
#         "description": "Welcome! sample_app installed successfully."
#     })
#     todo.insert(ignore_permissions=True)
#     frappe.db.commit()
#     print("Default ToDo Created")




import frappe

def before_app_install(app_name):
    print(f"🚀 sample_app noticed that '{app_name}' is about to be installed")


def after_app_install(app_name):
    print(f"✅ sample_app noticed that '{app_name}' has been installed")