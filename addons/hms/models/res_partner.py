from odoo import models, fields, api # type: ignore
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = "res.partner"

    related_patient_id = fields.Many2one(
        "hms.patient",
        string="Related Patient",
    )

    @api.constrains("related_patient_id", "email")
    def _check_patient_email(self):
        for record in self:
            if record.related_patient_id and record.email:
                other_partners = self.search(
                    [
                        ("id", "!=", record.id),
                        ("email", "=", record.email),
                        ("related_patient_id", "!=", False),
                    ]
                )

                if other_partners:
                    raise ValidationError(
                        "This email is already used by another customer with a linked patient!"

                    )

    @api.constrains("vat", "is_company")
    def _check_vat_for_crm_customers(self):
        for record in self:
            if record.is_company and not record.vat:
                raise ValidationError(" VAT is required for companies")
