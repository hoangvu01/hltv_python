from hltv_scraper.scraper import HLTVScraper

if __name__ == '__main__':
    scraper = HLTVScraper() 
    scraper.fetch_results(max_result_count=230)
    print(scraper.results_df)