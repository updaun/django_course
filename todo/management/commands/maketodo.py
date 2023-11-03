from django.core.management import BaseCommand
from todo.models import Todo
from random import choice
import sys


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("make todo start :")
        
        for i in range(1, 101):
           # todo = Todo.objects.create(name=f"테스트 todo {i}")
            todo,created = Todo.objects.get_or_create(name=f"테스트 todo {i}")
            if created : 
                print(f"{i}번째 todo 생성 완료")
            else:
                print(f"{i}번째 todo 이미 존재")
            
        print("make todo end :" )
        sys.stdout.write(self.style.SUCCESS("make todo end: "))