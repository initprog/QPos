import os
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow

from qpos import app, login
from qpos.view.main_window_ui import Ui_MainWindow

from qpos.home import Home
from qpos.dashboard import Dashboard
from qpos.lexus import Lexus
from qpos.more import More
from qpos.checkout import Checkout
from qpos.item import Item
from qpos.category import ItemCategory


class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(app.appicon())
        self.auth_user = None # current authenticated user

        ## =======================================================================================================
        ## Get all the objects in windows
        ## =======================================================================================================
        self.home_btn = self.ui.btnHome
        self.dashboard_btn = self.ui.btnDashboard
        self.checkout_btn = self.ui.btnCheckout
        self.customer_btn = self.ui.btnCustomer
        self.transaction_btn = self.ui.btnTransaction
        # Logistic submenus
        self.order_btn = self.ui.btnOrder
        self.item_btn = self.ui.btnItem
        self.invoice_btn = self.ui.btnInvoice
        self.report_btn = self.ui.btnReport
        self.vendor_btn = self.ui.btnVendor
        self.billpay_btn = self.ui.btnBillpay
        # Business submenus
        self.merchant_btn = self.ui.btnMerchant
        self.location_btn = self.ui.btnLocation
        self.team_btn = self.ui.btnTeam
        self.shift_btn = self.ui.btnShift
        self.payroll_btn = self.ui.btnPayroll
        self.bank_btn = self.ui.btnBank

        # Items
        self.item_lib_btn = self.ui.btnItemLib
        self.inv_mgt_btn = self.ui.btnInventoryMgt
        self.serv_lib_btn = self.ui.btnServiceLib
        self.modifier_btn = self.ui.btnModifier
        self.category_btn = self.ui.btnCategory
        self.discount_btn = self.ui.btnDiscount
        self.unit_btn = self.ui.btnUnit
        self.item_setting_btn = self.ui.btnItemSetting
        self.item_to_home_btn = self.ui.btnItem2Home

        ## =======================================================================================================
        ## Create dict for menu buttons and tab windows
        ## =======================================================================================================
        self.menu_btns_list = {
            self.home_btn: Home(),
            self.dashboard_btn: Dashboard(),
            self.checkout_btn: Checkout(),
            self.customer_btn: Lexus(),
            self.transaction_btn: Lexus(),

            self.order_btn: Lexus(),
            self.item_btn: Lexus(),
            self.invoice_btn: Lexus(),
            self.report_btn: Lexus(),
            self.vendor_btn: Lexus(),
            self.billpay_btn: Lexus(),

            self.merchant_btn: Lexus(),
            self.location_btn: Lexus(),
            self.team_btn: Lexus(),
            self.shift_btn: Lexus(),
            self.payroll_btn: Lexus(),
            self.bank_btn: Lexus(),

            self.item_lib_btn: Item(),
            self.inv_mgt_btn: Lexus(),
            self.serv_lib_btn: Lexus(),
            self.modifier_btn: Lexus(),
            self.category_btn: ItemCategory(),
            self.discount_btn: Lexus(),
            self.unit_btn: Lexus(),
            self.item_setting_btn: Lexus(),
            self.item_to_home_btn: Lexus(),
        }

        ## =======================================================================================================
        ## Show home window when start app
        ## =======================================================================================================
        self.show_home_window()

        ## =======================================================================================================
        ## Connect signal and slot
        ## =======================================================================================================
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)
        # General
        self.home_btn.clicked.connect(self.show_selected_window)
        self.dashboard_btn.clicked.connect(self.show_selected_window)
        self.checkout_btn.clicked.connect(self.show_selected_window)
        self.customer_btn.clicked.connect(self.show_selected_window)
        self.transaction_btn.clicked.connect(self.show_selected_window)
        # Logistic
        self.order_btn.clicked.connect(self.show_selected_window)
        self.item_btn.clicked.connect(self.switchMenu)
        self.invoice_btn.clicked.connect(self.show_selected_window)
        self.report_btn.clicked.connect(self.show_selected_window)
        self.vendor_btn.clicked.connect(self.show_selected_window)
        self.billpay_btn.clicked.connect(self.show_selected_window)
        # Business
        #self.check_user()
        self.merchant_btn.clicked.connect(self.show_selected_window)
        self.location_btn.clicked.connect(self.show_selected_window)        
        self.team_btn.clicked.connect(self.show_selected_window)
        self.shift_btn.clicked.connect(self.show_selected_window)
        self.payroll_btn.clicked.connect(self.show_selected_window)
        self.bank_btn.clicked.connect(self.show_selected_window)

        # Items
        self.item_lib_btn.clicked.connect(self.show_selected_window)
        self.inv_mgt_btn.clicked.connect(self.show_selected_window)
        self.serv_lib_btn.clicked.connect(self.show_selected_window)
        self.modifier_btn.clicked.connect(self.show_selected_window)
        self.category_btn.clicked.connect(self.show_selected_window)
        self.discount_btn.clicked.connect(self.show_selected_window)
        self.unit_btn.clicked.connect(self.show_selected_window)
        self.item_setting_btn.clicked.connect(self.show_selected_window)
        self.item_to_home_btn.clicked.connect(lambda: self.ui.stacked_menu.setCurrentIndex(0))

        vendor_sub = QtWidgets.QMenu()
        vendor_sub.addAction('Vendors', self.doVendor)
        vendor_sub.addAction('Account Payable')
        vendor_sub.addAction('Purchase Order')
        self.vendor_btn.setMenu(vendor_sub)

    def doVendor(self):
        print('vendor crud')

    def switchMenu(self):
        self.ui.stacked_menu.setCurrentIndex(1)
        
    def show_home_window(self):
        """
        Function for showing home window
        :return:
        """
        result = self.open_tab_flag(self.home_btn.text())
        self.set_btn_checked(self.home_btn)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            title = self.home_btn.text()
            curIndex = self.ui.tabWidget.addTab(Home(), title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)

    def show_selected_window(self):
        """
        Function for showing selected window
        :return:
        """
        button = self.sender()

        result = self.open_tab_flag(button.text())
        self.set_btn_checked(button)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            title = button.text()
            curIndex = self.ui.tabWidget.addTab(self.menu_btns_list[button], title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)

    def close_tab(self, index):
        """
        Function for close tab in tabWidget
        :param index: index of tab
        :return:
        """
        self.ui.tabWidget.removeTab(index)

        if self.ui.tabWidget.count() == 0:
            self.ui.toolBox.setCurrentIndex(0)
            self.show_home_window()

    def open_tab_flag(self, tab):
        """
        Check if selected window showed or not
        :param tab: tab title
        :return: bool and index
        """
        open_tab_count = self.ui.tabWidget.count()

        for i in range(open_tab_count):
            tab_name = self.ui.tabWidget.tabText(i)
            if tab_name == tab:
                return True, i
            else:
                continue

        return False,

    def set_btn_checked(self, btn):
        """
        Set the status of selected button checked and set other buttons' status unchecked
        :param btn: button object
        :return: None
        """
        for button in self.menu_btns_list.keys():
            if button != btn:
                button.setChecked(False)
            else:
                button.setChecked(True)


    def check_user(self):
        if self.auth_user == None:
            self.login = login.Login(parent=self)

        
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = MainApp()
    window.show()

    sys.exit(app.exec())
