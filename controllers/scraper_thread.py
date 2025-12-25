from scraper.zillow_scraper import ZillowScraper
from PySide6.QtCore import QThread, Signal

class ScraperThread(QThread):
    """Background thread for scraping"""
    progress_update = Signal(int, int)  # current_page, total_pages
    log_update = Signal(str)  # log message
    status_update = Signal(str)  # status text
    finished_scraping = Signal(list)  # results
    
    def __init__(self, location, max_pages):
        super().__init__()
        self.location = location
        self.max_pages = max_pages
        self.is_running = True # Control flag
        self.scraper = None # Will hold the scraper instance
    
    def run(self):
        """Run the scraping in background"""
        try:
            # emit starting logs
            self.log_update.emit(f"🚀 Starting scraper for {self.location}") 
            self.log_update.emit(f"📄 Will scrape {self.max_pages} page(s)")
            
            #Create scraper instance
            self.scraper = ZillowScraper(
                location=self.location, 
                max_pages=self.max_pages,
                progress_callback=self.emit_progress, 
                log_callback=self.log_update.emit 
            )
            
            results = self.scraper.scraper()
            
            self.log_update.emit(f"✅ Scraping completed! Found {len(results)} listings")
            self.finished_scraping.emit(results)

        except Exception as e:
            self.log_update.emit(f"❌ Error: {str(e)}")
            self.finished_scraping.emit([])
        finally:
            # Reset UI state even if error occurs
            pass

    def stop(self):
        """Stop the scraping"""
        self.is_running = False
        if self.scraper:
            self.scraper.should_stop = True
        self.log_update.emit("⚠️ Stopping scraper...")
    
    def emit_progress(self, current, total):
        """Helper to emit progress"""
        if self.is_running:
            self.progress_update.emit(current, total)