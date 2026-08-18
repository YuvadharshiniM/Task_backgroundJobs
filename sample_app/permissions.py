# import frappe


# def permission_test_query_conditions(user):
#     print("QUERY CONDITIONS EXECUTED:", user)

#     if user == "Administrator":
#         return ""

#     return f"`tabPermission Test`.owner = {frappe.db.escape(user)}"



def permission_test_has_permission(doc, user=None, permission_type=None):

    print("===== HAS PERMISSION =====")
    print("Document:", doc.name)
    print("Document Owner:", doc.owner)
    print("User:", user)
    print("Permission Type:", permission_type)

    if user == "Administrator":
        return True

    if doc.owner == user:
        return True

    return False