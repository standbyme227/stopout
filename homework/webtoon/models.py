from django.db import models


class Webtoon(models.Model):
    webtoon_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    week_webtoon = models.CharField(max_length=100)
    img_url = models.CharField(max_length=100)


    def __str__(self):
        return'({weekday}) {title}'.format(
            weekday = self.week_webtoon,
            title = self.title,
        )


class Episode(models.Model):
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE)
    episode_id = models.CharField(max_length=100)
    episode_title = models.CharField(max_length=100)
    episode_img_url = models.CharField(max_length=100)
    episode_date = models.CharField(max_length=100)

    def __str__(self):
        return '{title}, '
