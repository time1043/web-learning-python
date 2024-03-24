import os
import random
import string

import django
from django.utils import timezone
from faker import Faker
from tqdm import tqdm

# 确保在导入任何Django模块之前设置环境变量和初始化Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user_manage_django.settings")
django.setup()

from app01.models import Department, UserInfo, PrettyNum


def create_data_to_department():
    """ 生成 Department 表的数据 """
    # 读取文件
    department_names = []
    with open('departments_name.txt', 'r', encoding='utf-8') as file:
        for line in file:
            department_names.append(line.strip())
    print(department_names)
    # 添加到数据库中
    for dept in department_names:
        Department.objects.create(title=dept)


def generate_random_password(length=8):
    if length < 3:
        raise ValueError("ensure the password contains an uppercase, a lowercase, and a number.")
    # 先确保至少有一个大写字母、一个小写字母和一个数字
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits)
    ]
    # 填充剩下的长度
    for i in range(length - 3):
        characters = string.ascii_letters + string.digits
        password.append(random.choice(characters))
    # 打乱字符的顺序以确保随机性
    random.shuffle(password)
    return ''.join(password)


def create_data_to_userinfo(count):
    """ 生成 UserInfo 表的数据 """
    for _ in tqdm(range(count), desc="Generating data of UserInfo"):
        naive_datetime = fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)  # 无时区信息
        aware_datetime = timezone.make_aware(naive_datetime, timezone.get_default_timezone())  # 转换为有时区信息的对象

        user = UserInfo(
            name=fake.name(),
            password=generate_random_password(),
            age=fake.random_int(min=20, max=60),
            account=fake.pydecimal(left_digits=8, right_digits=2, positive=True),
            create_time=aware_datetime,
            depart=random.choice(Department.objects.all()),
            gender=fake.random_element(elements=[0, 1])
        )
        user.save()


def generate_pretty_num_data():
    mobile = fake.phone_number()  # 随机电话号码
    price = round(random.uniform(0, 10000), 2)  # 随机价格区间
    level = random.choice([1, 2, 3])  # 随机选择一个级别
    status = random.choice([0, 1])  # 随机选择一个状态
    return {
        "mobile": mobile,
        "price": price,
        "level": level,
        "status": status
    }


def create_data_to_prettynum(count):
    """ 生成 PrettyNum 表的数据 """
    for _ in tqdm(range(count), desc="Generating data of PrettyNum"):
        data = generate_pretty_num_data()
        pretty_num = PrettyNum(**data)
        pretty_num.save()


if __name__ == '__main__':
    fake = Faker('zh_CN')
    create_data_to_department()
    create_data_to_userinfo(1000)
    create_data_to_prettynum(1000)
