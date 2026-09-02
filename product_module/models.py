from django.db import models

# Create your models here.



class ProductCategory(models.Model):
    parent = models.ForeignKey('ProductCategory',on_delete=models.CASCADE,null=True,blank=True,verbose_name='دسته بندی',related_name='children')
    title = models.CharField(max_length=300,verbose_name='عنوان دسته بندی',db_index=True)
    url_title = models.CharField(max_length=300,db_index=True,verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True,verbose_name='فعال/غیر فعال')
    is_delete = models.BooleanField(default=False,verbose_name='حذف شده / نشده')

    def __str__(self):
        return self.title
    
    class Meta:
        
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductBrand(models.Model):
    title = models.CharField(max_length=300,verbose_name='عنوان برند',db_index=True)
    is_active = models.BooleanField(default=True,verbose_name='فعال/غیر فعال')
    def __str__(self):
            return self.title
        
    class Meta:
            
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'


class Product(models.Model):
    title = models.CharField(max_length=300,verbose_name='عنوان محصول',db_index=True)
    category = models.ManyToManyField(ProductCategory,verbose_name='دسته بندی محصول',related_name='product_categories')
    slug = models.SlugField(null=True,blank=True,db_index=True,default='',unique=True,allow_unicode=True)
    price = models.PositiveIntegerField(verbose_name='قیمت')
    short_description = models.CharField(max_length=400,null=True,blank=True,verbose_name='توضیحات کوتاه ')
    description = models.TextField(verbose_name='توضیحات',null=True,blank=True)
    image = models.ImageField(upload_to='images/product_image',verbose_name='تصویر محصول',null=True,blank=True)
    product_brand = models.ForeignKey(ProductBrand,on_delete=models.CASCADE,verbose_name='برند محصول',related_name='product_brand',null=True,blank=True)
    is_active = models.BooleanField(default=True,verbose_name='فعال/غیر فعال')
    is_delete = models.BooleanField(default=False,verbose_name='حذف شده / نشده')
    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'    


    
