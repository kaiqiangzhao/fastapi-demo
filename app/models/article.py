#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kaiqiang.zhao


class Article(object):
    # 文章
    title = None
    index_image = None
    title_image = None
    author = None
    content = None
    creation_time = None


class ArticlePublishCalendar(object):
    # 发布的日历
    article = None
    date = None


class ParentCategory(object):
    """
    1级类目: 电影, 游戏, 软件
    2级类目: 电影名, 游戏名, 软件名
    其他标签: 电影的场景名,人物名, 游戏的场景名,人物名, 软件的页面名或按钮名
    """
    name = None


class ChildCategory(object):
    one = ParentCategory
    name = None


class ArticleCategoryShip(object):
    # 文章和标签的关系
    article = None
    tag = None


