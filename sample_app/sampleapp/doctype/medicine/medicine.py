# Copyright (c) 2026, Yuvadharshini and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Medicine(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		available_stock: DF.Int
		manufacturer: DF.Data | None
		medicine_name: DF.Data
		route: DF.Data | None
		unit_price: DF.Currency
	# end: auto-generated types

	pass
