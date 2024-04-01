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

    # custody details

    custody_ids = fields.One2many('logic.staff.custody.information', 'custody_id', string='Custody')


class StaffCustodyInformation(models.Model):
    _name = 'logic.staff.custody.information'

    custody_id = fields.Many2one('hr.employee', string='Custody', ondelete='cascade')
    property = fields.Many2one('logic.custody.type', string='Property', ondelete='cascade')
    serial_number = fields.Char(string='Serial Number')
