from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog
from user.addDonationWindow import AddDonationWindow
from user.viewDonationsWindow import ViewDonationsWindow
from db import get_user_by_id
'''
from user.trackDeliveryWindow import TrackDeliveryWindow
from user.makeRequestWindow import MakeRequestWindow
'''
from user.viewRequestsWindow import ViewRequestsWindow
from user.viewMatchesWindow import ViewMatchesWindow
from db import log_audit_action

class DashboardWindow(QDialog):
    def __init__(self, user_id=None, login_window=None):
        super().__init__()
        loadUi("user/dashboardWindow.ui", self)

        self.user_id = user_id
        self.login_window = login_window

        if self.user_id:
            user = get_user_by_id(self.user_id)
            if user:
                self.welcomeLabel.setText(f"Welcome, {user['name']}!")

        self.addDonationButton.clicked.connect(self.openAddDonation)
        self.viewDonationsButton.clicked.connect(self.openViewDonations)
        '''
        self.trackDeliveryButton.clicked.connect(self.openTrackDelivery)
        self.makeRequestButton.clicked.connect(self.openMakeRequest)
        '''
        self.viewRequestsButton.clicked.connect(self.openViewRequests)
        self.viewMatchesButton.clicked.connect(self.openViewMatches)
    
        self.logoutButton.clicked.connect(self.logout)

    def openAddDonation(self):
        dialog = AddDonationWindow(self.user_id, self)
        dialog.exec()
    #Separate
    def openViewRequests(self):
        dialog = ViewRequestsWindow(self.user_id, self)
        dialog.exec()

    def openViewMatches(self):
        dialog = ViewMatchesWindow(self.user_id, self)
        dialog.exec()

    def logout(self):
        if self.user_id:
            log_audit_action(self.user_id, "Logout")
        self.login_window.show()
        self.close()

    def openViewDonations(self):
        dialog = ViewDonationsWindow(self.user_id, self)
        dialog.exec()
'''
    def openTrackDelivery(self):
        dialog = TrackDeliveryWindow(self.user_id, self)
        dialog.exec()

    def openMakeRequest(self):
        dialog = MakeRequestWindow(self.user_id, self)
        dialog.exec()
'''
    