frappe.pages['sample3'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'sample3',
		single_column: true
	});
}