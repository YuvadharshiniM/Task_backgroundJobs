# Copyright (c) 2026, Yuvadharshini and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Customers(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		company_group: DF.Data | None
		company_type: DF.Data | None
		customer_name: DF.Data | None
		territory: DF.Data | None
	# end: auto-generated types

	pass
