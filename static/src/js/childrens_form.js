odoo.define('logic_employee_form.childrens_form', function(require){
	"use strict";
	console.log('one2many testing')
	var publicWidget = require('web.public.widget');
	var core = require('web.core');
	var ajax = require('web.ajax');
	var rpc = require('web.rpc');
	var core = require('web.core');
	var QWeb = core.qweb;
	var _t = core._t;

	publicWidget.registry.generic_form_data = publicWidget.Widget.extend({
    	selector: '#employee_joining_form',
    	events: {
       	'click .add_total_project': '_onClickAdd_total_project',
       	'click .remove_line': '_onClickRemove_line',
       	'click .custom_create': '_onClickSubmit',
   	},

   	_onClickSubmit: async function(ev){
        	var self = this;
        	var cost_data = [];

        	_.each(rows, function(row) {
            	let child_name = $(row).find('input[name="child_name"]').val();
            	let child_age = $(row).find('input[name="child_age"]').val();
            	console.log(child_name, child_age, 'details')
            	cost_data.push({
                	'name': child_name,
                	'age': child_age,
            	});
        	});
        	$('textarea[name="data_line_ids"]').val(JSON.stringify(cost_data));

   	},

   	_onClickRemove_line: function(ev){
               $(this).parent().parent().remove();
    },

   	_onClickAdd_total_project: function(ev){
   	            console.log('button working')
            	var $new_row = $('.add_extra_project').clone(true);
            	$new_row.removeClass('d-none');
            	$new_row.removeClass('add_extra_project');
            	$new_row.addClass('project_cost_line');
            	$new_row.insertBefore($('.add_extra_project'));
            	_.each($new_row.find('td'), function(val) {
                	$(val).find('input').attr('required', 'required');
            	});
        	},

	});
});
