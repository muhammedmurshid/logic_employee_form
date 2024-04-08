from odoo import http
from odoo.http import request
import io
import base64
import json
from datetime import datetime



class WebsiteForm(http.Controller):
    @http.route(['/employee_form'], type='http', auth="public", website=True)
    def appointment(self):
        partners = request.env['employee.module.form'].sudo().search([])
        branch = request.env['logic.base.branches'].sudo().search([])
        department = request.env['hr.department'].sudo().search([])
        relation = request.env['hr.employee.relation'].sudo().search([('name', '=', 'Father')])
        relation2 = request.env['hr.employee.relation'].sudo().search([('name', '=', 'Mother')])
        relation3 = request.env['hr.employee.relation'].sudo().search([])
        relation4 = request.env['hr.employee.relation'].sudo().search([])
        relation5 = request.env['hr.employee.relation'].sudo().search([])
        values = {}
        values.update({
            'partners': partners,
            'branch': branch,
            'department': department,
            'relation': relation,
            'relation2': relation2,
            'relation3': relation3,
            'relation4': relation4,
            'relation5': relation5

        })
        return request.render("logic_employee_form.employee_joining_form", values)

    @http.route(['/employee_form/submit'], type='http', csrf=False, auth='public', website=True, method=['POST'])
    def handle_file_upload(self, **kw):
        print(kw, 'kw')
        print(kw.get('father_dob'), 'dad_dob')
        print(kw.get('joining'), 'join')
        # dad_dob_date = kw.get('father_dob')
        # date_object = datetime.strptime(dad_dob_date, '%Y/%m/%d')
        # print(date_object, 'date_object')
        childes = []
        # childes.append(1)
        # childes.append(2)
        childes.append((0, 0, {
            'name': kw.get('father_name'),
            'dob': kw.get('father_dob'),
            'mobile_number': kw.get('father_number'),
            'relation': kw.get('father_relation'),

        }))
        childes.append((0, 0, {
            'name': kw.get('mother_name'),
            'dob': kw.get('mother_dob'),
            'mobile_number': kw.get('mother_number'),
            'relation': kw.get('mother_relation'),

        }))
        if kw.get('child_dob'):

            childes.append((0, 0, {
                'name': kw.get('child_name'),
                'dob': kw.get('child_dob'),
                'mobile_number': kw.get('child_number'),
                'relation': kw.get('child_relation'),

            }))
        if kw.get('child2_dob'):
            childes.append((0, 0, {
                'name': kw.get('child2_name'),
                'dob': kw.get('child2_dob'),
                'mobile_number': kw.get('child2_number'),
                'relation': kw.get('child2_relation'),

            }))
        if kw.get('child3_dob'):
            childes.append((0, 0, {
                'name': kw.get('child3_name'),
                'dob': kw.get('child3_dob'),
                'mobile_number': kw.get('child3_number'),
                'relation': kw.get('child3_relation'),

            }))

        print(childes, 'childes')



        # data = json.loads(kw['data_line_ids'])
        # val = [(0, 0, line) for line in data]
        # print(val, 'data')
        # values = {
        #     'name': kw['name'],
        #     'data_line_ids': val,
        # }
        # print(values, 'val')
        file = kw.get('upload_cv')
        photo = kw.get('upload_phone')
        paan = kw.get('upload_paan')
        aadhar = kw.get('upload_aadhar')
        baank = kw.get('upload_passbook')

        # Pass the file data to your module form
        # request.env['employee.module.form'].create({
        #     # 'name': file_name,
        #     # 'type': 'binary',
        #     'upload_cv': base64.b64encode(file.read()),
        #     'photo': base64.b64encode(photo.read()),
        #     'aadhar_photo': base64.b64encode(aadhar.read()),
        #     'pan_photo': base64.b64encode(paan.read()),
        #     'bank_passbook': base64.b64encode(baank.read()),
        # })
        # print('kkk')
        if kw.get('marital_stats') == 'married':
            field_value = kw.get('spouse_dob')
            if not field_value:
                error_message = "Please fill in the required field."
                return request.render('logic_employee_form.logic_employee_form_error', {'error_message': error_message})
            else:
                request.env['employee.module.form'].sudo().create({
                    'employee_name': kw.get('employee_name'),
                    'designation': kw.get('designation'),
                    'mail_id': kw.get('mail_id'),
                    'office_phone': kw.get('office_number'),
                    'phone_number': kw.get('phone_number'),
                    'office_mail': kw.get('office_mail_id'),
                    'address': kw.get('address'),
                    'date_of_birth': kw.get('birth'),
                    'date_of_joining': kw.get('joining'),
                    'bank_name': kw.get('bank_name'),
                    'branch_bank': kw.get('branch'),
                    'bank_acc_number': kw.get('account_number'),
                    'ifsc_code': kw.get('ifsc'),
                    'micr_code': kw.get('micr'),
                    'branch_id': kw.get('branch'),
                    'name_as_per_bank': kw.get('name_as_per_bank'),
                    'aadhar_card_number': kw.get('aadhar_number'),
                    'name_as_per_aadhar': kw.get('name_as_per_aadhar'),
                    'pan_card_number': kw.get('pan_number'),
                    'name_as_per_pan': kw.get('pan_name'),
                    'marital_stats': kw.get('marital_stats'),
                    'blood_group': kw.get('blood_group'),
                    'pf_uan_number': kw.get('pf_number'),
                    'esi_ip_number': kw.get('esi_number'),
                    ''
                    # 'father_name': kw.get('father'),
                    # 'father_number': kw.get('father_number'),
                    # 'mother_number': kw.get('mother_number'),
                    # 'mother_name': kw.get('mother'),
                    # 'father_dob': kw.get('father_dob'),
                    # 'mother_dob': kw.get('mother_dob'),
                    'spouse_dob': kw.get('spouse_dob'),
                    'spouse_name': kw.get('spouse_name'),
                    'number_of_childes': kw.get('number_of_children'),
                    'data_line_ids': childes,
                    'upload_cv': base64.b64encode(file.read()),
                    'photo': base64.b64encode(photo.read()),
                    'aadhar_photo': base64.b64encode(aadhar.read()),
                    'pan_photo': base64.b64encode(paan.read()),
                    'bank_passbook': base64.b64encode(baank.read()),
                    'gender': kw.get('gender'),
                    'department_id': kw.get('department'),
                    'work_location': kw.get('work_location'),
                    'work_place': kw.get('work_place'),
                    'highest_education_college_name': kw.get('highest_education_college'),
                    'highest_education_full_time_or_partime': kw.get('highest_education_time'),
                    'highest_education_degree': kw.get('highest_education_education'),
                    'highest_education_qualification_specialization': kw.get('highest_education_specialization'),
                    'highest_education_qualification_passed_out_month_year': kw.get('highest_education_year'),
                    'previous_employment_company_name': kw.get('previous_employment_company'),
                    'previous_employment_company_location': kw.get('previous_employment_company_location'),
                    'previous_employment_company_designation': kw.get('previous_employment_designation'),
                    'previous_employment_company_tenure': kw.get('previous_employment_company_tenure'),
                    'total_years_of_experience_before_joining_veranda': kw.get('total_years_of_experience_varanda'),
                    'emergency_contact_person_name': kw.get('emergency_contact_person_name'),
                    'emergency_contact_person_relationship': kw.get('emergency_contact_person_relationship'),
                    'emergency_contact_person_mobile_number': kw.get('emergency_contact_person_mobile_number'),
                    'emergency_contact_person_email': kw.get('emergency_contact_person_mail'),
                    'emergency_contact_person_correspondence_address': kw.get(
                        'emergency_contact_correspondence_address'),
                    'emergency_details_any_allergies_specifically': kw.get('emergency_details_any_allergies'),
                    'nominee_name': kw.get('nominee_name'),
                    'nominee_relation': kw.get('nominee_relationship'),
                    'nominee_id_proof': kw.get('nominee_id_proof')

                })
            print('married')
        else:
            request.env['employee.module.form'].sudo().create({
                'employee_name': kw.get('employee_name'),
                'designation': kw.get('designation'),
                'mail_id': kw.get('mail_id'),
                'office_phone': kw.get('office_number'),
                'phone_number': kw.get('phone_number'),
                'office_mail': kw.get('office_mail_id'),
                'address': kw.get('address'),
                'date_of_birth': kw.get('birth'),
                'date_of_joining': kw.get('joining'),
                'bank_name': kw.get('bank_name'),
                'branch_bank': kw.get('branch'),
                'bank_acc_number': kw.get('account_number'),
                'ifsc_code': kw.get('ifsc'),
                'micr_code': kw.get('micr'),
                'branch_id': kw.get('branch'),
                'data_line_ids': childes,
                'name_as_per_bank': kw.get('name_as_per_bank'),
                'aadhar_card_number': kw.get('aadhar_number'),
                'name_as_per_aadhar': kw.get('name_as_per_aadhar'),
                'pan_card_number': kw.get('pan_number'),
                'name_as_per_pan': kw.get('pan_name'),
                'marital_stats': kw.get('marital_stats'),
                'blood_group': kw.get('blood_group'),
                'pf_uan_number': kw.get('pf_number'),
                'esi_ip_number': kw.get('esi_number'),
                # 'father_name': kw.get('father'),
                # 'mother_name': kw.get('mother'),
                # 'father_number': kw.get('father_number'),
                # 'mother_number': kw.get('mother_number'),

                # 'father_dob': kw.get('father_dob'),
                # 'mother_dob': kw.get('mother_dob'),
                'name_of_children': kw.get('name_of_children'),
                'upload_cv': base64.b64encode(file.read()),
                'photo': base64.b64encode(photo.read()),
                'aadhar_photo': base64.b64encode(aadhar.read()),
                'pan_photo': base64.b64encode(paan.read()),
                'bank_passbook': base64.b64encode(baank.read()),
                'gender': kw.get('gender'),
                'department_id': kw.get('department'),
                'work_location': kw.get('work_location'),
                'work_place': kw.get('work_place'),
                'highest_education_college_name': kw.get('highest_education_college'),
                'highest_education_full_time_or_partime': kw.get('highest_education_time'),
                'highest_education_degree': kw.get('highest_education_education'),
                'highest_education_qualification_specialization': kw.get('highest_education_specialization'),
                'highest_education_qualification_passed_out_month_year': kw.get('highest_education_year'),
                'previous_employment_company_name': kw.get('previous_employment_company'),
                'previous_employment_company_location': kw.get('previous_employment_company_location'),
                'previous_employment_company_designation': kw.get('previous_employment_designation'),
                'previous_employment_company_tenure': kw.get('previous_employment_company_tenure'),
                'total_years_of_experience_before_joining_veranda': kw.get('total_years_of_experience_varanda'),
                'emergency_contact_person_name': kw.get('emergency_contact_person_name'),
                'emergency_contact_person_relationship': kw.get('emergency_contact_person_relationship'),
                'emergency_contact_person_mobile_number': kw.get('emergency_contact_person_mobile_number'),
                'emergency_contact_person_email': kw.get('emergency_contact_person_mail'),
                'emergency_contact_person_correspondence_address': kw.get('emergency_contact_correspondence_address'),
                'emergency_details_any_allergies_specifically': kw.get('emergency_details_any_allergies'),
                'nominee_name': kw.get('nominee_name'),
                'nominee_relation': kw.get('nominee_relationship'),
                'nominee_id_proof': kw.get('nominee_id_proof')
            })
            print('ok')

        return request.render("logic_employee_form.logic_employee_form_success")
        # Retrieve the file data

        # if kw.get('marital_stats') == 'married':
        #     field_value = kw.get('spouse_dob')
        #     if not field_value:
        #         error_message = "Please fill in the required field."
        #         return request.render('logic_employee_form.logic_employee_form_error', {'error_message': error_message})
        #     else:
        #         request.env['employee.module.form'].sudo().create({
        #             'employee_name': kw.get('employee_name'),
        #             'designation': kw.get('designation'),
        #             'mail_id': kw.get('mail_id'),
        #             'office_phone': kw.get('office_number'),
        #             'phone_number': kw.get('phone_number'),
        #             'office_mail': kw.get('office_mail_id'),
        #             'address': kw.get('address'),
        #             'date_of_birth': kw.get('birth'),
        #             'date_of_joining': kw.get('joining'),
        #             'bank_name': kw.get('bank_name'),
        #             'branch_bank': kw.get('branch'),
        #             'bank_acc_number': kw.get('account_number'),
        #             'ifsc_code': kw.get('ifsc'),
        #             'micr_code': kw.get('micr'),
        #             'name_as_per_bank': kw.get('name_as_per_bank'),
        #             'aadhar_card_number': kw.get('aadhar_number'),
        #             'name_as_per_aadhar': kw.get('name_as_per_aadhar'),
        #             'pan_card_number': kw.get('pan_number'),
        #             'name_as_per_pan': kw.get('pan_name'),
        #             'marital_stats': kw.get('marital_stats'),
        #             'blood_group': kw.get('blood_group'),
        #             'pf_uan_number': kw.get('pf_number'),
        #             'esi_ip_number': kw.get('esi_number'),
        #             'father_name': kw.get('father'),
        #             # 'fath_relation': father,
        #             # 'moth_relation': mother,
        #             'mother_name': kw.get('mother'),
        #             'father_dob': kw.get('father_dob'),
        #             'mother_dob': kw.get('mother_dob'),
        #             'spouse_dob': kw.get('spouse_dob'),
        #             'spouse_name': kw.get('spouse_name'),
        #             'name_of_children': kw.get('name_of_children'),
        #
        #         })
        #         print('married')
        # else:
        #     request.env['employee.module.form'].sudo().create({
        #         'employee_name': kw.get('employee_name'),
        #         'designation': kw.get('designation'),
        #         'mail_id': kw.get('mail_id'),
        #         'office_phone': kw.get('office_number'),
        #         'phone_number': kw.get('phone_number'),
        #         'office_mail': kw.get('office_mail_id'),
        #         'address': kw.get('address'),
        #         'date_of_birth': kw.get('birth'),
        #         'date_of_joining': kw.get('joining'),
        #         'bank_name': kw.get('bank_name'),
        #         'branch_bank': kw.get('branch'),
        #         'bank_acc_number': kw.get('acc_number'),
        #         'ifsc_code': kw.get('ifsc'),
        #         'micr_code': kw.get('micr'),
        #         # 'fath_relation': father,
        #         # 'moth_relation': mother,
        #         'name_as_per_bank': kw.get('name_as_per_bank'),
        #         'aadhar_card_number': kw.get('aadhar_number'),
        #         'name_as_per_aadhar': kw.get('name_as_per_aadhar'),
        #         'pan_card_number': kw.get('pan_number'),
        #         'name_as_per_pan': kw.get('pan_name'),
        #         'marital_stats': kw.get('marital_stats'),
        #         'blood_group': kw.get('blood_group'),
        #         'pf_uan_number': kw.get('pf_number'),
        #         'esi_ip_number': kw.get('esi_number'),
        #         'father_name': kw.get('father'),
        #         'mother_name': kw.get('mother'),
        #         'father_dob': kw.get('father_dob'),
        #         'mother_dob': kw.get('mother_dob'),
        #         'name_of_children': kw.get('name_of_children'),
        #         'spouse_name': kw.get('spouse_name'),
        #         # 'spouse_dob': kw.get('spouse_dob'),
        #
        #     })
        #     print('okss')
        #

        # attachment = post.get("cv")
        # file_name = attachment.cv
        #
        # return request.render("logic_employee_form.logic_employee_form_success", {"upload_cv": file_name})
