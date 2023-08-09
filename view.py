from django.core.paginator import Paginator
objects = ["john", "paul", "george", "ringo"]
p = Paginator(objects, 2)
p.count
p.num_pages
type(p.page_range)
p.page_range
range(1, 3)
page1 = p.page(1)
page1
page1.object_list
['john', 'paul']
page2 = p.page(2)
page2.object_list
['george', 'ringo']
page2.has_next()
page2.has_previous()
page2.has_other_pages()
page2.next_page_number()
page2.previous_page_number()
page2.start_index() 
page2.end_index()
p.page(0)
p.page(3)
