frappe.ui.form.on("ToDo", {
    before_save(frm) {
        frappe.utils.play_sound("ping");
    }
});