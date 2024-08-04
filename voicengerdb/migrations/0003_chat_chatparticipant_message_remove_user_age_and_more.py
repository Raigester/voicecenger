# Generated by Django 4.2.14 on 2024-08-04 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voicengerdb', '0002_user_delete_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_type', models.CharField(choices=[('Private', 'Private'), ('Group', 'Group'), ('Anonim Group', 'Anonim Group'), ('Channel', 'Channel')], max_length=20)),
                ('chat_image', models.ImageField(blank=True, null=True, upload_to='chat_images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('closed_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChatParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('notifications_enabled', models.BooleanField(default=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voicengerdb.chat')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.CharField(choices=[('Text', 'Text'), ('Audio', 'Audio'), ('Video', 'Video')], max_length=10)),
                ('content', models.TextField(blank=True, null=True)),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='audio_files/')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='video_files/')),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('is_edited', models.BooleanField(default=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voicengerdb.chat')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='facebook_profile',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_online',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_login_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='notifications_enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_pictures',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='default_username', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='MessageReadReceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_at', models.DateTimeField(auto_now_add=True)),
                ('chat_participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voicengerdb.chatparticipant')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voicengerdb.message')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voicengerdb.user'),
        ),
        migrations.AddField(
            model_name='chatparticipant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voicengerdb.user'),
        ),
        migrations.AddField(
            model_name='chat',
            name='last_message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_message_in_chat', to='voicengerdb.message'),
        ),
    ]
