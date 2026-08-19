import frappe


@frappe.whitelist()
def training_api():
    ToDo = frappe.qb.DocType("ToDo")
    User = frappe.qb.DocType("User")

    results = (
        frappe.qb.from_(ToDo)
        .join(User)
        .on(ToDo.owner == User.name)
        .select(
            ToDo.name,
            ToDo.description,
            ToDo.status,
            ToDo.owner,
            User.full_name
        )
        .limit(5)
    ).run(as_dict=True)

    if not results:
        return []

    doc = frappe.get_doc("ToDo", results[0]["name"])
    doc.status = "Closed"
    doc.save()

    for row in results:
        frappe.db.set_value(
            "ToDo",
            row["name"],
            "status",
            "Closed"
        )

    return results