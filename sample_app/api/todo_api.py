import frappe


@frappe.whitelist()
def get_recent_todos():

    todo_list = frappe.get_list(
        "ToDo",
        fields=["name", "description", "owner"],
        order_by="creation desc",
        limit=5
    )

    for todo in todo_list:
        todo["email"] = frappe.db.get_value(
            "User",
            todo["owner"],
            "email"
        )

    return {
        "timestamp": frappe.utils.now(),
        "records": todo_list
    }