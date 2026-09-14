from frappe import _

def get_data():
    return [
        {
            "module_name": "Sample App",
            "category": "Modules",
            "label": _("Sample App"),
            "color": "#2490EF",
            "icon": "assets/sample_app/images/sample_app.svg",
            "type": "module",
            "description": "Sample App",
        }
    ]