from frappe.utils import now

def test_now():
    current_time = now()
    print("Current time:", current_time)