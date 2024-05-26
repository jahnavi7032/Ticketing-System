# Generated by Django 4.2.10 on 2024-02-16 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_rename_ticked_id_ticket_ticket_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='notes',
        ),
        migrations.AddField(
            model_name='ticket',
            name='ticket_notes',
            field=models.ManyToManyField(blank=True, related_name='tickets_related', to='ticket.note'),
        ),
        migrations.AlterField(
            model_name='note',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes_related', to='ticket.ticket'),
        ),
    ]