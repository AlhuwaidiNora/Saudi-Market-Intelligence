import asyncio
import aiohttp
import pandas as pd
from datetime import datetime
from typing import Dict

# Define the Scraper Class
class MarketScraper:
    def __init__(self):
        self.session = None
        self.sources = {
            'tadawul': 'https://api.tadawul.com.sa/...',
            'investing': 'https://api.investing.com/...',
            # Add more sources
        }

    # Initialize an asynchronous session
    async def init_session(self):
        self.session = aiohttp.ClientSession()

    # Close the session after use
    async def close_session(self):
        if self.session:
            await self.session.close()

    # Fetch data from the API
    async def fetch_data(self, source: str, endpoint: str) -> Dict:
        if not self.session:
            await self.init_session()

        async with self.session.get(f"{self.sources[source]}{endpoint}") as response:
            return await response.json()

    # Process and clean the data
    async def process_market_data(self, raw_data: Dict) -> pd.DataFrame:
        # Convert raw data to DataFrame
        df = pd.DataFrame(raw_data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values('timestamp')
        return df

    # Run the entire pipeline of data fetching, processing, and combining
    async def run_pipeline(self):
        try:
            tasks = []
            for source in self.sources:
                tasks.append(self.fetch_data(source, '/market-data'))
            
            # Gather the raw data
            raw_data = await asyncio.gather(*tasks)
            processed_data = []

            # Process each source's data
            for data in raw_data:
                df = await self.process_market_data(data)
                processed_data.append(df)

            # Combine the data into one DataFrame
            final_df = pd.concat(processed_data)
            return final_df
            
        finally:
            await self.close_session()

# Main function to execute the scraper
async def main():
    scraper = MarketScraper()
    data = await scraper.run_pipeline()

    # Save the processed data to a CSV file
    data.to_csv('market_data.csv', index=False)

    print("Data saved to market_data.csv")

# Start the scraper script
if __name__ == "__main__":
    asyncio.run(main())
