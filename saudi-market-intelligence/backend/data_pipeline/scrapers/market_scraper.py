import asyncio
import aiohttp
import pandas as pd
from datetime import datetime
from typing import List, Dict

class MarketScraper:
    def __init__(self):
        self.session = None
        self.sources = {
            'tadawul': 'https://api.tadawul.com.sa/...',
            'investing': 'https://api.investing.com/...',
            # Add more sources here if needed
        }

    async def init_session(self):
        """Initialize the HTTP session."""
        self.session = aiohttp.ClientSession()

    async def close_session(self):
        """Close the HTTP session."""
        if self.session:
            await self.session.close()

    async def fetch_data(self, source: str, endpoint: str) -> Dict:
        """Fetch data from a source's API."""
        if not self.session:
            await self.init_session()

        async with self.session.get(f"{self.sources[source]}{endpoint}") as response:
            return await response.json()

    async def process_market_data(self, raw_data: Dict) -> pd.DataFrame:
        """Process raw market data into a clean DataFrame."""
        df = pd.DataFrame(raw_data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values('timestamp')
        return df

    async def run_pipeline(self):
        """Run the scraping pipeline to fetch and process data."""
        try:
            tasks = []
            for source in self.sources:
                tasks.append(self.fetch_data(source, '/market-data'))
            
            raw_data = await asyncio.gather(*tasks)
            processed_data = []
            
            for data in raw_data:
                df = await self.process_market_data(data)
                processed_data.append(df)
            
            # Combine data from different sources
            final_df = pd.concat(processed_data)
            return final_df
            
        finally:
            await self.close_session()

# Usage
async def main():
    scraper = MarketScraper()
    data = await scraper.run_pipeline()
    # Save data to MongoDB or other storage
    print(data.head())  # Just to see the first few rows

if __name__ == "__main__":
    asyncio.run(main())
