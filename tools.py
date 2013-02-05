#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re


#分页函数
def Pager(lists,page=1):
	count = len(lists)
	page_count = count / 10
	if count % 10 != 0:
			page_count = page_count + 1		
	if page < page_count:
		return lists[10*(page-1):10*page],page_count
	elif page == page_count:
		if count >10:
			return lists[10*(page-1):],page_count
		else:
			return lists[:],page_count


#通过正则表达式提取博文的纯文本部分(去除所有html标记)，用于首页显示summary和more
def GetSummary(content):
	result=re.sub(r'<[^>]*>','',content)
	if len(result) <= 200:
		return result
	else:
		 result = result[0:200]
		 return result
	



		