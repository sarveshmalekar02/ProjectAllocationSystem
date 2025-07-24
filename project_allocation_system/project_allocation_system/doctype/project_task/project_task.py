# Copyright (c) 2025, sarvesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.data import getdate

class ProjectTask(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		assignee: DF.Link | None
		project_id: DF.Link
		status: DF.Literal["New", "WIP", "Under QA", "Completed"]
		task_end_date: DF.Date | None
		task_start_date: DF.Date | None
		task_title: DF.Data
	# end: auto-generated types
	
	def validate(self):
		project = frappe.get_doc("Project", self.project_id)
  
		task_start = getdate(self.task_start_date)
		task_end = getdate(self.task_end_date)
		project_start = getdate(project.start_date)
		project_expected_end = getdate(project.expected_end_date)

		if task_start < project_start:
			frappe.throw("Task Start Date must be on or after Project Start Date.")

		if task_end > project_expected_end:
			frappe.throw("Task End Date must be on or before Project Expected End Date.")
