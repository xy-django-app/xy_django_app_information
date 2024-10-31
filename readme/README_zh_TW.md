<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:51:56
 * @FilePath: /xy_django_app_information/readme/README_zh_TW.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_app_information

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

## 說明

後台帳號資料模型.

## 程式碼庫

- <a href="https://github.com/xy-django-app/xy_django_app_information.git" target="_blank">Github位址</a>  
- <a href="https://gitee.com/xy-django-app/xy_django_app_information.git" target="_blank">Gitee位址</a>

## 安裝

```bash
# bash
pip install xy_django_app_information
```

## 使用


#### 1. 创建Information模块
> 操作 [样例工程](./samples/xy_web_server_demo/)

```bash
# bash
xy_web_server -w django startapp Information
# Information 模块创建在 source/Runner/Admin/Information 
```

#### 2. 在样例工程中的[settings.py](./samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)设置如下

```python
# settings.py

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Demo",
    "Resource",
    "Media",
    "Information",
]

```

#### 3. 在[Information](./samples/xy_web_server_demo/source/Runner/Admin/Information)模块的[models.py](./samples/xy_web_server_demo/source/Runner/Admin/Information/models.py)文件中加入如下代码

```python
# models.py
from xy_django_app_information.abstracts import MARegion
from django.utils.translation import gettext_lazy as _

class MRegion(MARegion):
    class Meta:
        app_label = "Information"
        verbose_name = _("地理信息")
        verbose_name_plural = _("地理信息")

```

#### 4. 在[Information](./samples/xy_web_server_demo/source/Runner/Admin/Information)模块的[admin.py](./samples/xy_web_server_demo/source/Runner/Admin/Information/admin.py)文件中加入如下代码

```python
# admin.py
from django.contrib import admin
from .models import MRegion

@admin.register(MRegion)
class ARegion(admin.ModelAdmin):
    pass

```

#### 5. 运行项目

```bash
xy_web_server -w django start
# 启动工程后访问 http://127.0.0.1:8401/admin 验证账户系统
```

##### 運轉 [範例工程](../samples/xy_web_server_demo)

> 範例工程具體使用方式請移步 <b style="color: blue">xy_web_server.git</b> 下列倉庫
> - <a href="https://github.com/xy-web-service/xy_web_server.git" target="_blank">Github位址</a>  
> - <a href="https://gitee.com/xy-web-service/xy_web_server.git" target="_blank">Gitee位址</a>

## 許可證
xy_django_app_information 根據 <木蘭寬鬆許可證, 第2版> 獲得許可。有關詳細信息，請參閱 [LICENSE](../LICENSE) 文件。

## 捐贈

如果小夥伴們覺得這些工具還不錯的話，能否請咱喝一杯咖啡呢?  

![Pay-Total](./Pay-Total.png)

## 聯繫方式

```
微信: yuyangiit
郵箱: yuyangit.0515@qq.com
```