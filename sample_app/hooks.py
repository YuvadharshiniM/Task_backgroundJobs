app_name = "sample_app"
app_title = "SampleApp"
app_publisher = "Yuvadharshini"
app_description = "Practice"
app_email = "yuvadharshinim05@gmail.com"
app_license = "mit"


test_string = "This is a test string"
test_dict = {"name":"Yuvadharshini"}

scheduler_events = {
	"daily": [
		"sample_app.tasks.daily_maintenance"
	]
}

app_include_js = "/assets/sample_app/js/practice.js"

# app_include_js = "custom.bundle.js"

# Apps
# ------------------

# required_apps = [ "erpnext" ]

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "sample_app",
# 		"logo": "/assets/sample_app/logo.png",
# 		"title": "SampleApp",
# 		"route": "/sample_app",
# 		"has_permission": "sample_app.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sample_app/css/sample_app.css"
# app_include_js = "/assets/sample_app/js/sample_app.js"


# include js, css files in header of web template
# web_include_css = "/assets/sample_app/css/sample_app.css"
# web_include_js = "/assets/sample_app/js/sample_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sample_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

webform_include_css = {"ToDo": "public/css/custom_todo.css"}
# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "sample_app/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------
# add methods and filters to jinja environment
jinja = {
    "methods": "sample_app.utils",
    "filters": "sample_app.filters"
}

# Installation
# ------------

before_install = "sample_app.install.before_install"
after_install = "sample_app.install.after_install"


# Uninstallation
# ------------

before_uninstall = "sample_app.uninstall.before_uninstall"
after_uninstall = "sample_app.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

before_app_install = "sample_app.install.before_app_install"
after_app_install = "sample_app.install.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sample_app.utils.before_app_uninstall"
# after_app_uninstall = "sample_app.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

after_build = "sample_app.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

notification_config = "sample_app.notification.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#     "Permission Test": "sample_app.permissions.permission_test_query_conditions"
# }

has_permission = {
    "Permission Test": "sample_app.permissions.permission_test_has_permission",
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sample_app.tasks.all"
# 	],
# 	"daily": [
# 		"sample_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"sample_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sample_app.tasks.weekly"
# 	],
# 	"monthly": [
# 		"sample_app.tasks.monthly"
# 	],
# }

# Testing 
# -------

# before_tests = "sample_app.install.before_tests"

# Extend DocType Class
# ------------------------------#not done 
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "sample_app.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------

override_whitelisted_methods = {
    "frappe.desk.doctype.event.event.get_events":
        "sample_app.event.get_events"
}

# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sample_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sample_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

ignore_links_on_delete = ["testlink2"]

# Request Events
# ----------------
before_request = ["sample_app.utils.before_request"]
after_request = ["sample_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["sample_app.utils.before_job"]
# after_job = ["sample_app.utils.after_job"]


# User Data Protection #doubt
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# user_data_fields = [
#     {
#         "doctype": "Customer Data Test",
#         "filter_by": "email",
#     }
# ]

# Authentication and authorization
# --------------------------------

auth_hooks = [
    "sample_app.auth.validate"#doubt
]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
ignore_translatable_strings_from = ["frappe"]

export_python_type_annotations = True

doc_events = {
    "ToDo": {
        "validate": "sample_app.api.customlogic.todo_validate" 
    },
    "Category": {
        "before_insert": "sample_app.events.before_insert_test"
    }
}

# on_login = "app.overrides.successful_login"
# on_session_creation = "app.overrides.allocate_free_credits"
# on_logout = "app.overrides.clear_user_cache"

#app_include_css = "/assets/sample_app/css/sample_app.css"
#app_include_js = "/assets/sample_app/js/Sample.js"
#web_include_js="/assets/sample_app/js/Website.js"

webform_include_js = {
    "Sample": "public/js/practice.js"
}

page_js = {"sample3" : "public/js/practice.js"}

#app_include_icons = "sample_app\sample_app\public\icons\sample.svg"#####doubt

website_generators = ["websiteGenerator_sample"]

# website_catch_all = "not_found"

# website_path_resolver = "sample_app.website.custom_website_path_resolver"

clear_cache = "sample_app.cache.clear_cache"

website_clear_cache = "sample_app.cache.clear_website_cache"

sounds = [
    {
        "name": "ping",
        "src": "/assets/sample_app/sounds/ping.mp3",
        "volume": 0.3
    }
]

doctype_js = {
     "Sample": "public/js/practice.js",
    "ToDo": "public/js/todo_sound.js"
}

fixtures = [
    "websiteGenerator_sample",
    "Server Script",
    "Notification"
]

before_migrate = "sample_app.migrate.before_migrate"
after_migrate = "sample_app.migrate.after_migrate"

before_tests = "sample_app.migrate.before_tests"#not done

# before_write_file = "sample_app.overrides.file.before_write"
# write_file = "sample_app.overrides.file.write_file"

extend_doctype_class = {
    "Address": ["sample_app.address.AddressMixin"]
}
# extend_doctype_class = {
#     "Address": [
#         "app.extensions.address.GeocodingMixin",
#         "app.extensions.common.ValidationMixin"
#     ],
#     "Contact": [
#         "app.extensions.common.ValidationMixin"
#     ]
# }
