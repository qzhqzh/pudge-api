# django-分页

[toc]

## 理解 page_size 

page_size 是分页的每页条数，默认情况下 page_size 是 None，所以 **必须、必须、必须** 给这个变量一个值。

第一种方式：url 后面加上 ?page_size=5

第二种方式：在分页类中（比如 PageNumberPagination）设置属性 page_size=5

第三种方式：在 settings 中设置，具体是 REST_FRAMEWORK = { 'PAGE_SIZE': 5 }

