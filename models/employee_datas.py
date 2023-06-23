from odoo import fields, models, _


class LogicStaffInformation(models.Model):
    _inherit = 'hr.employee'

    bank_name = fields.Char(string='Bank Name')
    children_name = fields.Text(string='Children Name')
    children_birthdate = fields.Date(string='Date Of Birth Of Children')
    bank_acc_number = fields.Char(string='Account Number')
    branch_bank = fields.Char(string='Branch')
    ifsc_code = fields.Char(string='IFSC Code')
    micr_code = fields.Char(string='MICR Code')
    name_as_per_bank = fields.Char(string='Name As Per Bank Account')
    aadhar_card_number = fields.Integer(string='Aadhar Card Number')
    name_as_per_aadhar = fields.Char(string='Name As Per Aadhaar Card')
    pan_card_number = fields.Char(string='Pan Card Number')
    name_as_per_pan = fields.Char(string='Name As Per Pan Card')
    pf_uan_number = fields.Char(string='PF UAN Number')
    esi_ip_number = fields.Char(string='ESI IP Number')
    blood_group = fields.Char(string='Blood Group')
    home_address = fields.Text(string='Address')

