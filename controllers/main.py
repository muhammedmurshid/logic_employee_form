from odoo import http
from odoo.http import request


class WebsiteForm(http.Controller):
    @http.route(['/employee_form'], type='http', auth="public", website=True)
    def appointment(self):
        partners = request.env['employee.module.form'].sudo().search([])
        values = {}
        values.update({
            'partners': partners
        })
        return request.render("logic_employee_form.employee_joining_form", values)

    @http.route(['/employee_form/submit'], type='http', auth="public", website=True, csrf=False)
    def employee_form_submit(self, **kw):
        request.env['employee.module.form'].sudo().create({
            'employee_name': kw.get('employee_name'),
            'phone_number': kw.get('phone_number'),
            'designation': kw.get('designation'),
            'date_of_joining': kw.get('joining'),
            'mail_id': kw.get('mail_id'),
            'address': kw.get('address'),
            'date_of_birth': kw.get('birth'),
            'marital_stats': kw.get('marital_stats'),
            'spouse_name': kw.get('spouse_name'),
            'name_of_children': kw.get('name_of_children'),
            'pan_card_number': kw.get('pan_number'),
            'name_as_per_pan': kw.get('pan_name'),
            'pf_uan_number': kw.get('pf_number'),
            'esi_ip_number': kw.get('esi_number'),
            'blood_group': kw.get('blood_group'),
            'name_as_per_aadhar': kw.get('name_as_per_aadhar'),
            'aadhar_card_number': kw.get('aadhar_number'),
            'bank_name': kw.get('bank_name'),
            'bank_acc_number': kw.get('account_number'),
            'branch_bank': kw.get('branch'),
            'ifsc_code': kw.get('ifsc'),
            'micr_code': kw.get('micr'),
            'name_as_per_bank': kw.get('name_as_per_bank'),
            # 'upload_cv': kw.get(file)

            # 'sale_order_id': kw.get('sale_order')
        })
        return request.render("logic_employee_form.logic_employee_form_success",{})

        # attachment = post.get("cv")
        # file_name = attachment.cv
        #
        # return request.render("logic_employee_form.logic_employee_form_success", {"upload_cv": file_name})


        # # if request.httprequest.method == 'POST' and request.httprequest.files.get('cv'):
        # #     file = request.httprequest.files.get('cv')
        #         # Read the file data
        #     # file_data = file.read()
        #
        # return request.render("logic_employee_form.logic_employee_form_success", {})
