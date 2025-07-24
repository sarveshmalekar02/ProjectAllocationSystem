// Copyright (c) 2025, sarvesh and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Project", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on("Project", {
  refresh: function (frm) {
    if(!frm.is_new()){
    frm.add_custom_button("Create Project Task", () => {
      frappe.new_doc("Project Task", {
        project: frm.doc.name,
      });
    });
   }
  },
});
