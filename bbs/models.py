from django.db import models

class Topic(models.Model):
    class Meta:
        db_table = "topic"

    comment = models.CharField(verbose_name="comment", max_length=200)

    def __str__(self):
        return self.comment
        
    