from django.core.management.base import BaseCommand, CommandError
from api.models import Message

from random import choice

class Command(BaseCommand):
    help = 'This command populates chat'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.fill_chat()
        print('Done')

    def fill_chat(self):
        replicas = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
        Donec felis mauris, faucibus id bibendum eu, bibendum ac sapien.\
        Aliquam laoreet dictum cursus. Morbi consequat dictum sem, in accumsan eros placerat at.\
        Nulla facilisi. Donec porttitor nibh augue, eu lacinia nisl dignissim sit amet.\
        Donec mi nulla, luctus nec mi sit amet, scelerisque fringilla nisl.\
        In volutpat ultrices lectus, sed interdum nunc pharetra vel.\
        Vivamus placerat quis lacus eu sagittis.\
        Nulla aliquet sagittis lectus, eu mattis nulla lacinia et.In imperdiet elit a nisi porta pharetra.\
        Cras sagittis feugiat consequat. Donec a porta ipsum. Aliquam erat volutpat.\
        Pellentesque sem metus, aliquet quis felis id, placerat viverra dui. Suspendisse ultricies a felis at vulputate.\
        Mauris et metus eu elit scelerisque pharetra ac a dolor. Donec lacinia rhoncus est, sed egestas tortor gravida eget.\
        Nulla vehicula porttitor nunc, vitae sodales ligula accumsan in.\
        Nulla diam augue, commodo eget varius et, porttitor sed ex. Nullam sed neque erat.\
        Aenean a sem tincidunt risus interdum ultrices et et nulla. Praesent mi nisi, ornare eget suscipit ut, semper vitae massa.\
        Nulla dui nibh, malesuada ut pharetra sit amet, auctor sed massa. Integer ipsum metus, volutpat non maximus at, tristique in lorem.\
        Etiam ac nisl dui.".split('.')

        for i in range(50):
            m = Message(author=f'user{i}@mail.com',
                        text=choice(replicas))
            m.save()