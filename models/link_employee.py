from odoo import api, fields, models, _
from odoo.exceptions import UserError

class LinkEmployeeJoiningForm(models.Model):
    _inherit = 'hr.employee'

    related_employee_id = fields.Many2one('employee.module.form', string="Related Employee")

    # def write(self, value):
    #     print('werytrweuriqwoq')
    #     if self.related_employee_id:
    #         employee = self.env['employee.module.form'].browse(self.related_employee_id.id)
    #
    #     return super(LinkEmployeeJoiningForm, self).write(value)

    @api.depends('related_employee_id')
    def _compute_related_fields(self):
        for rec in self:
            if rec.related_employee_id:
                rec.birthday = rec.related_employee_id.date_of_birth

    def add_related_employee(self):
        if self.related_employee_id:
            if self.related_employee_id.mail_id:
                self.work_email = self.related_employee_id.mail_id
            if self.related_employee_id.phone_number:
                self.mobile_phone = self.related_employee_id.phone_number
            if self.related_employee_id.address:
                self.home_address = self.related_employee_id.address
            if self.related_employee_id.date_of_birth:
                self.birthday = self.related_employee_id.date_of_birth
            if self.related_employee_id.date_of_joining:
                self.joining_date_cus = self.related_employee_id.date_of_joining
            if self.related_employee_id.bank_name:
                self.bank_name = self.related_employee_id.bank_name
            if self.related_employee_id.bank_acc_number:
                self.bank_acc_number = self.related_employee_id.bank_acc_number
            if self.related_employee_id.branch_bank:
                self.branch_bank = self.related_employee_id.branch_bank
            if self.related_employee_id.ifsc_code:
                self.ifsc_code = self.related_employee_id.ifsc_code
            if self.related_employee_id.micr_code:
                self.micr_code = self.related_employee_id.micr_code
            if self.related_employee_id.name_as_per_bank:
                self.name_as_per_bank = self.related_employee_id.name_as_per_bank
            if self.related_employee_id.aadhar_card_number:
                self.aadhar_card_number = self.related_employee_id.aadhar_card_number
            if self.related_employee_id.name_as_per_aadhar:
                self.name_as_per_aadhar = self.related_employee_id.name_as_per_aadhar
            if self.related_employee_id.pan_card_number:
                self.pan_card_number = self.related_employee_id.pan_card_number
            if self.related_employee_id.name_as_per_pan:
                self.name_as_per_pan = self.related_employee_id.name_as_per_pan
            if self.related_employee_id.pf_uan_number:
                self.pf_uan_number = self.related_employee_id.pf_uan_number
            if self.related_employee_id.esi_ip_number:
                self.esi_ip_number = self.related_employee_id.esi_ip_number
            if self.related_employee_id.blood_group:
                self.blood_group = self.related_employee_id.blood_group
            if self.related_employee_id.spouse_name:
                self.spouse_complete_name = self.related_employee_id.spouse_name
            if self.related_employee_id.name_of_children:
                self.children_name = self.related_employee_id.name_of_children
            if self.related_employee_id.upload_cv:
                self.upload_cv = self.related_employee_id.upload_cv
            if self.related_employee_id.aadhar_photo:
                self.aadhar_photo = self.related_employee_id.aadhar_photo
            if self.related_employee_id.pan_photo:
                self.pan_photo = self.related_employee_id.pan_photo
            if self.related_employee_id.bank_passbook:
                self.bank_passbook = self.related_employee_id.bank_passbook
            if self.related_employee_id.photo:
                self.photo = self.related_employee_id.photo
            if self.related_employee_id.marital_stats:
                self.marital = self.related_employee_id.marital_stats
            if self.related_employee_id.spouse_dob:
                self.spouse_birthdate = self.related_employee_id.spouse_dob
        else:
            raise UserError("Please Select Related Employee")

            # if self.related_employee_id.photo:
            #     self.photo = self.related_employee_id.photo,

                # self.esi_ip_number = self.related_employee_id.esi_ip_number,
            # self.blood_group = self.related_employee_id.blood_group,

            # self.spouse_birthdate = self.related_employee_id.spouse_dob,
            # self.spouse_complete_name = self.related_employee_id.spouse_name,
            # self.children_name = self.related_employee_id.name_of_children,
            # # 'fam_ids': abc,
            # self.upload_cv = self.related_employee_id.upload_cv,
            # self.aadhar_photo = self.related_employee_id.aadhar_photo,
            # self.pan_photo = self.related_employee_id.pan_photo,
            # self.bank_passbook = self.related_employee_id.bank_passbook,
            # self.photo = self.related_employee_id.photo,
            # self.private_email = self.related_employee_id.mail_id,
            # self.work_phone = self.related_employee_id.office_phone

        print('add_related_employee')


