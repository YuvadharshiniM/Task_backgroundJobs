# Copyright (c) 2026, Yuvadharshini and Contributors
# See license.txt

# import frappe
from frappe.tests import IntegrationTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]



class IntegrationTestFile_hook(IntegrationTestCase):
	"""
	Integration tests for File_hook.
	Use this class for testing interactions between multiple components.
	"""

	pass
