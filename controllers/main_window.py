from PySide6.QtWidgets import QMainWindow, QApplication
from main_window_ui.main_ui import Ui_MainWindow
from controllers.scraper_thread import ScraperThread
from PySide6.QtCore import Qt,QSettings
from PySide6.QtWidgets import QTableWidgetItem
import time
from scraper.zillow_scraper import ZillowScraper
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up the UI 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Initialize variables
        self.scraper_thread = None
        self.results = []
        
        # Connect signals to slots
        self.connect_signals()

        self.settings = QSettings("YourCompany", "ScraperApp")

        # Load saved value (default = False)
        self.dark_mode_enabled = self.settings.value(
            "dark_mode_enabled", False, type=bool
        )

        # Apply mode on startup
        if self.dark_mode_enabled:
            self.apply_stylesheet(r"main_window_ui\dark_style.qss")
            self.ui.dark_mode.setChecked(True)

        # Connect dark mode toggle
        self.ui.dark_mode.toggled.connect(self.toggle_dark_mode)

        
    def connect_signals(self):
        """Connect UI signals to their handlers"""
        self.ui.start_button.clicked.connect(self.start_scraping)
        self.ui.stop_button.clicked.connect(self.stop_scraping)
        
        # Set initial states
        self.ui.stop_button.setEnabled(False)
        self.ui.location_input.setPlaceholderText("e.g., brooklyn-ny, manhattan-ny")
        self.ui.location_input.setText("new-york-ny")  # Default value
        
        # Initial log message
        self.log("🎯 Application ready. Configure settings and click 'Start Scraping'")

    def log(self, message):
        """Add message to log text area"""
        timestamp = time.strftime("%H:%M:%S")
        self.ui.log_text.append(f"[{timestamp}] {message}")
        # Auto-scroll to bottom
        scrollbar = self.ui.log_text.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    
    def start_scraping(self):
        """Start the scraping process"""
        # Get values from UI 
        location = self.ui.location_input.text().strip()
        max_pages = self.ui.max_pages.value()
        
        if not location:
            self.log("❌ Error: Please enter a location")
            return
        
        # Update UI state
        self.ui.start_button.setEnabled(False)
        self.ui.stop_button.setEnabled(True)
        self.ui.progressBar.setValue(0)
        
        # Clear previous results
        self.results = []
        self.ui.preview_table.setRowCount(0)
        
        # Create and start scraper thread
        self.scraper_thread = ScraperThread(location, max_pages)
        self.scraper_thread.progress_update.connect(self.update_progress)
        self.scraper_thread.log_update.connect(self.log) # Log messages
        self.scraper_thread.status_update.connect(self.update_status)
        self.scraper_thread.finished_scraping.connect(self.scraping_finished)
        self.scraper_thread.start()   

    def stop_scraping(self):
        """Stop the scraping process"""
        if self.scraper_thread and self.scraper_thread.isRunning():
            self.scraper_thread.stop()
            # self.scraper_thread.wait()  # Wait for thread to finish
            self.log("🛑 Scraping stopped by user")
            self.ui.start_button.setEnabled(True)
            self.ui.stop_button.setEnabled(False)  


    def update_progress(self, current, total):
        """Update progress bar"""
        progress = int(((current-1) / total) * 100)
        self.ui.progressBar.setValue(progress)
        self.ui.progress_page_label.setText(f"{current}/{total}")
    
    def update_status(self, status):
        """Update status label"""
        self.ui.progress_page_label.setText(status)
    
    def scraping_finished(self, results):
        """Handle completion of scraping"""
        self.results = results
        
        # Update UI state
        self.ui.start_button.setEnabled(True)
        self.ui.stop_button.setEnabled(False)
        self.ui.progressBar.setValue(100)
        self.ui.progress_page_label.setText("✅ Scraping completed!")
        QApplication.beep()
        # Update stats
        self.ui.listing_found.setText(f" {len(results)}")
        
        # Populate results table (show first 50)
        self.populate_results_table(results[:50])
        
        # Auto-save if checkbox is checked

        self.save_results()
    
    def populate_results_table(self, results):
        """Populate the results table with data"""
        self.ui.preview_table.setRowCount(len(results))

        for i, result in enumerate(results):

            # Column 0: Address
            self.ui.preview_table.setItem(
                i, 0, QTableWidgetItem(result.get("address", ""))
            )

            # Column 1: Building Name
            self.ui.preview_table.setItem(
                i, 1, QTableWidgetItem(result.get("buildingName", ""))
            )

            # Column 2: Status
            self.ui.preview_table.setItem(
                i, 2, QTableWidgetItem(result.get("status", ""))
            )

            # Column 3: Availability Count
            self.ui.preview_table.setItem(
                i, 3, QTableWidgetItem(str(result.get("availabilityCount", "")))
            )

            # Column 4: Units
            units = result.get("units", [])

            if units:
                units_text = ", ".join(
                    f"{bed}: {price}"
                    for unit in units
                    for bed, price in unit.items()
                )
            else:
                units_text = "N/A"

            self.ui.preview_table.setItem(
                i, 4, QTableWidgetItem(units_text)
            )


            # Column 5: Zipcode
            self.ui.preview_table.setItem(
                i, 5, QTableWidgetItem(result.get("zipcode", ""))
            )


            # Column 6: Detail URL
            self.ui.preview_table.setItem(
                i, 6, QTableWidgetItem(result.get("detail_url", ""))
            )

            # Column 7: Features
            features = ", ".join(result.get("features", []))
            self.ui.preview_table.setItem(i, 7, QTableWidgetItem(features))

    
    def save_results(self):
        """Save results based on selected format"""
        if not self.results:
            self.log("⚠️ No results to save")
            return
        
        scraper = ZillowScraper()
        formats_to_save = []
        
        # Check which formats are selected
        if self.ui.csv_checkBox.isChecked():
            formats_to_save.append('csv')
        if self.ui.Excel_checkBox.isChecked():
            formats_to_save.append('excel')
        if self.ui.json_checkBox.isChecked():
            formats_to_save.append('json')
        
        # If no format selected, default to CSV
        if not formats_to_save:
            formats_to_save = ['csv']
            self.log("⚠️ No format selected, defaulting to CSV")
        
        # Save in selected formats
        for fmt in formats_to_save:
            try:
                scraper.save_results(self.results, format=fmt)
                self.log(f"💾 Results saved as {fmt.upper()}")
            except Exception as e:
                self.log(f"❌ Failed to save {fmt.upper()}: {str(e)}")



    def toggle_dark_mode(self):
        """Toggle dark mode stylesheet"""
        
        if not self.dark_mode_enabled:
            print("Toggling dark mode")
            
            stylesheet_path = Path("main_window_ui") / "dark_style.qss"
            self.apply_stylesheet(str(stylesheet_path))
            self.dark_mode_enabled = True
        else:
           
            self.clear_stylesheet()
            self.dark_mode_enabled = False
        # Save preference
        self.settings.setValue("dark_mode_enabled", self.dark_mode_enabled)

    def apply_stylesheet(self, qss_file):
        """Load and apply QSS file"""

        try:
            with open(qss_file, "r", encoding="utf-8") as f:
                qss = f.read()
                QApplication.instance().setStyleSheet(qss)

        except Exception as e:
            self.log(f"Failed to load stylesheet: {e}")

    def clear_stylesheet(self):
        """Remove all stylesheets"""
        QApplication.instance().setStyleSheet("")

