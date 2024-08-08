# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re 
from scrapy.exceptions import DropItem


class WebscrapePipeline:
    def process_item(self, item, spider):
       return item
    

# class WebscrapePipeline:
#     def process_item(self, item, spider):
#         new=re.findall(r'Python',str(item['desc']))
#         print('pipeline executed',new)
#         if len(new)>0:
#             return item
#         else:
#             raise DropItem
        
