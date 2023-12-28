from PyQt6.QtWidgets import QApplication, QMainWindow

from qpos import app, login
from qpos.view.main_window_ui import Ui_MainWindow

from qpos.home import Home
from qpos.dashboard import Dashboard
from qpos.lexus import Lexus
from qpos.checkout import Checkout
from qpos.item import Item


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
        self.home_btn = self.ui.pushButton
        self.dashboard_btn = self.ui.pushButton_2
        self.checkout_btn = self.ui.btnCheckout
        # More submenus
        self.order_btn = self.ui.btnOrder
        self.item_btn = self.ui.btnItem
        self.invoice_btn = self.ui.btnInvoice
        self.customer_btn = self.ui.btnCustomer
        self.vendor_btn = self.ui.btnVendor
        # Settings submenus
        self.merchant_btn = self.ui.btnMerchant
        self.location_btn = self.ui.btnLocation
        self.team_btn = self.ui.btnTeam
        self.shift_btn = self.ui.btnShift
        self.wage_btn = self.ui.btnWage

        ## =======================================================================================================
        ## Create dict for menu buttons and tab windows
        ## =======================================================================================================
        self.menu_btns_list = {
            self.home_btn: Home(),
            self.dashboard_btn: Dashboard(),
            self.checkout_btn: Checkout(),
            self.order_btn: Lexus(),
            self.item_btn: Item(),
            self.invoice_btn: Lexus(),
            self.customer_btn: Lexus(),
            self.vendor_btn: Lexus(),
            self.merchant_btn: Lexus(),
            self.location_btn: Lexus(),
            self.team_btn: Lexus(),
            self.shift_btn: Lexus(),
            self.wage_btn: Lexus(),
        }

        ## =======================================================================================================
        ## Show home window when start app
        ## =======================================================================================================
        self.show_home_window()

        ## =======================================================================================================
        ## Connect signal and slot
        ## =======================================================================================================
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)

        self.home_btn.clicked.connect(self.show_selected_window)
        self.dashboard_btn.clicked.connect(self.show_selected_window)
        self.checkout_btn.clicked.connect(self.show_selected_window)
        self.order_btn.clicked.connect(self.show_selected_window)
        self.item_btn.clicked.connect(self.show_selected_window)
        self.invoice_btn.clicked.connect(self.show_selected_window)
        self.customer_btn.clicked.connect(self.show_selected_window)
        self.vendor_btn.clicked.connect(self.show_selected_window)
        self.check_user()
        self.merchant_btn.clicked.connect(self.show_selected_window)
        self.location_btn.clicked.connect(self.show_selected_window)        
        self.team_btn.clicked.connect(self.show_selected_window)
        self.shift_btn.clicked.connect(self.show_selected_window)
        self.wage_btn.clicked.connect(self.show_selected_window)

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
        :return:
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
