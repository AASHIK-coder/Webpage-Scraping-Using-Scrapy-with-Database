import scrapy


class housingSpider(scrapy.Spider):
    name = "housing"
    
    start_urls = ["https://www.funda.nl/koop/heel-nederland/"]
    
    def parse(self, response):
        print ("[ here ]")
       
        houses = response.css("div.search-result-content")
        
        for house in houses:
            title = house.css("h2::text").get()
            subtitle = house.css("h4::text").get()
            price = house.css("span.search-result-price::text").get()
            area = house.css("ul span::text").get()
            owner_name = house.css("span.search-result-makelaar-name::text").get()
            
            
            print(title,subtitle,price,area,owner_name)
            
            yield {
                "title":title,
                "subtitle":subtitle,
                "price":price,
                "area":area,
                "owner_name":owner_name
            }
            
