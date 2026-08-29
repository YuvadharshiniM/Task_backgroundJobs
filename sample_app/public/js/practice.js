// frappe.ready(() => {
//     console.log("MY FRAPPE.READY CALLBACK");

//     console.log("WEB FORM:", frappe.web_form);

//     frappe.web_form.validate = () => {
//         alert("HOOK VALIDATE CALLED");

//         const title = frappe.web_form.get_value("title");

//         if (!title) {
//             frappe.msgprint("Please enter the Title");
//             return false;
//         }

//         return true;
//     };
// });



// frappe.call({
//     method: "sample_app.sample_app.utils.test_response",
//     callback: function(r) {
//         console.log(r);
//     }
// });


console.log("PRACTICE.JS LOADED");

frappe.call({
    method: "sample_app.utils.test_response",
    callback: function(r) {
        console.log("RESPONSE:", r);
    }
});