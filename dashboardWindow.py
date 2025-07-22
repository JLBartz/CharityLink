from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog

from addDonationWindow import AddDonationWindow
from viewDonationsWindow import ViewDonationsWindow
from trackDeliveryWindow import TrackDeliveryWindow
from makeRequestWindow import MakeRequestWindow
from viewRequestsWindow import ViewRequestsWindow
from viewMatchesWindow import ViewMatchesWindow

class DashboardWindow(QDialog):
    def __init__(self, user_id=None, parent=None):
        super().__init__(parent)
        loadUi("dashboardWindow.ui", self)
        self.user_id = user_id

        self.addDonationButton.clicked.connect(self.openAddDonation)
        self.viewDonationsButton.clicked.connect(self.openViewDonations)
        self.trackDeliveryButton.clicked.connect(self.openTrackDelivery)
        self.makeRequestButton.clicked.connect(self.openMakeRequest)
        self.viewRequestsButton.clicked.connect(self.openViewRequests)
        self.viewMatchesButton.clicked.connect(self.openViewMatches)
        self.logoutButton.clicked.connect(self.logout)

    def openAddDonation(self):
        dialog = AddDonationWindow(self.user_id, self)
        dialog.exec()

    def openViewDonations(self):
        dialog = ViewDonationsWindow(self.user_id, self)
        dialog.exec()

    def openTrackDelivery(self):
        dialog = TrackDeliveryWindow(self.user_id, self)
        dialog.exec()

    def openMakeRequest(self):
        dialog = MakeRequestWindow(self.user_id, self)
        dialog.exec()

    def openViewRequests(self):
        dialog = ViewRequestsWindow(self.user_id, self)
        dialog.exec()

    def openViewMatches(self):
        dialog = ViewMatchesWindow(self.user_id, self)
        dialog.exec()

    def logout(self):
        self.accept()
