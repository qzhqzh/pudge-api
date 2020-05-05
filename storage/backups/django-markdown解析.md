[toc]

## 方法一

## 方法二：使用markdown包解析



step 1. 安装`markdown`包  

```shell script  
pip install markdown
```

step 2. 后端将md内容转换为`html`内容
```python  
from markdown import markdown~~~~

def detail(request):
    ...
    content_html = markdown(resp.data['content'],
                                extensions=[
                                    'markdown.extensions.extra',
                                    'markdown.extensions.codehilite',
                                    'markdown.extensions.toc',
                                ]
                                )
    return Response({'note': resp.data, 'page': self.page,
                         'content_html': content_html})
```
step 3. 前端展示，需要使用 safe 管道
```html
<div style="text-align: left">
    {#  <p>{{ note.content }}</p> #}
    {{ content_html|safe }}
</div>
```
