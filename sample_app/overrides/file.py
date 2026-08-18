# import frappe


# def before_write(file_size):
#     frappe.log_error(
#         title="REAL FILE HOOK FIRED",
#         message=f"Frappe called before_write_file. File size = {file_size}"
#     )



import frappe
from frappe.utils.file_manager import save_file_on_filesystem

def write_file(fname, content, content_type=None, is_private=0):
    frappe.log_error(
        title="WRITE FILE HOOK FIRED",
        message=f"""
Filename: {fname}
Content Type: {content_type}
Private: {is_private}
Content Size: {len(content)} bytes
"""
    )

    # Don't replace Frappe's actual file-writing logic yet