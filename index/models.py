from django.db import models

choice=(
    ('rare','RARE'),
    ('low','LOW'),
    ('medium','Medium'),
    ('high','HIGH'),
    ("extreme",'EXTREME')
)


class item(models.Model):
    title=models.CharField(max_length=50)
    img=models.ImageField()
    probability=models.CharField(max_length=50,choices=choice,default='normal')

    def __str__(self):
        return self.title
    

class case(models.Model):
    title=models.CharField(max_length=50)
    price=models.FloatField(default=0.00)
    pic=models.ImageField()
    box_item=models.ManyToManyField(item,null=False)

    def __str__(self):
        return self.title
    
