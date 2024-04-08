from odoo import fields, models, _
import io
import cairosvg


class EmployeeModuleForm(models.Model):
    _name = 'employee.module.form'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'employee_name'
    _description = "Joining Form"
    _order = 'id desc'

    bank_name = fields.Char(string='Bank Name')
    spouse_name = fields.Char(string='Spouse Name')
    name_of_children = fields.Text(string='Name Of Childrens')
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
    employee_name = fields.Char(string='Employee Name')
    designation = fields.Char(string='Designation')
    date_of_joining = fields.Date(string='Date Of Joining')
    date_of_birth = fields.Date(string='Date Of Birth')
    mail_id = fields.Char(string='Email')
    phone_number = fields.Char(string='Personal Phone Number')
    office_phone = fields.Char(string='Office Phone Number')
    office_mail = fields.Char(string='Office Email')
    father_name = fields.Char(string='Father Name')
    mother_name = fields.Char(string='Mother Name')
    mother_dob = fields.Date(string='Mother Date Of Birth')
    father_dob = fields.Date(string='Father Date Of Birth')
    spouse_dob = fields.Date(string='Spouse Date Of Birth')
    number_of_childes = fields.Char(string='Number Of Childes')
    marital_stats = fields.Selection([('married', 'Married'), ('single', 'Unmarried')], string='Marital Status')
    address = fields.Text(string='Address')
    fath_rel = fields.Char(string='Father Relation')
    moth_rel = fields.Char(string='Mother Relation')
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', required=True, readonly=True, copy=False,
        tracking=True, default='draft')
    upload_cv = fields.Binary(string='Upload CV')
    aadhar_photo = fields.Binary(string='Aadhar Card Photo')
    pan_photo = fields.Binary(string='Pan Card Photo')
    bank_passbook = fields.Binary(string='Bank Passbook')
    photo = fields.Binary(string='Photo')
    father_number = fields.Char(string='Father Number')
    mother_number = fields.Char(string='Mother Number')
    branch_id = fields.Many2one('logic.base.branches', string='Branch')
    department_id = fields.Many2one('hr.department', string='Department')
    work_location = fields.Char(string='Work Location(city)')
    work_place = fields.Char(string='Work Place(office)')
    highest_education_college_name = fields.Char(string='Highest Education College Name')
    highest_education_full_time_or_partime = fields.Char(
        string='Highest Education Qualification - Full Time / Part Time / Distance Education')
    highest_education_degree = fields.Char(string='Highest Education Qualification - Degree')
    highest_education_qualification_specialization = fields.Char(
        string='Highest Education Qualification - Specialization')
    highest_education_qualification_passed_out_month_year = fields.Char(
        string='Highest Education Qualification - Passed Out Month Year')
    previous_employment_company_name = fields.Char(string='Previous Employment - Company Name')
    previous_employment_company_location = fields.Char(string='Previous Employment - Company Location')
    previous_employment_company_designation = fields.Char(string='Previous Employment - Company Designation')
    previous_employment_company_tenure = fields.Char(string='Previous Employment - Company Tenure')
    total_years_of_experience_before_joining_veranda = fields.Integer(
        string='Total Years Of Experience Before Joining Veranda')
    emergency_contact_person_name = fields.Char(string='Emergency Contact Person Name')
    emergency_contact_person_relationship = fields.Char(string='Emergency Contact Person Relationship')
    emergency_contact_person_mobile_number = fields.Char(string='Emergency Contact Person Mobile Number')
    emergency_contact_person_email = fields.Char(string='Emergency Contact Person Email')
    emergency_contact_person_correspondence_address = fields.Char(
        string='Emergency Contact Person Correspondence Address')
    emergency_details_any_allergies_specifically = fields.Char(string='Emergency Details - Any Allergies Specifically')
    nominee_name = fields.Char(string='Nominee Name')
    nominee_relation = fields.Char(string='Nominee Relation')
    nominee_id_proof = fields.Char(string='Nominee ID Proof Pan or Aadhar')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
    data_line_ids = fields.One2many('data.line', 'form_id', 'Data Lines')

    def confirm_employee_request(self):
        print("hr_approval")

        self.state = 'confirm'

    def cancel_employee_request(self):
        self.state = 'cancel'

    def confirm_technical_officer(self):
        # abc = []
        # for rec in self:
        #     res_list = {
        #         'member_name': rec.father_name,
        #         # 'relation_id': 'father',
        #         # 'classroom_id': self.class_room.name,
        #         'member_contact': rec.father_number,
        #         'birth_date': rec.father_dob,
        #
        #
        #     }
        #     res_list_mom = {
        #         'member_name': rec.mother_name,
        #         # 'relation_id': 'mother',
        #         'member_contact': rec.mother_number,
        #         'birth_date': rec.mother_dob,
        #
        #     }
        #     abc.append((0, 0, res_list))
        #     abc.append((0, 0, res_list_mom))
        #
        # if self.marital_stats == 'married':
        #     self.env['hr.employee'].create({
        #         'marital': 'married',
        #         'name': self.employee_name,
        #         'job_title': self.designation,
        #         'work_email': self.mail_id,
        #         'mobile_phone': self.phone_number,
        #         'home_address': self.address,
        #         'birthday': self.date_of_birth,
        #         'joining_date_cus': self.date_of_joining,
        #         'bank_name': self.bank_name,
        #         'bank_acc_number': self.bank_acc_number,
        #         'branch_bank': self.branch_bank,
        #         'ifsc_code': self.ifsc_code,
        #         'department_id': self.department_id.id,
        #         'micr_code': self.micr_code,
        #         'name_as_per_bank': self.name_as_per_bank,
        #         'aadhar_card_number': self.aadhar_card_number,
        #         'name_as_per_aadhar': self.name_as_per_aadhar,
        #         'pan_card_number': self.pan_card_number,
        #         'name_as_per_pan': self.name_as_per_pan,
        #         'pf_uan_number': self.pf_uan_number,
        #         'esi_ip_number': self.esi_ip_number,
        #         'blood_group': self.blood_group,
        #         'spouse_birthdate': self.spouse_dob,
        #         'spouse_complete_name': self.spouse_name,
        #         'children_name': self.name_of_children,
        #         'fam_ids': abc,
        #         'upload_cv': self.upload_cv,
        #         'aadhar_photo': self.aadhar_photo,
        #         'pan_photo': self.pan_photo,
        #         'bank_passbook': self.bank_passbook,
        #         'photo': self.photo,
        #         'private_email': self.mail_id,
        #         'work_phone': self.office_phone,
        #         'work_location': self.work_location,
        #         'work_place': self.work_place,
        #         'highest_education_college_name': self.highest_education_college_name,
        #         'highest_education_full_time_or_partime': self.highest_education_full_time_or_partime,
        #         'highest_education_degree': self.highest_education_degree,
        #         'highest_education_qualification_specialization': self.highest_education_qualification_specialization,
        #         'highest_education_qualification_passed_out_month_year': self.highest_education_qualification_passed_out_month_year,
        #         'previous_employment_company_name': self.previous_employment_company_name,
        #         'previous_employment_company_location': self.previous_employment_company_location,
        #         'total_years_of_experience_before_joining_veranda': self.total_years_of_experience_before_joining_veranda,
        #         'emergency_contact_person_name': self.emergency_contact_person_name,
        #         'emergency_contact_person_relationship': self.emergency_contact_person_relationship,
        #         'emergency_contact_person_mobile_number': self.emergency_contact_person_mobile_number,
        #         'emergency_contact_person_correspondence_address': self.emergency_contact_person_correspondence_address,
        #         'emergency_details_any_allergies_specifically': self.emergency_details_any_allergies_specifically,
        #         'nominee_name': self.nominee_name,
        #         'previous_employment_company_designation': self.previous_employment_company_designation,
        #         'previous_employment_company_tenure': self.previous_employment_company_tenure,
        #
        #         'nominee_relation': self.nominee_relation,
        #         'nominee_id_proof': self.nominee_id_proof,
        #
        #
        #
        #     }
        #     )
        # else:
        #     self.env['hr.employee'].create({
        #         'name': self.employee_name,
        #         'job_title': self.designation,
        #         'work_email': self.mail_id,
        #         'mobile_phone': self.phone_number,
        #         'home_address': self.address,
        #         'birthday': self.date_of_birth,
        #         'joining_date_cus': self.date_of_joining,
        #         'bank_name': self.bank_name,
        #         'bank_acc_number': self.bank_acc_number,
        #         'branch_bank': self.branch_bank,
        #         'ifsc_code': self.ifsc_code,
        #         'micr_code': self.micr_code,
        #         'name_as_per_bank': self.name_as_per_bank,
        #         'aadhar_card_number': self.aadhar_card_number,
        #         'name_as_per_aadhar': self.name_as_per_aadhar,
        #         'pan_card_number': self.pan_card_number,
        #         'name_as_per_pan': self.name_as_per_pan,
        #         'pf_uan_number': self.pf_uan_number,
        #         'esi_ip_number': self.esi_ip_number,
        #         'blood_group': self.blood_group,
        #         'fam_ids': abc,
        #         'spouse_complete_name': self.spouse_name,
        #         'children_name': self.name_of_children,
        #         'upload_cv': self.upload_cv,
        #         'aadhar_photo': self.aadhar_photo,
        #         'pan_photo': self.pan_photo,
        #         'bank_passbook': self.bank_passbook,
        #         'photo': self.photo,
        #         'private_email': self.mail_id,
        #         'work_phone': self.office_phone,
        #         'work_location': self.work_location,
        #         'work_place': self.work_place,
        #         'highest_education_college_name': self.highest_education_college_name,
        #         'highest_education_full_time_or_partime': self.highest_education_full_time_or_partime,
        #         'highest_education_degree': self.highest_education_degree,
        #         'highest_education_qualification_specialization': self.highest_education_qualification_specialization,
        #         'highest_education_qualification_passed_out_month_year': self.highest_education_qualification_passed_out_month_year,
        #         'previous_employment_company_name': self.previous_employment_company_name,
        #         'previous_employment_company_location': self.previous_employment_company_location,
        #         'total_years_of_experience_before_joining_veranda': self.total_years_of_experience_before_joining_veranda,
        #         'emergency_contact_person_name': self.emergency_contact_person_name,
        #         'emergency_contact_person_relationship': self.emergency_contact_person_relationship,
        #         'emergency_contact_person_mobile_number': self.emergency_contact_person_mobile_number,
        #         'emergency_contact_person_correspondence_address': self.emergency_contact_person_correspondence_address,
        #         'emergency_details_any_allergies_specifically': self.emergency_details_any_allergies_specifically,
        #         'nominee_name': self.nominee_name,
        #         'nominee_relation': self.nominee_relation,
        #         'nominee_id_proof': self.nominee_id_proof,
        #         'previous_employment_company_designation': self.previous_employment_company_designation,
        #         'previous_employment_company_tenure': self.previous_employment_company_tenure,
        #
        #     }
        #     )
        # activity_id = self.env['mail.activity'].search([('res_id', '=', self.id), ('user_id', '=', self.env.user.id), (
        #     'activity_type_id', '=', self.env.ref('logic_employee_form.mail_activity_joining_form').id)])
        # activity_id.action_feedback(feedback=f'Confirmed {self.env.user.name}')
        # other_activity_ids = self.env['mail.activity'].search([('res_id', '=', self.id), (
        #     'activity_type_id', '=', self.env.ref('logic_employee_form.mail_activity_joining_form').id)])
        # other_activity_ids.unlink()
        if self.mail_id:
            user = self.env['res.users'].sudo().create({
                'name': self.employee_name,
                'login': self.mail_id,
            })
        else:
            user = self.env['res.users'].sudo().create({
                'name': self.employee_name,
                'login': self.employee_name + '@mail.com',
            })
        self.state = 'done'

    def return_employee_request(self):
        activity_id = self.env['mail.activity'].search([('res_id', '=', self.id), ('user_id', '=', self.env.user.id), (
            'activity_type_id', '=', self.env.ref('logic_employee_form.mail_activity_joining_form').id)])
        activity_id.action_feedback(feedback=f'Returned {self.env.user.name}')
        other_activity_ids = self.env['mail.activity'].search([('res_id', '=', self.id), (
            'activity_type_id', '=', self.env.ref('logic_employee_form.mail_activity_joining_form').id)])
        other_activity_ids.unlink()
        self.state = 'draft'

    def technical_activity(self):
        print('hhhi')
        ss = self.env['employee.module.form'].search([])
        for i in ss:
            if i.state == 'confirm':
                users = ss.env.ref('logic_employee_form.joining_form_for_technical_officer').users
                for j in users:
                    activity_type = i.env.ref('logic_employee_form.mail_activity_joining_form')
                    i.activity_schedule('logic_employee_form.mail_activity_joining_form', user_id=j.id,
                                        note=f'Please Confirm Joining Form {j.name}')

    name_ids = fields.One2many('one.many', 'name_id', string='Name')

    def action_bulk_add_family_details(self):
        selected_records = self.env['employee.module.form'].browse(self._context.get('active_ids', []))
        selected_record_ids = selected_records.ids
        father_rel = self.env['hr.employee.relation'].search([('name', '=', 'Father')])
        mother_rel = self.env['hr.employee.relation'].search([('name', '=', 'Mother')])
        for i in selected_records:
            if i.father_name:
                i.data_line_ids = [(0, 0, {
                    'name': i.father_name,
                    'mobile_number': i.father_number,
                    'relation': father_rel.id,
                    'dob': i.father_dob,
                })]
            if i.mother_name:
                i.data_line_ids = [(0, 0, {
                    'name': i.mother_name,
                    'mobile_number': i.mother_number,
                    'dob': i.mother_dob,
                    'relation': mother_rel.id,
                })]

        print(selected_record_ids)


class OneMany(models.Model):
    _name = 'one.many'

    name = fields.Char(string='Name')
    name_id = fields.Many2one('employee.module.form', string='Name')

class DataLine(models.Model):
    _name = 'data.line'
    _description = 'Data Lines'

    name = fields.Char('Name')
    relation = fields.Many2one('hr.employee.relation', 'Relation')
    mobile_number = fields.Char('Mobile Number', widgets='phone')
    dob = fields.Date('Date of Birth')
    form_id = fields.Many2one('employee.module.form', 'Form Id', ondelete='cascade')
