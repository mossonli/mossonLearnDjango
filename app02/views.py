from django.shortcuts import render, HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage
from app01.models import Book
from .mforms import UserForm
# Create your views here.
def login(request):
    return HttpResponse("APP02")

def app_namespace_url(request):
    pat = reverse('app02:app_namespace_url')
    print(pat)
    return HttpResponse("app02 app_namespace_url")

def ajax_demo(request):

    return render(request, "ajax_demo.html")

def file_put(request):
    if request.method == 'POST':
        # 文件操作接收文件
        file_obj = request.FILES.get('filename')
    elif request.method == 'GET':
        return render(request, 'file_put.html')

def user_reg(request):
    form = UserForm()
    return render(request, 'user_reg.html', locals())


def page_demo(request):
    # django 批量插入数据
    """
    book_list = []
    for i in range(100):
        book = Book(title='page_book_%s' % i, price=100, publishDate='2019-01-30', publish_id=1)
        book_list.append(book)
    Book.objects.bulk_create(book_list)
    """
    current_page = int(request.GET.get('page', 1))
    book_ = Book.objects.all()
    # 分页器
    paginator = Paginator(book_, 3)
    print('ccount', paginator.count)    # 数据总数
    print('num_pages', paginator.num_pages)    # 总页数
    print('page_range', paginator.page_range)    # 页码的列表

    if paginator.num_pages > 11:
        if current_page-5 < 1:
            page_range=range(1, 12)
        elif current_page+5 > paginator.num_pages:
            page_range=range(paginator.num_pages-11, paginator.num_pages+1)
        else:
            page_range = range(current_page - 5, current_page + 6)
    else:
        page_range = paginator.page_range


    try:
        book_list = paginator.page(current_page)
        # 显示某一页具体数据的两种方式
        for i in book_list:
            print(i)
    except EmptyPage as e:
        current_page = paginator.page(1)

    return render(request, 'page_demo.html', locals())