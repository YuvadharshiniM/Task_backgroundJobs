frappe.pages['university_dashboard'].on_page_load = function(wrapper) {

	let page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'University Dashboard',
		single_column: true
	});

	page.set_primary_action("Click Me", function () {
		frappe.msgprint("Hello Yuvadharshini!");
	});

	$(page.body).html(`
    <div style="padding:25px;">

        <div style="display:flex; gap:20px; margin-bottom:30px;">

            <div style="
                background:#ffffff;
                padding:20px;
                border-radius:10px;
                flex:1;
                text-align:center;
                box-shadow:0 2px 8px rgba(0,0,0,0.1);">

                <h4>Total Departments</h4>
                <h1>0</h1>

            </div>

            <div style="
                background:#ffffff;
                padding:20px;
                border-radius:10px;
                flex:1;
                text-align:center;
                box-shadow:0 2px 8px rgba(0,0,0,0.1);">

                <h4>Total Faculty</h4>
                <h1>0</h1>

            </div>

            <div style="
                background:#ffffff;
                padding:20px;
                border-radius:10px;
                flex:1;
                text-align:center;
                box-shadow:0 2px 8px rgba(0,0,0,0.1);">

                <h4>Total Courses</h4>
                <h1>0</h1>

            </div>
		<div style="
    background:#ffffff;
    padding:20px;
    border-radius:10px;
    flex:1;
    text-align:center;
    box-shadow:0 2px 8px rgba(0,0,0,0.1);">

    <h4>Total Students</h4>

    <h1 id="student-count">0</h1>

</div>

        </div>

    </div>
`);

$("#student-count").text("150");
}