# import Artist model
```
from artists.models import Artist
```
# create some artists
```
artist = Artist(stage_name = "Mahmoud Mohamed" , social_link_field = 'https://www.instagram.com/mahmoud/')
artist.save()
artist = Artist(stage_name = "Ahmed Mohamed" , social_link_field = 'https://www.instagram.com/ahmed/')
artist.save()
```
# list down all artists
```
Artist.objects.all()
<QuerySet [<Artist: stage_name = Mahmoud Mohamed || social_link_field = https://www.instagram.com/mahmoud/>, <Artist: stage_name = Ahmed Mohamed || social_link_field = https://www.instagram.com/ahmed/>]>
```
# list down all artists sorted by name
```
Artist.objects.all().order_by('stage_name')
<QuerySet [<Artist: stage_name = Ahmed Mohamed || social_link_field = https://www.instagram.com/ahmed/>, <Artist: stage_name = Mahmoud Mohamed || social_link_field = https://www.instagram.com/mahmoud/>]>
```
# list down all artists whose name starts with `A`
```
Artist.objects.filter(stage_name__startswith='A') 
<QuerySet [<Artist: stage_name = Ahmed Mohamed || social_link_field = https://www.instagram.com/ahmed/>]>
```
# import Album model and timezone
```
from albums.models import Album  
from django.utils import timezone
```
# in 2 different ways, create some albums and assign them to any artists (hint: use `objects` manager and use the related object reference)
```
album = Album(artist = Artist.objects.get(pk=1) , name = "album1", creation_datetime = timezone.now() , release_datetime = timezone.now() , cost = '70.75')
album.save()
album = Album(artist = Artist.objects.get(pk=2) , name = "album2", creation_datetime = timezone.now() , release_datetime = timezone.now() , cost = '75.70')
album.save()
```
# get the latest released album
```
Album.objects.latest('release_datetime')
<Album: name = album2 || creation_datetime = 2022-10-08 06:07:10.733132+00:00 || release_datetime = 2022-10-08 06:07:10.733132+00:00 || cost = 75.70>
```
# get all albums released before today
```
Album.objects.filter(release_datetime__lt = timezone.now())
<QuerySet [<Album: Album object (1)>, <Album: Album object (2)>]>
```
# get all albums released today or before but not after today
```
Album.objects.filter(release_datetime__lte = timezone.now())
<QuerySet [<Album: Album object (1)>, <Album: Album object (2)>]>
```
# count the total number of albums (hint: count in an optimized manner)
```
Album.objects.count()
2
```
# in 2 different ways, for each artist, list down all of his/her albums (hint: use `objects` manager and use the related object reference)
```
for track in Artist.objects.all():
    print(Album.objects.filter(artist=track.id))

<QuerySet [<Album: Album object (1)>]>
<QuerySet [<Album: Album object (2)>]>

for track in Album.objects.select_related('artist'):
        print(track.name, "belong to Artist : ",track.artist.stage_name)

album1 belong to Artist :  Mahmoud Mohamed
album2 belong to Artist :  Ahmed Mohamed
```
# list down all albums ordered by cost then by name (cost has the higher priority)
```
Album.objects.order_by('-cost' , 'name')
<QuerySet [<Album: Album object (2)>, <Album: Album object (1)>]>
```
# Modify the artist queryset so that I can order the list of artists by the number of their approved albums
```
query_set = Artist.objects.all()
sorted(query_set, key=lambda object:object.approved_albums())
[<Artist: stage_name = Mahmoud Mohamed || social_link_field = https://www.instagram.com/mahmoud/>, <Artist: stage_name = 
Ahmed Mohamed || social_link_field = https://www.instagram.com/ahmed/>]
```
