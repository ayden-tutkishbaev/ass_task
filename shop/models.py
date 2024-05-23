from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import Media


class Category(models.Model):
    title = models.CharField(_('Title'), max_length=150)
    image = models.ForeignKey(Media, related_name='category_image', blank=True, null=True,
                              on_delete=models.CASCADE, verbose_name=_("Category image"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Brand(models.Model):
    title = models.CharField(_('Title'), max_length=150)
    image = models.ForeignKey(Media, related_name='brand_image', blank=True, null=True, on_delete=models.CASCADE,
                              verbose_name=_('Brand image'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')


class Product(models.Model):
    class Gender(models.TextChoices):
        MEN = 'men', _('Men')
        WOMEN = 'women', _('Women')

    image1 = models.ForeignKey(Media, related_name='product_image', on_delete=models.CASCADE,
                               verbose_name=_('Image 1'))
    image2 = models.ForeignKey(Media, related_name='product_image2', blank=True, null=True, on_delete=models.CASCADE,
                               verbose_name=_('Image 2'))
    image3 = models.ForeignKey(Media, related_name='product_image3', blank=True, null=True, on_delete=models.CASCADE,
                               verbose_name=_('Image 3'))
    image4 = models.ForeignKey(Media, related_name='product_image4', blank=True, null=True, on_delete=models.CASCADE,
                               verbose_name=_('Image 4'))
    image5 = models.ForeignKey(Media, related_name='product_image5', blank=True, null=True, on_delete=models.CASCADE,
                               verbose_name=_('Image 5'))

    title = models.CharField(verbose_name=_('Title'), max_length=150)

    price = models.FloatField(verbose_name=_('Price'))
    discounted_price = models.FloatField(verbose_name=_("Discounted price"), default=0)

    size_num = models.ManyToManyField("ProductSizeNumerical", verbose_name=_('Size in numbers'))
    size_letter = models.ManyToManyField("ProductSizeLetter", verbose_name=_('Size in letters'))
    colors = models.ManyToManyField("common.Media", verbose_name=_('Colors'))

    description = models.TextField(verbose_name=_('Description'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"),
                                 related_name='category_product')

    gender = models.CharField(max_length=120, verbose_name=_("Men/Women"), choices=Gender.choices)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name=_("Brand"),
                              related_name='brand_product_women')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class ProductSizeNumerical(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product numerical size')
        verbose_name_plural = _('Product numerical sizes')


class ProductSizeLetter(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product size in letters')
        verbose_name_plural = _('Product sizes in letters')


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        NEW = 'new', _('new')
        ACCEPTED = 'accepted', _('accepted')
        PROGRESS = 'progress', _('progress')
        CANCELLED = 'cancelled', _('cancelled')
        FINISHED = 'finished', _('finished')

    class Payment(models.TextChoices):
        CREDIT_CARD = 'credit_card', _('Credit card')
        CASH = 'cash', _('Cash')

    name = models.CharField(verbose_name=_('Name'), max_length=120)
    surname = models.CharField(verbose_name=_('Surname'), max_length=120)
    street = models.CharField(verbose_name=_('Street'), max_length=120)
    house = models.CharField(verbose_name=_('House'), max_length=12)
    apartment = models.CharField(verbose_name=_('Apartment'), max_length=12, blank=True)

    delivery_date = models.DateField(verbose_name=_('Delivery date'))
    delivery_time = models.TimeField(verbose_name=_("Delivery Time"))

    status = models.CharField(verbose_name=_('status'), max_length=20, choices=OrderStatus.choices,
                              default=OrderStatus.NEW)

    payment = models.CharField(verbose_name=_("Payment method"), max_length=120, choices=Payment.choices)

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_('order'), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_('product'), on_delete=models.CASCADE)
    quantity = models.IntegerField(_('quantity'), default=1)

    class Meta:
        verbose_name = _('order item')
        verbose_name_plural = _('order item')
        unique_together = ('order', 'product')

    def __str__(self):
        return f"Id: {self.id} | Q: {self.quantity}"

    @property
    def total_price(self):
        return self.product.price * self.quantity


class Return(models.Model):
    reason = models.TextField(verbose_name=_("The reason of return"))

    def __str__(self):
        return self.reason

    class Meta:
        verbose_name = _("Return")
