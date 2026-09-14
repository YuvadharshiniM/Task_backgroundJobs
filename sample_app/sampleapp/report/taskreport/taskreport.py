import frappe

def execute(filters=None):
    columns = [
        {
            "label": "Customer Name",
            "fieldname": "customer_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": "Company Type",
            "fieldname": "company_type",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Customer Group",
            "fieldname": "customer_group",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Territory",
            "fieldname": "territory",
            "fieldtype": "Data",
            "width": 150
        }
    ]

    data = frappe.get_all(
        "Customer",
        fields=[
            "customer_name",
            "company_type",
            "customer_group",
            "territory"
        ]
    )

    return columns, data