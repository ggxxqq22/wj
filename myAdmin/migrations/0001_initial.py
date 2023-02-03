# Generated by Django 2.1 on 2022-09-01 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionId', models.IntegerField(verbose_name='关联问题id')),
                ('submitId', models.IntegerField(verbose_name='关联提交id')),
                ('wjId', models.IntegerField(verbose_name='问卷id')),
                ('type', models.CharField(max_length=20, verbose_name='题目类型')),
                ('answer', models.IntegerField(blank=True, null=True, verbose_name='答案')),
                ('answerText', models.TextField(blank=True, null=True, verbose_name='文本答案')),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionId', models.IntegerField(verbose_name='关联题目id')),
                ('title', models.CharField(max_length=100, verbose_name='选项名')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='题目标题')),
                ('type', models.CharField(max_length=20, verbose_name='题目类型')),
                ('wjId', models.IntegerField(verbose_name='关联问卷id')),
                ('row', models.IntegerField(null=True, verbose_name='行数')),
                ('must', models.BooleanField(verbose_name='是否必填')),
            ],
        ),
        migrations.CreateModel(
            name='Submit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wjId', models.IntegerField(verbose_name='关联问卷id')),
                ('submitTime', models.DateTimeField(verbose_name='提交时间')),
                ('submitIp', models.CharField(max_length=15, verbose_name='提交ip')),
                ('useTime', models.IntegerField(verbose_name='填写用时')),
            ],
        ),
        migrations.CreateModel(
            name='TempOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionId', models.IntegerField(verbose_name='关联题目id')),
                ('title', models.CharField(max_length=100, verbose_name='选项名')),
            ],
        ),
        migrations.CreateModel(
            name='TempQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='题目标题')),
                ('type', models.CharField(max_length=20, verbose_name='题目类型')),
                ('wjId', models.IntegerField(verbose_name='关联问卷id')),
                ('row', models.IntegerField(null=True, verbose_name='行数')),
                ('must', models.BooleanField(verbose_name='是否必填')),
            ],
        ),
        migrations.CreateModel(
            name='TempWj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='问卷标题')),
                ('username', models.CharField(max_length=20, verbose_name='创建人')),
                ('desc', models.TextField(null=True, verbose_name='问卷说明')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('email', models.CharField(max_length=30, null=True, verbose_name='邮箱')),
                ('status', models.IntegerField(choices=[(0, '正常'), (1, '禁用')], default=0, verbose_name='状态')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户列表',
            },
        ),
        migrations.CreateModel(
            name='Wj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='问卷标题')),
                ('username', models.CharField(max_length=20, verbose_name='发起人')),
                ('status', models.IntegerField(choices=[(0, '未发布'), (1, '已发布')], default=0, verbose_name='是否发布')),
                ('desc', models.TextField(null=True, verbose_name='问卷说明')),
            ],
            options={
                'verbose_name': '问卷',
                'verbose_name_plural': '问卷列表',
            },
        ),
    ]
