import requests
from bs4 import BeautifulSoup
import time
import random
import json
import pandas as pd
from pathlib import Path
import logging


output_dir = Path("log")
output_dir.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO, # Capture 
    format='%(asctime)s - %(levelname)s - %(message)s', # log formate
    handlers=[
        logging.FileHandler("log/scraper.log"), # Save to a file
        logging.StreamHandler()            #  show in the terminal
    ]
)

class ZillowScraper():

    def __init__(self,location="new-york-ny", max_pages=1):
        self.BASE_URL = "https://www.zillow.com"
        self.location = location
        self.url = f"https://www.zillow.com/{location}/rentals/"
        self.max_pages = max_pages
        self.HEADERS = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }
        self.session = requests.Session()

        self.output_dir = Path("data")
        self.output_dir.mkdir(exist_ok=True)


    def fetch_html(self):
        try:
            logging.info("fetching html...")
            time.sleep(random.uniform(2, 4))
            response =self.session.get(self.url,headers=self.HEADERS,timeout=15)
            response.raise_for_status()
            return response.text

        except requests.exceptions.RequestException as e:
            logging.error(f"Request error: {e}")
            return None 

    def extract_info(self,content):
        logging.info("extracting data...")

        soup = BeautifulSoup(content, "html.parser")
        script = soup.find("script", id="__NEXT_DATA__")
        if not script:
            logging.error("Embedded JSON not found")
            return []


        data = json.loads(script.string)


        try:
            listings = data["props"]["pageProps"]["searchPageState"]["cat1"]["searchResults"]["listResults"]
        except KeyError:
            logging.error("Listings path not found")
            return []

        results = []

        for home in listings:
            units_list = [
                {
                    ("studio" if u.get("beds") == "0" else f"{u.get('beds')} beds"): u.get("price")
                }
                for u in home.get("units", [])
            ] if home.get("units") else []  
                        
            photo_data = home.get("carouselPhotosComposable", {}).get("photoData", [])
            photo_urls = [f"https://photos.zillowstatic.com/fp/{p['photoKey']}-p_e.jpg" for p in photo_data[:4]]
            
            # Extract features
            features = [rec.get("displayString") for rec in home.get("listCardRecommendation", {}).get("flexFieldRecommendations", [])]
            
            # Extract phone number if available
            phone = None
            cta_recs = home.get("listCardRecommendation", {}).get("ctaRecommendations", [])
            for cta in cta_recs:
                if cta.get("contentType") == "PHONE":
                    phone = cta.get("displayString")
                    break
            
            results.append({
                "address": home.get("address"),
                "street": home.get("addressStreet"),
                "city": home.get("addressCity"),
                "state": home.get("addressState"),
                "zipcode": home.get("addressZipcode"),
                "units": units_list,
                "latitude": home.get("latLong", {}).get("latitude"),
                "longitude": home.get("latLong", {}).get("longitude"),
                "status": home.get("statusType"),
                "buildingName": home.get("buildingName"),
                "availabilityCount": home.get("availabilityCount"),
                "detail_url": self.BASE_URL + home.get("detailUrl", ""),
                "photo_urls": photo_urls,
                
                # New useful fields
                "features": features,  # ['3D Tour', '31 available units']
                "phone": phone,  # '7189578721'
                "has_3d_tour": home.get("has3DModel", False),
                "is_featured": home.get("isFeaturedListing", False),
                "is_contactable": home.get("isContactable", False),
                "provider_listing_id": home.get("providerListingId")
            })
        return results


    def save_results(self, results, format='csv'):
        """Save results to file"""

        logging.info(f"Saving data into {format}")
        output_dir = Path("data")
        output_dir.mkdir(exist_ok=True)
        
        timestamp = time.strftime("%Y-%m-%d_at_%I-%M%p")

        try:
            if format == 'csv':
                df = pd.DataFrame(results)
                # Convert lists to strings for CSV
                df['units'] = df['units'].apply(json.dumps)
                df['features'] = df['features'].apply(json.dumps)
                df['photo_urls'] = df['photo_urls'].apply(json.dumps)
                
                filename = output_dir / f"zillow_listings_{timestamp}.csv"
                df.to_csv(filename, index=False)
                logging.info(f"Saved {len(results)} listings to {filename}")
            
            elif format == 'excel':
                df = pd.DataFrame(results)
                # Convert lists to strings for Excel
                df['units'] = df['units'].apply(json.dumps)
                df['features'] = df['features'].apply(json.dumps)
                df['photo_urls'] = df['photo_urls'].apply(json.dumps)
                
                filename = output_dir / f"zillow_listings_{timestamp}.xlsx"
                df.to_excel(filename, index=False, engine='openpyxl')
                logging.info(f"Saved {len(results)} listings to {filename}")
            
            elif format == 'json':
                filename = output_dir / f"zillow_listings_{timestamp}.json"
                with open(filename, 'w') as f:
                    json.dump(results, f, indent=2)
                logging.info(f"Saved {len(results)} listings to {filename}")
            
            else:
                logging.error(f"Unsupported format: {format}")

        except Exception as e:
            logging.error(f"❌ Failed to save {format} file: {e}")


    def scraper(self):
        all_results = []

        for page in range(1, self.max_pages + 1):
            # Build URL for current page
            url = f"{self.url}{page}_p/" if page > 1 else self.url
            logging.info(f"Scraping page {page}/{self.max_pages}")
            
            # Update the URL
            self.url = url
            
            # Fetch HTML for this page
            content = self.fetch_html()
            
            if content is None:
                logging.error(f"Failed to fetch HTML for page {page}, skipping")
                continue  # Skip to next page
            
            # Extract data from this page
            results = self.extract_info(content)
            
            if results:
                all_results.extend(results)
                logging.info(f"Extracted {len(results)} listings from page {page}")
            else:
                logging.warning(f"No listings found on page {page}")
            
            # Add delay between pages (but not after the last page)
            if page < self.max_pages:
                delay = random.uniform(3, 6)
                logging.info(f"Waiting {delay:.1f}s before next page...")
                time.sleep(delay)
        
        logging.info(f"Total: Fetched {len(all_results)} listings from {self.max_pages} page(s)")
        return all_results
        


if __name__ == "__main__":
    scraper = ZillowScraper(max_pages=2)
    results = scraper.scraper()
    
    if results:
        scraper.save_results(results, format='json')
        scraper.save_results(results, format='csv')
        scraper.save_results(results, format='excel')
        print(f"\n✅ Successfully scraped {len(results)} listings")
    else:
        print("❌ No results found")


