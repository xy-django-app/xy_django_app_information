<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:52:22
 * @FilePath: /xy_django_app_information/readme/README.en.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_app_information

| [简体中文](../README.md)         | [繁體中文](./README.zh-hant.md)        |                      [English](./README.en.md)          |
| ----------- | -------------|---------------------------------------|

## Description

Common information data model.

## Source Code Repositories

| [Github](https://github.com/xy-django-app/xy_django_app_information.git)         | [Gitee](https://gitee.com/xy-opensource/xy_django_app_information.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_django_app_information.git)          |
| ----------- | -------------|---------------------------------------|

## Installation

```bash
# bash
pip install xy_django_app_information
```

## How to use


##### 1. Direct import

- ###### 1. Setting global configuration

Add the following configuration to the settings.py file in the Django project.  
For example:[settings.py](../samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)

```python
# settings.py

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "xy_django_app_information",
    "Demo",
    "Resource",
    "Media",
]

```

- ###### 2. Run the project

```bash
xy_web_server -w django makemigrations
xy_web_server -w django migrate
# 同步数据表
xy_web_server -w django start

# 启动工程后访问 http://127.0.0.1:8401/admin 验证信息管理系统
```

##### 2. Custom

- ###### 1. Create the Information module

> Operation [Sample Project](../samples/xy_web_server_demo/)

```bash
# bash
xy_web_server -w django startapp Information
# Information 模块创建在 source/Runner/Admin/Information 
```

- ###### 2. Setting global configuration

Add the following configuration to the settings.py file in the Django project.  
For example: [settings.py](../samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)

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

- ###### 3. Add the following code to the [models.py](../samples/xy_web_server_demo/source/Runner/Admin/Information/models.py) of the  [Information](../samples/xy_web_server_demo/source/Runner/Admin/Information) module

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

- ###### 4. Add the following code to the [admin.py](../samples/xy_web_server_demo/source/Runner/Admin/Information/admin.py) of the [Information](../samples/xy_web_server_demo/source/Runner/Admin/Information) module

```python
# admin.py
from django.contrib import admin
from .models import MRegion

# Register your models here.


@admin.register(MRegion)
class ARegion(admin.ModelAdmin):
    pass

```

- ###### 5. Run the project

```bash
xy_web_server -w django makemigrations
xy_web_server -w django migrate
# 同步数据表
xy_web_server -w django start

# 启动工程后访问 http://127.0.0.1:8401/admin 验证账户管理系统
```


##### Run [Sample Project](../samples/xy_web_server_demo)

> For detailed usage of the sample project, please go to the following repository <b style="color: blue">xy_web_server.git</b> 

| [Github](https://github.com/xy-web-service/xy_web_server.git)         | [Gitee](https://gitee.com/xy-opensource/xy_web_server.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_web_server.git)          |
| ----------- | -------------|---------------------------------------|

## License
xy_django_app_information is licensed under the <Mulan Permissive Software License，Version 2>. See the [LICENSE](../LICENSE) file for more info.

## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  

![Pay-Total](./Pay-Total.png)  


## Contact

```
WeChat: yuyangiit
Mail: yuyangit.0515@qq.com
```