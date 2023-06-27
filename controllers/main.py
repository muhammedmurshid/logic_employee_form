from odoo import http
from odoo.http import request
import io
import base64


class WebsiteForm(http.Controller):
    @http.route(['/employee_form'], type='http', auth="public", website=True)
    def appointment(self):
        partners = request.env['employee.module.form'].sudo().search([])
        values = {}
        values.update({
            'partners': partners
        })
        return request.render("logic_employee_form.employee_joining_form", values)

    @http.route(['/employee_form/submit'], type='http', csrf=False, auth='public', website=True, method=['POST'])
    def handle_file_upload(self, **kw):
        file_name = kw.get('upload_cv').filename
        file = kw.get('upload_cv')
        photo = kw.get('upload_phone')
        aadhar = kw.get('upload_aadhar')
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
                    'name_as_per_bank': kw.get('name_as_per_bank'),
                    'aadhar_card_number': kw.get('aadhar_number'),
                    'name_as_per_aadhar': kw.get('name_as_per_aadhar'),
                    'pan_card_number': kw.get('pan_number'),
                    'name_as_per_pan': kw.get('pan_name'),
                    'marital_stats': kw.get('marital_stats'),
                    'blood_group': kw.get('blood_group'),
                    'pf_uan_number': kw.get('pf_number'),
                    'esi_ip_number': kw.get('esi_number'),
                    'father_name': kw.get('father'),
                    'father_number': kw.get('father_number'),
                    'mother_number': kw.get('mother_number'),
                    'mother_name': kw.get('mother'),
                    'father_dob': kw.get('father_dob'),
                    'mother_dob': kw.get('mother_dob'),
                    'spouse_dob': kw.get('spouse_dob'),
                    'spouse_name': kw.get('spouse_name'),
                    'name_of_children': kw.get('name_of_children'),
                    'upload_cv': base64.b64encode(file.read()),
                    'photo': base64.b64encode(photo.read()),
                    'aadhar_photo': base64.b64encode(aadhar.read()),
                    'pan_photo': base64.b64encode(paan.read()),
                    'bank_passbook': base64.b64encode(baank.read()),

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
                'name_as_per_bank': kw.get('name_as_per_bank'),
                'aadhar_card_number': kw.get('aadhar_number'),
                'name_as_per_aadhar': kw.get('name_as_per_aadhar'),
                'pan_card_number': kw.get('pan_number'),
                'name_as_per_pan': kw.get('pan_name'),
                'marital_stats': kw.get('marital_stats'),
                'blood_group': kw.get('blood_group'),
                'pf_uan_number': kw.get('pf_number'),
                'esi_ip_number': kw.get('esi_number'),
                'father_name': kw.get('father'),
                'mother_name': kw.get('mother'),
                'father_number': kw.get('father_number'),
                'mother_number': kw.get('mother_number'),

                'father_dob': kw.get('father_dob'),
                'mother_dob': kw.get('mother_dob'),
                'name_of_children': kw.get('name_of_children'),
                'upload_cv': base64.b64encode(file.read()),
                'photo': base64.b64encode(photo.read()),
                'aadhar_photo': base64.b64encode(aadhar.read()),
                'pan_photo': base64.b64encode(paan.read()),
                'bank_passbook': base64.b64encode(baank.read()),
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
