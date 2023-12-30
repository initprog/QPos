from PyQt6.QtWidgets import QWidget
from qpos.lexus import Lexus
from qpos.category import ItemCategory
from qpos.view.more_ui import Ui_Form


class More(QWidget):
    def __init__(self):
        super(More, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ## =======================================================================================================
        ## Get all the objects in windows
        ## =======================================================================================================
        self.category_btn = self.ui.btnCategory
        self.customer_group_btn = self.ui.btnCustomerGroup
        self.warehouse_btn = self.ui.btnWarehouse
        self.payment_term_btn = self.ui.btnPaymentTerm
        self.unit_btn = self.ui.btnUnit
        self.locator_btn = self.ui.btnLocator
        self.business_hour_btn = self.ui.btnHours
        self.job_assignment_btn = self.ui.btnJobAssignment

        ## =======================================================================================================
        ## Create dict for menu buttons and tab windows
        ## =======================================================================================================
        self.more_btns_list = {
            self.category_btn: ItemCategory(),
            self.customer_group_btn: Lexus(),
            self.warehouse_btn: Lexus(),
            self.payment_term_btn: Lexus(),
            self.unit_btn: Lexus(),
            self.locator_btn: Lexus(),
            self.business_hour_btn: Lexus(),
            self.job_assignment_btn: Lexus(),
        }

        ## =======================================================================================================
        ## Connect signal and slot
        ## =======================================================================================================
        self.category_btn.clicked.connect(self.show_selected_window)
        self.customer_group_btn.clicked.connect(self.show_selected_window)
        self.warehouse_btn.clicked.connect(self.show_selected_window)
        self.payment_term_btn.clicked.connect(self.show_selected_window)
        self.unit_btn.clicked.connect(self.show_selected_window)
        self.locator_btn.clicked.connect(self.show_selected_window)
        self.business_hour_btn.clicked.connect(self.show_selected_window)
        self.job_assignment_btn.clicked.connect(self.show_selected_window)

    def show_selected_window(self):
        """
        Function for showing selected window
        :return:
        """
        button = self.sender()
        '''
        result = self.open_tab_flag(button.text())
        self.set_btn_checked(button)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            title = button.text()
            curIndex = self.ui.tabWidget.addTab(self.menu_btns_list[button], title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)
        '''