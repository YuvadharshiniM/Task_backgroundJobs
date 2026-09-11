# Copyright (c) 2026, Yuvadharshini and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Students(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		age: DF.Int
		city: DF.Data | None
		department: DF.Data | None
		gender: DF.Data | None
		marks: DF.Int
		name1: DF.Data | None
		student_id: DF.Data | None
	# end: auto-generated types

	pass
