# Generated by Django 4.2.4 on 2023-08-16 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls_new', '0004_car_carbooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls_new.touristplace')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls_new.cart')),
            ],
        ),
        migrations.DeleteModel(
            name='CarBooking',
        ),
        migrations.AddField(
            model_name='cart',
            name='cars',
            field=models.ManyToManyField(through='polls_new.CartItem', to='polls_new.touristplace'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
