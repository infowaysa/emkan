from . import __version__ as app_version

app_name = "emkan_einvoice"
app_title = "Emkan Einvoice"
app_publisher = "InfoWay for ICT"
app_description = "Emkan Holding E-Invoicing Customizations"
app_email = "spport@infoway.com.sa"
app_license = "MIT"

fixtures = [
    {"dt": "Property Setter", "filters": [
        ["doc_type", "in", ["Company", "Customer", "Item", "Sales Invoice"]]
    ]},
    "Custom Field",
    "Print Format",
    "Role",
    "Workspace",
    "Custom DocPerm",
    "Workflow Action Master",
    "Workflow State",
    "Workflow Action",
    "Workflow Action Permitted Role",
    "Workflow Transition",
    "Workflow",
    "Workflow Document State",
    "Client Script",
    # Add any other DocTypes or records you've customized.
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/emkan_einvoice/css/emkan_einvoice.css"
# app_include_js = "/assets/emkan_einvoice/js/emkan_einvoice.js"

# include js, css files in header of web template
# web_include_css = "/assets/emkan_einvoice/css/emkan_einvoice.css"
# web_include_js = "/assets/emkan_einvoice/js/emkan_einvoice.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "emkan_einvoice/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "emkan_einvoice.utils.jinja_methods",
#	"filters": "emkan_einvoice.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "emkan_einvoice.install.before_install"
# after_install = "emkan_einvoice.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "emkan_einvoice.uninstall.before_uninstall"
# after_uninstall = "emkan_einvoice.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "emkan_einvoice.utils.before_app_install"
# after_app_install = "emkan_einvoice.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "emkan_einvoice.utils.before_app_uninstall"
# after_app_uninstall = "emkan_einvoice.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "emkan_einvoice.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"emkan_einvoice.tasks.all"
#	],
#	"daily": [
#		"emkan_einvoice.tasks.daily"
#	],
#	"hourly": [
#		"emkan_einvoice.tasks.hourly"
#	],
#	"weekly": [
#		"emkan_einvoice.tasks.weekly"
#	],
#	"monthly": [
#		"emkan_einvoice.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "emkan_einvoice.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "emkan_einvoice.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "emkan_einvoice.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["emkan_einvoice.utils.before_request"]
# after_request = ["emkan_einvoice.utils.after_request"]

# Job Events
# ----------
# before_job = ["emkan_einvoice.utils.before_job"]
# after_job = ["emkan_einvoice.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"emkan_einvoice.auth.validate"
# ]
