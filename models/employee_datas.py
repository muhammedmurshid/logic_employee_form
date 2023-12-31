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
    aadhar_card_number = fields.Char(string='Aadhar Card Number')
    name_as_per_aadhar = fields.Char(string='Name As Per Aadhaar Card')
    pan_card_number = fields.Char(string='Pan Card Number')
    name_as_per_pan = fields.Char(string='Name As Per Pan Card')
    pf_uan_number = fields.Char(string='PF UAN Number')
    esi_ip_number = fields.Char(string='ESI IP Number')
    blood_group = fields.Char(string='Blood Group')
    home_address = fields.Text(string='Address')
    upload_cv = fields.Binary(string='Upload CV')
    aadhar_photo = fields.Binary(string='Aadhar Card Photo')
    pan_photo = fields.Binary(string='Pan Card Photo')
    bank_passbook = fields.Binary(string='Bank Passbook')
    photo = fields.Binary(string='Photo')

    # custody details

    custody_ids = fields.One2many('logic.staff.custody.information', 'custody_id', string='Custody')


class StaffCustodyInformation(models.Model):
    _name = 'logic.staff.custody.information'

    custody_id = fields.Many2one('hr.employee', string='Custody', ondelete='cascade')
    property = fields.Many2one('logic.custody.type', string='Property', ondelete='cascade')
    serial_number = fields.Char(string='Serial Number')
