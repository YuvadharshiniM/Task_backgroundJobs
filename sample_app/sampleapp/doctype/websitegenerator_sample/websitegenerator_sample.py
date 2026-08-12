# Copyright (c) 2026, Yuvadharshini and contributors
# For license information, please see license.txt

import frappe

from frappe.website.website_generator import WebsiteGenerator


class websiteGenerator_sample(WebsiteGenerator):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        author: DF.Data | None
        route: DF.Data | None
        title: DF.Data | None
    # end: auto-generated types

    def before_save(self):
        if self.title:
            self.route = frappe.scrub(self.title)