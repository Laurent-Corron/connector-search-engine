# -*- coding: utf-8 -*-
# Copyright 2018 ACSONE SA/NV (<http://acsone.eu>)
# Copyright 2018 Akretion (http://www.akretion.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo.addons.component.core import Component


class SeDeleter(Component):
    _name = 'se.deleter'
    _inherit = ['base.se.connector', 'base.deleter']
    _usage = 'record.exporter.deleter'

    def run(self, records):
        """
        Run the synchronization, delete the record on the backend
        :param records: recordset
        :return: bool
        """
        if records:
            return self.backend_adapter.delete(records.ids)
        return True