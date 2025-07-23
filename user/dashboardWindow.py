from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog

from user.addDonationWindow import AddDonationWindow
from user.viewDonationsWindow import ViewDonationsWindow
'''
from user.trackDeliveryWindow import TrackDeliveryWindow
from user.makeRequestWindow import MakeRequestWindow
'''
from user.viewRequestsWindow import ViewRequestsWindow
from user.viewMatchesWindow import ViewMatchesWindow

class DashboardWindow(QDialog):
    def __init__(self, user_id=None, parent=None):
        super().__init__(parent)
        loadUi("user/dashboardWindow.ui", self)
        self.user_id = user_id

        self.addDonationButton.clicked.connect(self.openAddDonation)
        self.viewDonationsButton.clicked.connect(self.openViewDonations)
        '''
        self.trackDeliveryButton.clicked.connect(self.openTrackDelivery)
        self.makeRequestButton.clicked.connect(self.openMakeRequest)
        self.viewRequestsButton.clicked.connect(self.openViewRequests)
        self.viewMatchesButton.clicked.connect(self.openViewMatches)
        '''
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
        self.accept()

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
    