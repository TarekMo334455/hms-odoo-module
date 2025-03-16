from odoo import models, fields, api # type: ignore


class Department(models.Model):
    _name = "hms.department"
    _description = "Department Record"

    name = fields.Char(string="Name", required=True)
    capacity = fields.Integer(string="Capacity")
    state = fields.Selection(
        [("open", "Open"), ("closed", "Closed")],
        string="Status",
        default="open",
        required=True,
    )
    patient_ids = fields.One2many("hms.patient", "department_id", string="Patients")
