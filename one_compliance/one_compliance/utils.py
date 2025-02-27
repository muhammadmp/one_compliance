import frappe
from frappe.utils import *


@frappe.whitelist()
def create_todo(doctype, name, assign_to, owner, description):
    todo = frappe.new_doc('ToDo')
    todo.status = 'Open'
    todo.owner = owner
    todo.reference_doctype = doctype
    todo.reference_name = name
    todo.description = description
    todo.assigned_by = assign_to
    todo.date = frappe.utils.today()
    todo.save(ignore_permissions = True)
