from django.shortcuts import render,HttpResponse
from django.urls import reverse # 用于url的反向解析

from app01.models import *
# Create your views here.

def special_case_2003(request):
    # request 是封装的请求对象
    print(request)
    print(request.GET)
    return HttpResponse("OK")

def login(request):

    return render(request, 'login.html')

def login_reverse(request):
    """
    URL反向解析
    """

    h = reverse('LOGIN') # 通过reverse配合url中的name就可以获得 当前的url

    return render(request, 'login_reverse.html')


def app_namespace_url(request):
    pat = reverse('app01:app_namespace_url')
    print(pat)
    return HttpResponse("app01 app_namespace_url")

def app01_url_converter_month(request, month):

    return HttpResponse(month)

def templates_lan(request):
    """
    模版语法
    {{}} 渲染变量，{%%}渲染标签
    """
    name = 'mosson'
    age = 18
    li = [1, 2, 3, 4]
    dic = {'name': 'mosson', 'age': 18}
    b = True
    return render(request, 'templates_lan.html', locals())

def orm_operator(request):
    """django orm操作练习"""
    # 1 添加记录 方式1
    # book = Book(state=1, title="Python-Book", price=100, pub_date='2018-12-12', publish='路飞')
    # book.save()
    # 1.1 添加记录 方式2 create创建表 返回值book就是刚刚新生成的表记录
    # book = Book.objects.create(state=1, title="Go-Book", price=150, pub_date='2018-2-12', publish='老男孩')

    # 2 查询表记录
    # 2.1 all() 返回值是queryset对象
    # book_list = Book.objects.all()
    # print(book_list)  # [obj1, obj2]
    # 2.2 first last 调用者是queryset
    # book = Book.objects.all().first()
    # book = Book.objects.all().last()
    # 2.3 filter() 返回值是 queryset对象
    # book_list = Book.objects.filter(price=100)
    # print(book_list)
    # 2.4 get  有且只有一个的结果时才有意义，返回值是 model对象
    # book = Book.objects.get(name='Go-Book')
    # 2.5 exclude 返回值是queryset
    # res = Book.objects.exclude(title='go') # 查询出title不等于go的书籍
    # print(res)
    # 2.6 order_by 调用者queryset返回值也是queryset
    # ret = Book.objects.all().order_by('-id') # - 表示倒序
    # ret = Book.objects.all().order_by('price', 'id') # price 排序如果重了 再按照id排序
    # 2。7 count 调用者是 queryset
    # ret =Book.objects.all().count()
    # 2。8 exist
    # 2.9 values 方法 调用者是queryset 返回值也是queryset
    # book = Book.objects.all().values('price')
    # book = Book.objects.values('price') # 不加all也一样
    # print(book)#<QuerySet [{'price': Decimal('100.00')}, {'price': Decimal('150.00')}]>
    # 2。10 values_list
    # book = Book.objects.all().values_list('price', 'title')
    # print(book) #<QuerySet [(Decimal('100.00'), 'Python-Book'), (Decimal('150.00'), 'Go-Book')]>
    # 2.11 distinct 去重 配合这values values_list
    # ret = Book.objects.all().values('price').distinct()
    # =================================== 模糊查询 =======
    '''
    orm中 __gt= 表示大于
          __lt= 表示小于   
          __startwith= 表示以xx开头
          __contains= 表示该字段包含xx 
          __icontains= 表示该字段包含xx 不区分大小写
          price__in=[100, 200, 300] 价格是100 200 300 的
          __year=2018 筛选2018年的
    '''
    #####  删除修改
    # Book.objects.filter(price=200).delete() # queryset调用delete（）
    # Book.objects.filter(price=100).first().delete()
    ##### 修改操作 update的调用对象一定是queryset
    # ret = Book.objects.update(title='python').update(title='go')

    return HttpResponse('OK')

