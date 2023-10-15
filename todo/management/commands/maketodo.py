from django.core.management import BaseCommand
from todo.models import Todo
import sys

class Command(BaseCommand):
    def handle(self, *args, **option):
        print("make todo start :")
        
        for i in range(1, 101):
            # todo = Todo.objects.create(name=f"test todo {i}")
            todo, created = Todo.objects.get_or_create(name=f"test todo {i}")
            if created:
                print(f"{i}번째 todo 생성 완료")
            else:
                sys.stdout.write(self.style.ERROR("{i}번째 todo already exists\n"))
        print("make todo end :)")
        sys.stdout.write(self.style.SUCCESS("make todo end :)"))
        