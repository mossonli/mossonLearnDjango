from django.db import models

# Create your models here.

class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name=models.CharField( max_length=32)
    age=models.IntegerField()

    # 与AuthorDetail建立一对一的关系 OneToOneField 创建 unique
    authorDetail=models.OneToOneField(to="AuthorDetail",on_delete=models.CASCADE)

class AuthorDetail(models.Model):

    nid = models.AutoField(primary_key=True)
    birthday=models.DateField()
    telephone=models.BigIntegerField()
    addr=models.CharField( max_length=64)

class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name=models.CharField( max_length=32)
    city=models.CharField( max_length=32)
    email=models.EmailField()

class Book(models.Model):

    nid = models.AutoField(primary_key=True)
    title = models.CharField( max_length=32)
    publishDate=models.DateField()
    price=models.DecimalField(max_digits=5,decimal_places=2)

    # 与Publish建立一对多的关系,外键字段建立在多的一方
    publish=models.ForeignKey(to="Publish",to_field="nid",on_delete=models.CASCADE)
    # 与Author表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表
    authors=models.ManyToManyField(to='Author',) # 这个authors字段不会生成会生成第三张关系表

    # 新增 阅读量 评论量 对于新增的字段要设置默认值
    read_num = models.ImageField(default=0)
    comment_num = models.ImageField(default=0)

    def __str__(self):
        return self.title

class Emp(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    salary=models.DecimalField(max_digits=8,decimal_places=2)
    dep=models.CharField(max_length=32)
    province=models.CharField(max_length=32)

# 用户注册
class UserInfo(models.Model):
    name=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)
    email=models.EmailField()
    tel=models.CharField(max_length=32)
    sex_list = (
        (1, '男'),
        (2, '女'),
    )
    sex = models.IntegerField(choices=sex_list, default=1)