def orm_mul_table(request):
    # ======= 单表添加记录
    # 添加出版社信息
    # pub = Publish.objects.create(name='人民出版社', email='123@qq.com', city='北京')
    # 添加书本信息
    # 1 为book绑定出版社 方式1
    # book = Book.objects.create(title='西游记', price=150, publishDate='2019-01-01', publish_id=1)
    # pubobj = Publish.objects.filter(nid=1).first()
    # book = Book.objects.create(title='水浒传', price=150, publishDate='2019-01-01', publish=pubobj)
    # 查询西游记的出版社对应的邮箱
    # book_obj = Book.objects.filter(title='西游记').first()
    # print(book_obj.publish.email)

    #======================= 一对多 （一个出版社可以对应多本书）
    # 一旦确定表的关系是一对多，在多对应的表中创建关联字段

    # ====================== 多对多 （多个作者可以对应多本书）
    # 一旦确定表关系是多对多，就需要创建第三张表（作为多对多的关系表）
    # 为书添加作者
    # book_obj = Book.objects.filter(title='红楼梦').first()
    # alex = Author.objects.get(name='alex')
    # mosson = Author.objects.get(name='mosson')
    # # 绑定多对多关系的API接口
    # book_obj.authors.add(alex, mosson)
    # 解除多对多的关系
    # bookobj = Book.objects.filter(title='红楼梦').first()
    # bookobj.authors.remove(3) #解除多对多关系 1（book_id）， 3(author_id)
    # 解除所有的关系
    # bookobj.authors.clear()
    # 获取与本书相关的所有的作者对象
    # authors_obj= bookobj.authors.all()
    # 获取作者的名字
    # authors_obj = bookobj.authors.all().values('name')

    # ====================== 一对一 （作者和作者的详细信息表）
    # 一旦确定表的关系是一对一，关联字段在哪个表都无所谓

    # =================  基于对象的跨表查询 （双下划线 join查询 ）（基于对象的 属于子查询）


    return render(request, 'orm_mul_table.html')

