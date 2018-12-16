import scrapy
from ..items import ZufangItem
class GanjiSpider(scrapy.Spider):
    name="zufang"
    start_urls=['http://bj.ganji.com/wblist/chaoyang/zufang/']

    def parse(self, response):
        print(response)
        zf=ZufangItem();#实例化类
        title_list=response.xpath('.//div[@class="f-list-item ershoufang-list"]/dl/dd[1]/a/text()').extract()
        money_list = response.xpath('.//div[@class="f-list-item ershoufang-list"]/dl/dd[5]/div[1]/span[1]/text()').extract()
        for i,j in zip(title_list,money_list):
            zf['title']=i;
            zf['money']=j;
            yield zf;
            #yield 是一个类似 return的关键字，迭代一次遇到yield时就返回yield后面的值。重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码开始执行。