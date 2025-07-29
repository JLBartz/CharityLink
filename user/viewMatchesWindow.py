import sqlite3
from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt6.uic import loadUi
from utils import apply_window_icon
import openrouteservice

ORS_API_KEY = "your_api_key_here"  # Replace with your actual key
client = openrouteservice.Client(key=ORS_API_KEY)

def get_coordinates(address):
    try:
        geocode = client.pelias_search(text=address)
        coords = geocode['features'][0]['geometry']['coordinates']
        return coords  # [longitude, latitude]
    except Exception as e:
        print(f"Geocoding error for '{address}': {e}")
        return None

def calculate_distance(start_coords, end_coords):
    try:
        result = client.directions(
            coordinates=[start_coords, end_coords],
            profile='driving-car',
            format='geojson'
        )
        distance_meters = result['features'][0]['properties']['segments'][0]['distance']
        return distance_meters / 1000  # in kilometers
    except Exception as e:
        print(f"Routing error: {e}")
        return None

class ViewMatchesWindow(QDialog):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        loadUi("user/viewMatchesWindow.ui", self)
        apply_window_icon(self)
        
        self.user_id = user_id
        self.closeButton.clicked.connect(self.close)
        self.setupTable()
        self.loadMatches()

    def setupTable(self):
        headers = ["Match ID", "Type", "Item/Request", "Status", "Matched At", "Distance (km)"]
        self.matchesTable.setColumnCount(len(headers))
        self.matchesTable.setHorizontalHeaderLabels(headers)
        self.matchesTable.setEditTriggers(self.matchesTable.EditTrigger.NoEditTriggers)

    def loadMatches(self):
        conn = sqlite3.connect("CharityLink-Updated.db")
        c = conn.cursor()

        c.execute("""
            SELECT m.id, m.match_type, di.name, gr.name, di.location, gr.location, m.status, m.matched_at
            FROM matches m
            JOIN donation_items di ON m.donation_item_id = di.id
            JOIN goods_requests gr ON m.goods_request_id = gr.id
            WHERE di.donor_id = ? OR gr.requester_id = ?
            ORDER BY m.matched_at DESC
        """, (self.user_id, self.user_id))

        results = c.fetchall()
        self.matchesTable.setRowCount(len(results))

        for row_idx, row in enumerate(results):
            match_id, match_type, donation_name, request_name, donor_location, recipient_location, status, matched_at = row
            distance = "N/A"
            start_coords = get_coordinates(donor_location)
            end_coords = get_coordinates(recipient_location)

            if start_coords and end_coords:
                dist = calculate_distance(start_coords, end_coords)
                if dist:
                    distance = f"{dist:.2f} km"

            values = [match_id, match_type, f"{donation_name} ↔ {request_name}", status, matched_at, distance]
            for col_idx, val in enumerate(values):
                self.matchesTable.setItem(row_idx, col_idx, QTableWidgetItem(str(val)))

        conn.close()