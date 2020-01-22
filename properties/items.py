import scrapy


class PropertiesItem(scrapy.Item):
    code = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    district = scrapy.Field()
    category = scrapy.Field()
    status = scrapy.Field()
    bedrooms = scrapy.Field()
    bathrooms = scrapy.Field()
    agent = scrapy.Field()
    agent_contact = scrapy.Field()
    agent_email = scrapy.Field()
    agent_company = scrapy.Field()
