# Generated by Django 4.2.10 on 2024-02-16 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_remove_ticket_notes_ticket_ticket_notes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_notes',
        ),
        migrations.AlterField(
            model_name='note',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='ticket.ticket'),
        ),
    ]