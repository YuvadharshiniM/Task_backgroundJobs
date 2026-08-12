frappe.ui.form.on("ToDo", {
    after_save(frm) {
        frappe.utils.play_sound("ping");
    }
});