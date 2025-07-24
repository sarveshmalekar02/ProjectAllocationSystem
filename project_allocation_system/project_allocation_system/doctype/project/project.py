# Copyright (c) 2025, sarvesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Project(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        actual_end_date: DF.Date | None
        expected_end_date: DF.Date
        project_description: DF.TextEditor | None
        start_date: DF.Date
        title_of_the_project: DF.Data
    # end: auto-generated types

    def validate(self):
       
        if self.start_date > self.expected_end_date:
            frappe.throw("Project End date cannot be before Start date")