def orm_query(request):
    # ============= ORM 的跨表查询
    """
    1 基于对象的 2 基于双下划线 3 聚合的分组 4 F与Q查询
    """
    """
    表A 表B 关联属性在A表中
    正向查询：A===》B
    反向查询：B===》A
    # 一对多查询
    正向查询：A===》B 按照字段
    反向查询：B===》A 按照表名小写_set
    """
    # =================== 1 基于对象的跨表查询 ====================
    # 1.1 一对多的正向查询(按照字段)  查询红楼梦这本书的出版社的名字
    # bookobj = Book.objects.filter(title='红楼梦').first()
    # print(bookobj.publish.name)

    # 1.2 一对多的反向查询(按照表名小写_set)  查询人民出版社，出版的书籍的名称
    # pubobj = Publish.objects.filter(name='人民出版社').first()
    # print(pubobj.book_set.all())

    # 1.3 多对多的正向跨表查询（按照字段），书籍找作者，查询红楼梦的作者名字
    # bookobj = Book.objects.filter(title='红楼梦').first()
    # print(bookobj.authors.all().values('name'))

    # 1.4 多对多的反向跨表查询（按照字段），作者找书籍，查询alex出版的所有书籍
    # author = Author.objects.filter(name='alex').first()
    # print(author.book_set.all().values('title'))

    # 1.5 一对一的正向查询（按照字段）alex的详细对象的手机号
    # alex = Author.objects.filter(name='alex').first()
    # print(alex.authordetail.telephone)

    # 1.6 一对一的方向查询（按照表名小写）查询手机号16877888899用户的名字
    # _detail = AuthorDetail.objects.filter(telphone='16877888899').first()
    # print(_detail.author.name)

    # ======================== 基于双下划线的跨表查询 join
    """
    正向查询按字段，反向查询按照表名小写来告诉orm引擎join哪一张表
    """
    # 2.1 一对多的正向查询：查询红楼梦这本书的出版社的名字
    # ret = Book.objects.filter(title='红楼梦').values('publish__name')
    # print(ret) # ret 是一个queryset对象
    # 方式2
    # ret = Publish.objects.filter(book__title="红楼梦").values('name')
    # print(ret)
    # 2.2 多对多（相当于跨两张表）查询红楼梦这本书所有的作者
    # 方式1 正向查询 通过book表join与其关联的author表
    # ret = Book.objects.filter(title="红楼梦").values('authors__name')
    # print(ret)
    # 方式2 反向查询（表名小写）
    # ret = Author.objects.filter(book__title="红楼梦").values('name')
    # print(ret)
    # 2.3 一对一查询
    # 方式 1 正向查找 alex的手机号
    # alex = Author.objects.filter(name='alex').values('authordetail__telphone')
    # print(alex)
    # 方式 2 反向查找 alex的手机号
    # alex = AuthorDetail.objects.filter(author__name='alex').values('telphone')
    # print(alex)
    # ====================== 连续跨表查询
    # 3.1 手机号以138开头的作者出版过的所有的书籍的名称以及出版社的名称
    # 方式 1
    # Book.objects.filter(authors__authordetail__telphone__startwith='138').values('title', 'publish__name')
    # 方式 2
    # Author.objects.filter(authordetail__telphone__startwith='138').values('book__title', 'book_publish__name')

    # ========================= 聚合、分组查询 ===================
    # 聚合函数 aggregate 返回值是一个字典
    from django.db.models import Avg, Max, Min, Count

    # 聚合查询  1 查询所有书籍的平均价
    # ret = Book.objects.all().aggregate(avg_price=Avg("price"))
    # =====================  分组查询  annotate 返回值是一个queryset
    # 单表分组查询示例1 查询部门的名称以及员工的平均薪水
    # select dep, Avg(salary) from emp group_by dep;
    # ret = Emp.objects.values('dep').annotate(avg_salary=Avg('salary'))
    """ 对应的sql
    SELECT `app01_emp`.`dep`, AVG(`app01_emp`.`salary`) AS `avg_salary` FROM
     `app01_emp` GROUP BY `app01_emp`.`dep` 
     ORDER BY NULL LIMIT 21; args=()

    """
    # 单表的分组查询ORM语法总结：
    """
    单表.objects.values('group by 的字段').annotate(聚合函数('统计字段'))
    """
    # 单表分组查询示例2
    # 查询每一个省份的名称以及对应的员工数
    # Emp.objects.values('province').annotate(count=Count('people'))
    # 补充知识点
    # select 字段(select的哪一个字段就是按照哪一个字段进行分组)

    # 3.1 多表(跨表)分组查询
    # 查询每一个出版社的名称以及出版的书籍个数
    """sql
    select publish.name, Count("title") from Book inner join Publish on book.publish_id=publish.id group by publish.id
    
    """
    # orm 方式1
    # ret = Publish.objects.values('nid').annotate(count=Count('book__title'))
    # orm 方式2
    # ret = Publish.objects.values('nid').annotate(count=Count('book__title')).values('name', 'count')# 需要哪一个字段就在values里面添加

    # 3.2 查询出版社的名字以及书籍的最高价格
    """sql
    select app01_author.name,Max(app01_book.price) from app01_book inner join app01_book_authors on app01_book.nid=app01_book_authors.book_id
    inner join app01_author on app01_author.nid=app01_book_author.author_id
    group by app01_author.nid
    """
    # orm
    Author.objects.values('pk').annotate(max_price=Max('book__price')).values('name', 'max_price')
    # 总结 跨表的分组查询
    """ 总结
    每一个表模型.objects.values('pk').annotate(聚合函数(关联表__统计字段)).values('表模型的所有字段')
    每一个表模型.objects.annotate(聚合函数(关联表__统计字段)).values('表模型的所有字段').values('表模型的所有字段')
    """
    # 3.3 查询每一个书籍的名称以及对应的作者个数
    ret = Book.objects.values('pk').annotate(count_authors=Count('authors__name')).values('title', 'count_authors')

    # 3.4 统计一本以py开头的书籍的作者个数
    ret = Book.objects.filter(title__startwith='py').annotate(authors_num=Count('authors'))

    # 3.5 统计不止一个作业的图书
    ret = Book.objects.annotate(author_num=Count('authors')).filter(author_num__gt=1)
    ######### F 查询
    from django.db.models import F, Q
    # F 用法1 查询评论数大于阅读数的书籍
    ret = Book.objects.filter(comment_num__gt=F('read_num'))
    # F 用法2 所有书籍的价格都加10元
    ret = Book.objects.all().update(price=F('price')+1)

    ########## Q 查询
    # Q 方法1 查询书名是红楼梦或者价格为 100的书籍
    ret = Book.objects.filter(Q(title='红楼梦')|Q(price=100))
    # Q 方法1 查询书名是红楼梦且价格为 100的书籍
    ret = Book.objects.filter(Q(title='红楼梦')&Q(price=100))
    # 注意1  ～ 表示取反
    # 注意2 表模型.objects.filter(Q, 其他字段的键值对) Q放在前面

    print(ret)


















    return HttpResponse("OK")








