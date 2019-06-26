#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

import functools

from dayu_widgets.alert import MAlert
from dayu_widgets.button_group import MPushButtonGroup
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.qt import QWidget, QVBoxLayout, QApplication


class AlertExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(AlertExample, self).__init__(parent)
        self.setWindowTitle('Example for MAlert')
        main_lay = QVBoxLayout()
        self.setLayout(main_lay)
        main_lay.addWidget(MDivider('different type'))
        main_lay.addWidget(MAlert(text='Information Message', parent=self).info())
        main_lay.addWidget(MAlert(text='Success Message', parent=self).success())
        main_lay.addWidget(MAlert(text='Warning Message', parent=self).warning())
        main_lay.addWidget(MAlert(text='Error Message', parent=self).error())

        closeable_alert = MAlert('Some Message', parent=self).closable()

        main_lay.addWidget(MLabel(u'不同的提示信息类型'))
        main_lay.addWidget(MDivider('closable'))
        main_lay.addWidget(closeable_alert)
        main_lay.addWidget(MDivider('data bind'))
        self.register_field('msg', '')
        self.register_field('msg_type', MAlert.InfoType)

        data_bind_alert = MAlert(parent=self)
        data_bind_alert.set_closeable(True)

        self.bind('msg', data_bind_alert, 'dayu_text')
        self.bind('msg_type', data_bind_alert, 'dayu_type')
        button_grp = MPushButtonGroup()
        button_grp.set_button_list([
            {
                'text': 'error',
                'clicked': functools.partial(self.slot_change_alert, 'password is wrong',
                                             MAlert.ErrorType)},
            {
                'text': 'success',
                'clicked': functools.partial(self.slot_change_alert, 'login success',
                                             MAlert.SuccessType)},
            {
                'text': 'no more error',
                'clicked': functools.partial(self.slot_change_alert, '', MAlert.InfoType)}
        ])
        main_lay.addWidget(button_grp)
        main_lay.addWidget(data_bind_alert)
        main_lay.addStretch()

    def slot_change_alert(self, alert_text, alert_type):
        self.set_field('msg_type', alert_type)
        self.set_field('msg', alert_text)


if __name__ == '__main__':
    import sys
    from dayu_widgets import dayu_theme

    app = QApplication(sys.argv)
    test = AlertExample()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())