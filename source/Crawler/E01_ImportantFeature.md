**无财作为, 少有斗智, 既饶争时**

# SCRAPY 重要特性

### 1.spiders流程逻辑
Spider类定义了如何爬取某个(或某些)网站。包括了爬取的动作(例如:是否跟进链接)以及如何从网页的内容中提取结构化数据(爬取item)。
换句话说，Spider就是您定义爬取的动作及分析某个网页(或者是有些网页)的地方。

对spider来说，爬取的循环类似下文:

1. 以初始的URL初始化Request，并设置回调函数。
   当该request下载完毕并返回时，将生成response，并作为参数传给该回调函数。

   spider中初始的request是通过调用 `start_requests()` 来获取的。
   `start_requests()` 读取 `start_urls()` 中的URL，
   并以 `parse` 为回调函数生成 `Request` 。

2. 在回调函数内分析返回的(网页)内容，返回 `Item` 对象、`dict`、 `Request` 或者一个包括三者的可迭代容器。
   返回的Request对象之后会经过Scrapy处理，下载相应的内容，并调用设置的callback函数(函数可相同)。

3. 在回调函数内，您可以使用 `选择器(Selectors)`
   (您也可以使用BeautifulSoup, lxml 或者您想用的任何解析器) 来分析网页内容，并根据分析的数据生成item。

4. 最后，由spider返回的item将被存到数据库(由某些`Item Pipeline`处理)或使用 `Feed exports` 存入到文件中。

### 2.item pipeline
https://scrapy-chs.readthedocs.io/zh_CN/latest/topics/item-pipeline.html

一般作用：
- 清理html数据
- 验证爬取的数据
- 去重并丢弃
- 保存爬取的数据(数据库或文件)

主要函数:
- process_item(self,item,spider)
    
    必须调用的方法; 必须返回一个 `item` 对象, 或是抛出 `DropItem`
- from_settings(cls, settings)

    是一个类方法, 一般用于获取setting中的信息
- open_spide(self, spider),close_spide(self, spider)

    开启或关闭spider时调用

 配置
在setting文件配置 `ITEM_PIPELINES` 属性, 
Crawler.pipelines.CrawlerPipeline 是指定类名称, 300是优先级

    ITEM_PIPELINES = {
       'Crawler.pipelines.CrawlerPipeline': 300,
    }       

在parse(回调函数)返回 `item` 后才能生效, 一般使用 `yield item`;

<font color="red" face="KaiTi">
note: 如果后续还需使用 `item`, 则必须将spider爬取的数据返回</font>

### 3.Downloader Middleware
下载中间件, 在爬取之前, 对Request请求做一些处理;

框架默认有一些中间件, 在`DOWNLOADER_MIDDLEWARES_BASE`进行设置, 但是一般不去更改这个;
使用自己的中间件, 均在 `DOWNLOADER_MIDDLEWARES` 进行设置;如下所示 `CustomDownloaderMiddleware` 为自己编写的中间件;
后面的数字为中间件执行顺序, 数字越小, 越早执行, 设置 `None` 表示不执行

    DOWNLOADER_MIDDLEWARES = {
        'myproject.middlewares.CustomDownloaderMiddleware': 543,
    }

中间件主要包含两个函数
- process_request(self, request, spider)
    在发送请求之前对 `Request` 做一些处理, 设置代理, User-Agent等
- process_response(self, request, response, spider)
    在收到 `Response` 后, 做一些处理 
    
### 4.Item Loaders

`items` 是保存数据的容器    `ItemLoader` 是提供填充容器数据的机制

    content = ItemLoader(items=BookItem(), response=response)
    

对 `ItemLoader` 进行实例化, 参数items 为实例化的 `items` 对象, 
提供多种selecter, 对`items`中定义的变量(`book_name`)赋值(`div.info div.pub::text`);
但是无论赋值是什么, 最后结果都是一个`list`

    content.add_css("auth_info", "div.info div.pub::text")  
    content.add_xpath("book_name", "/html/head/title/text()")
    
在对应 `BookItem` 中, 可以对每个 `items` 属性做数据修改处理, 形式如下 

    from scrapy.loader.processors import MapCompose, TakeFirst
    auth_info = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip()),
        output_processor=TakeFirst()  # 取第一个元素
    )

`input_processor` 在拿到数据后处理   
`MapCompose` 是提供一系列函数依次对数据进行处理
`output_processor` 在处理完数据后, 对数据进行筛选