# Properties Scraper

This is a complete scrapy spider which pulls properties data .i.e houses and offices available for rent in Kampala and neighbouring districts.
The Scraped data containing property price, location, district, bedrooms, bathrooms, status whether its available for rent or sale and agent details are stored in the `tem` directory
as a `properties.csv` file.

### Installation

Create a virtual env and activate it.

Clone the project
<pre>
git clone https://github.com/peterwade153/properties.git
</pre>

Install Dependencies.

<pre>
pip install requirements.txt
</pre>

### Running the spider.

<pre>
scrapy crawl properties
</pre>