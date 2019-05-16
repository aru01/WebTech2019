from django.db import models


# Create your models here.

class TaskList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json_list(self):
        return {
            'id' : self.id,
            'name' : self.name
        }


class Task(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    due_on = models.DateTimeField()
    status = models.CharField(max_length=40)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return '{} : {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status
        }

    def to_json_detail(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status
        }