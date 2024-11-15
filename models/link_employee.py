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
           
            child_rel = self.env['hr.employee.relation'].sudo().search([('name', '=', 'Children')], limit=1)
            mom_rel = self.env['hr.employee.relation'].sudo().search([('name', '=', 'Mother')], limit=1)
            dad_rel = self.env['hr.employee.relation'].sudo().search([('name', '=', 'Father')], limit=1)
            abc = []
            for rec in self:
                # res_list = {
                #     'member_name': rec.related_employee_id.father_name,
                #     'relation_id': dad_rel.id,
                #     # 'classroom_id': self.class_room.name,
                #     'member_contact': rec.related_employee_id.father_number,
                #     'birth_date': rec.related_employee_id.father_dob,
                #
                # }
                #
                # res_list_mom = {
                #     'member_name': rec.related_employee_id.mother_name,
                #     'relation_id': mom_rel.id,
                #     # 'relation_id': 'mother',
                #     'member_contact': rec.related_employee_id.mother_number,
                #     'birth_date': rec.related_employee_id.mother_dob,
                #
                # }
                # abc.append((0, 0, res_list))
                # abc.append((0, 0, res_list_mom))
                for child in rec.related_employee_id.data_line_ids:
                    res_child = {
                        'member_name': child.name,
                        'relation_id': child.relation.id,
                        'member_contact': child.mobile_number,
                        'birth_date': child.dob,

                    }
                    abc.append((0,0, res_child))
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
            if self.related_employee_id.work_location:
                self.work_location = self.related_employee_id.work_location
            if self.related_employee_id.work_place:
                self.work_place = self.related_employee_id.work_place
            if self.related_employee_id.highest_education_college_name:
                self.highest_education_college_name = self.related_employee_id.highest_education_college_name
            if self.related_employee_id.highest_education_full_time_or_partime:
                self.highest_education_full_time_or_partime = self.related_employee_id.highest_education_full_time_or_partime
            if self.related_employee_id.highest_education_degree:
                self.highest_education_degree = self.related_employee_id.highest_education_degree
            if self.related_employee_id.highest_education_qualification_specialization:
                self.highest_education_qualification_specialization = self.related_employee_id.highest_education_qualification_specialization
            if self.related_employee_id.highest_education_qualification_passed_out_month_year:
                self.highest_education_qualification_passed_out_month_year = self.related_employee_id.highest_education_qualification_passed_out_month_year
            if self.related_employee_id.previous_employment_company_name:
                self.previous_employment_company_name = self.related_employee_id.previous_employment_company_name
            if self.related_employee_id.previous_employment_company_location:
                self.previous_employment_company_location = self.related_employee_id.previous_employment_company_location
            if self.related_employee_id.previous_employment_company_designation:
                self.previous_employment_company_designation = self.related_employee_id.previous_employment_company_designation
            if self.related_employee_id.previous_employment_company_tenure:
                self.previous_employment_company_tenure = self.related_employee_id.previous_employment_company_tenure
            if self.related_employee_id.total_years_of_experience_before_joining_veranda:
                self.total_years_of_experience_before_joining_veranda = self.related_employee_id.total_years_of_experience_before_joining_veranda
            if self.related_employee_id.emergency_contact_person_name:
                self.emergency_contact_person_name = self.related_employee_id.emergency_contact_person_name
            if self.related_employee_id.emergency_contact_person_relationship:
                self.emergency_contact_person_relationship = self.related_employee_id.emergency_contact_person_relationship

            if self.related_employee_id.department_id:
                self.department_id = self.related_employee_id.department_id.id
            if self.related_employee_id.emergency_contact_person_mobile_number:
                self.emergency_contact_person_mobile_number = self.related_employee_id.emergency_contact_person_mobile_number
            if self.related_employee_id.emergency_contact_person_email:
                self.emergency_contact_person_email = self.related_employee_id.emergency_contact_person_email
            if self.related_employee_id.emergency_contact_person_correspondence_address:
                self.emergency_contact_person_correspondence_address = self.related_employee_id.emergency_contact_person_correspondence_address
            if self.related_employee_id.emergency_details_any_allergies_specifically:
                self.emergency_details_any_allergies_specifically = self.related_employee_id.emergency_details_any_allergies_specifically
            if self.related_employee_id.nominee_name:
                self.nominee_name = self.related_employee_id.nominee_name
            if self.related_employee_id.nominee_relation:
                self.nominee_relation = self.related_employee_id.nominee_relation

            if self.related_employee_id.nominee_id_proof:
                self.nominee_id_proof = self.related_employee_id.nominee_id_proof

            self.fam_ids = abc

        else:
            raise UserError("Please Select Related Employee")
