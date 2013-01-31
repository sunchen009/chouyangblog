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

		