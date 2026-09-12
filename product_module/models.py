from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
# Create your models here.

class ProductManager(models.Manager):
    def get_queryset(self):
         return super().get_queryset().filter(is_active=True,is_delete=False)
    
class BaseModel(models.Model):
     is_active = models.BooleanField(default=True,verbose_name='فعال/غیر فعال')
     is_delete = models.BooleanField(default=False,verbose_name='حذف شده / نشده')
     objects = ProductManager()
     all_objects = models.Manager()
     
     class Meta:
          abstract = True
          
     

class ProductCategory(BaseModel):
    parent = models.ForeignKey('ProductCategory',on_delete=models.SET_NULL,null=True,blank=True,verbose_name='دسته بندی',related_name='children')
    title = models.CharField(max_length=300,verbose_name='عنوان دسته بندی',db_index=True)
    url_title = models.CharField(max_length=300,db_index=True,verbose_name='عنوان در url')
    

    def __str__(self):
        return self.title
    
    class Meta:
        
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductBrand(BaseModel):
    title = models.CharField(max_length=300,verbose_name='عنوان برند',db_index=True)
   
    def __str__(self):
            return self.title


    class Meta:
            
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'


class Product(BaseModel):
   
    title = models.CharField(max_length=300,verbose_name='عنوان محصول',db_index=True)
    category = models.ManyToManyField(ProductCategory,verbose_name='دسته بندی محصول',related_name='products')
    slug = models.SlugField(null=True,blank=True,unique=True,allow_unicode=True)
    price = models.PositiveIntegerField(verbose_name='قیمت')
    short_description = models.CharField(max_length=400,null=True,blank=True,verbose_name='توضیحات کوتاه ')
    description = models.TextField(verbose_name='توضیحات',null=True,blank=True)
    image = models.ImageField(upload_to='images/product_image',verbose_name='تصویر محصول',null=True,blank=True,validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])])
    product_brand = models.ForeignKey(ProductBrand,on_delete=models.SET_NULL,verbose_name='برند محصول',related_name='products',null=True,blank=True)
   
    def __str__(self):
        return f"{self.title} ({self.price})"
    
    def save(self,*args,**kwargs):

        if not self.slug:
            self.slug = slugify(self.title,allow_unicode=True)
            base = self.slug
            counter = 1
            while Product.all_objects.filter(slug=self.slug).exists():
                    self.slug = f"{base}-{counter}"
                    counter+=1



        
        super(Product,self).save(*args, **kwargs)
        
        

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'    


    
