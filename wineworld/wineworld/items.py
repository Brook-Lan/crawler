# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WineItem(scrapy.Item):
    """酒款
    """
    mongodb_spiders = ["wine"]
    mongodb_collections = ["wineworld_wine"]

    winery = scrapy.Field()   # 酒庄
    area = scrapy.Field()    # 产区 
    area_full = scrapy.Field()    # 产区 
    url = scrapy.Field()  
    id = scrapy.Field()
    cname = scrapy.Field()
    ename = scrapy.Field()
    grapes = scrapy.Field()    # 葡萄
    cover = scrapy.Field()

    logo = scrapy.Field()
    summary = scrapy.Field()
    grapeslist = scrapy.Field()
    wine_taste = scrapy.Field()
    vintages = scrapy.Field()   # 年份


class VintAgeItem(scrapy.Item):
    """年份
    """
    mongodb_spiders = ["vintage"]
    mongodb_collections = ["wineworld_vintage"]

    vintageid = scrapy.Field()  # 年份id
    wineid = scrapy.Field()   # 酒款id
    grape = scrapy.Field()
    price = scrapy.Field()
    year = scrapy.Field()
    logo = scrapy.Field()
    taste = scrapy.Field()


class AreaRegionItem(scrapy.Item):
    """产区
    """
    mongodb_spiders = ["area"]
    mongodb_collections = ["wineworld_area_region"]

    url = scrapy.Field()
    country = scrapy.Field()
    region_name_en = scrapy.Field()
    region_name_cn = scrapy.Field()
    region_info = scrapy.Field()
    intro = scrapy.Field()


class AreaCountryItem(scrapy.Item):
    mongodb_spiders = ["area"]
    mongodb_collections = ["wineworld_area_country"]

    url = scrapy.Field()
    country_en = scrapy.Field()
    country_cn = scrapy.Field()
    intro = scrapy.Field()
    regions = scrapy.Field()


class WineryItem(scrapy.Item):
    """酒庄
    """
    mongodb_spiders = ["winery"]
    mongodb_collections = ["wineworld_winery"]

    url = scrapy.Field()
    winery_cn = scrapy.Field()    # 中文名
    winery_en = scrapy.Field()    # 英文名
    winery_img = scrapy.Field()
    intro = scrapy.Field()     # 简介
    base_info = scrapy.Field()   # 土壤类型
    extra_info = scrapy.Field()
    winery_id = scrapy.Field()


class WineryWineItem(scrapy.Item):
    """酒庄的酒款
    """
    mongodb_spiders = ["winery"]
    mongodb_collections = ["wineworld_winery_wines"]

    winery_id = scrapy.Field()    # 酒庄id
    wine_id = scrapy.Field()      # 酒款id
    

class GrapeItem(scrapy.Item):
    """葡萄
    """
    mongodb_spiders = ["grape"]
    mongodb_collections = ["wineworld_grape"]

    url = scrapy.Field()
    name_en = scrapy.Field()
    name_cn = scrapy.Field()
    attr = scrapy.Field()
    img = scrapy.Field()
    intro = scrapy.Field()


class ImageItem(scrapy.Item):
    mongodb_spiders = ["img"]
    mongodb_collections = ["wineworld_image"]

    url = scrapy.Field()    # 图片url
    image_path = scrapy.Field()   # 图片在本地的路径
