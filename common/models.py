from django.db import models

from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _


class Media(models.Model):
    class FileType(models.TextChoices):
        IMAGE = 'image', _("Image")
        VIDEO = 'video', _("Video")
        DOCUMENT = 'document', _("document")
        GIF = 'gif', _("Gif")
        OTHER = 'other', _("Other")

    file = models.FileField(upload_to='only_medias/',
                            verbose_name=_("File"),
                            validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'mp4', 'avi',
                                                                                   'mov', 'gif', 'webp', 'pdf', 'doc',
                                                                                   'docx', 'mpeg'])])
    file_type = models.CharField(max_length=10, verbose_name=_("File Type"),
                                 choices=FileType.choices)

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media")

    def __str__(self):
        element = r"""[\]"""
        return f'Id: {self.id}|Name: {self.file.name.split(element)[-1]}'

    def clean(self):
        if self.file_type not in self.FileType.values:
            raise ValidationError(_("Invalid File Type"))
        elif self.file_type == self.FileType.IMAGE:
            if self.file.name.split('.')[-1] not in ['jpg', 'jpeg', 'png', 'webp']:
                raise ValidationError(_("Invalid Image File"))
        elif self.file_type == self.FileType.VIDEO:
            if self.file.name.split('.')[-1] not in ['mp4', 'avi', 'mov', 'mpeg']:
                raise ValidationError(_("Invalid Video File"))


class BackgroundImage1(models.Model):
    text = models.CharField(max_length=150, verbose_name=_('Background Image'))
    back_image = models.ForeignKey(Media, related_name='background_image1', verbose_name=_('Background Image'),
                                   on_delete=models.CASCADE)
    bottom_text = models.CharField(max_length=250, verbose_name=_('Bottom text'))

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _('Background Image One')


class AboutUs1(models.Model):
    headline = models.CharField(max_length=150, verbose_name=_("Headline"))
    text = models.TextField(verbose_name=_("Text"))
    image = models.ForeignKey(Media, related_name='about_us_image1', verbose_name=_('Image'),
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = _("First 'About us' page")


class AboutUs2(models.Model):
    headline = models.CharField(max_length=150, verbose_name=_("Headline"))
    text = models.TextField(verbose_name=_("Text"))
    image = models.ForeignKey(Media, related_name='about_us_image2', verbose_name=_('Image'),
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = _("Second 'About us' page")


class Promo(models.Model):
    headline = models.CharField(max_length=150, verbose_name=_("Headline"))
    text = models.TextField(verbose_name=_("Text"))
    image = models.ForeignKey(Media, related_name='promo_image', verbose_name=_('Image'),
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = _("Promo")


class StandardSettings(models.Model):
    main_phone_number = models.CharField(max_length=150, verbose_name=_("Main phone number"))
    main_email = models.CharField(max_length=150, verbose_name=_("Main email"))
    instagram = models.CharField(max_length=150, verbose_name=_("Instagram"))
    vkontakte = models.CharField(max_length=150, verbose_name=_("VK"))

    def __str__(self):
        return self.main_email

    class Meta:
        verbose_name = _("Standard Settings")


