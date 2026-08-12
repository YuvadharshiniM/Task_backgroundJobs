# Copyright (c) 2026, Yuvadharshini and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CustomerDataTest(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address: DF.SmallText | None
		customer_name: DF.Data | None
		email: DF.Data | None
		notes: DF.SmallText | None
		phone: DF.Data | None
	# end: auto-generated types

	pass
