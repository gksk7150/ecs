from django.db import models
from django.contrib.auth.models import User


# 기존 문의 게시판
class Inquiry(models.Model):
    TYPE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    STATUS_CHOICES = [
        ('Q', '문의'),
        ('A', '답변'),
        ('C', '종결'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='Q'
    )

    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    due_date = models.DateField(null=True)
    action = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# 고객사 메뉴
class CustomerMenu(models.Model):
    company_name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        is_new = self.pk is None   # 새로 생성인지 확인

        super().save(*args, **kwargs)

        if is_new:
            default_menus = ['IFQ', 'SQ', 'SIS']

            for menu in default_menus:
                SubMenu.objects.create(
                    customer_menu=self,
                    menu_name=menu
                )

    def __str__(self):
        return self.company_name


# 하위 메뉴
class SubMenu(models.Model):
    customer_menu = models.ForeignKey(
        CustomerMenu,
        on_delete=models.CASCADE,
        related_name='sub_menus'
    )

    menu_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.customer_menu.company_name} - {self.menu_name}"