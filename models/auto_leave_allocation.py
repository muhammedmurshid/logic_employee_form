from odoo import fields, models, api, _


class AutoLeaveAllocation(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def create(self, vals):
        res = super(AutoLeaveAllocation, self).create(vals)
        print('employee created')
        ss = self.env['hr.leave.allocation'].sudo().search([('holiday_type', '=', 'company'), ('state', '=', 'validate')])
        print(ss)
        for ss in ss:
            leave = self.env['hr.leave.allocation'].sudo().create({'employee_id': res.id,
                                                                   'holiday_type': 'employee',
                                                                   'holiday_status_id': ss.holiday_status_id.id,
                                                                   'name': ss.name,
                                                                   })

            leave.sudo().action_approve()
            leave.write({'state': 'confirm'})
            leave.sudo().action_validate()
        return res
