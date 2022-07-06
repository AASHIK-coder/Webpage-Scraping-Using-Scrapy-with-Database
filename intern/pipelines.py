
from pymongo import MongoClient
from itemadapter import ItemAdapter


class InternPipeline:
     
    def open_spider(self,spider):
       self.client= MongoClient(
         host = "mongodb+srv://aashik:aashikcool@internproject1.1gb8lvp.mongodb.net/?retryWrites=true&w=majority",
           connect=False
           
       )
       
       self.collection = self.client.get_database("housing").get_collection("info")
    
    def process_item(self, item, spider):
        self.collection.insert_one(
            ItemAdapter(item).asdict()
        )
        return item
    
    def close_spider(self,spider):
        self.client.close()
   
    
