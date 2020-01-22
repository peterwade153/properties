# Properties Scraper

This is a complete scrapy spider which pulls properties data .i.e houses and offices available for rent in Kampala and neighbouring districts.
The Scraped data containing property price, location, district, bedrooms, bathrooms, status whether its available for rent or sale and agent details are stored in a temporary directory `tmp` 
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

### To run the spider.
Use the command below
<pre>
scrapy crawl properties
</pre>