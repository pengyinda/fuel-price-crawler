# Fuel Price Crawler

This Python script is used to crawl and extract image data from the National Development and Reform Commission (NDRC) website, specifically from the fuel price adjustment information page.
## Prerequisites

- Python 3.x
- Requests library: `pip install requests`
- BeautifulSoup library: `pip install beautifulsoup4`
## Usage

1. Clone the repository:git clone https://github.com/your-username/fuel-price-crawler.git

2. Install the required libraries:pip install -r requirements.txt

3. Update the `root` variable in the script to specify the path where you want to save the downloaded images.

4. Run the script:python fuel_price_crawler.py

5. The script will print the URLs of each page (1 to 10) that it scrapes, along with the URLs of the fuel price adjustment information and image data.

6. During the image downloading process, the script will provide feedback on whether each image is successfully saved or if any errors occur.

7. The downloaded images will be saved with the date information as part of their filenames.
## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
## License

This project is licensed under the [MIT License](LICENSE).
