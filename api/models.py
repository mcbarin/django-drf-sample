from django.db import models


class Tile(models.Model):
    launch_date = models.DateTimeField(blank=False, null=False)

    LIVE = 1
    PENDING = 2
    ARCHIVED = 3
    TILE_STATUS_CHOICES = (
        (LIVE, 'Live'),
        (PENDING, 'Pending'),
        (ARCHIVED, 'Archived'),
    )
    status = models.PositiveSmallIntegerField(choices=TILE_STATUS_CHOICES)

    def __str__(self):
        return f'Launch Date: {self.launch_date}'

    class Meta:
        ordering = ['-launch_date']


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    order = models.IntegerField(default=0)
    tile = models.ForeignKey(
        Tile, 
        on_delete=models.CASCADE,
        related_name='tasks',
        blank=False,
        null=False
    )

    SURVEY = 1
    DISCUSSION = 2
    DIARY = 3
    TASK_TYPE_CHOICES = (
        (SURVEY, 'Survey'),
        (DISCUSSION, 'Discussion'),
        (DIARY, 'Diary'),
    )

    task_type = models.PositiveSmallIntegerField(choices=TASK_TYPE_CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

