from django.shortcuts import render

mock_ads = [{
    'id': '1',
    'image_url': 'https://images.adsttc.com/media/images/5e1d/02c3/3312/fd58/9c00/06e9/slideshow/NewHouse_SA_Photo_01.jpg?1578959519',
    'name': 'description 1',
    'price': 10,
    'area': 'Area 1'
}, {
    'id': '2',
    'image_url': 'https://images.adsttc.com/media/images/5e1d/02c3/3312/fd58/9c00/06e9/slideshow/NewHouse_SA_Photo_01.jpg?1578959519',
    'name': 'description 2',
    'price': 10,
    'area': 'Area 2'
}, {
    'id': '3',
    'image_url': 'https://images.adsttc.com/media/images/5e1d/02c3/3312/fd58/9c00/06e9/slideshow/NewHouse_SA_Photo_01.jpg?1578959519',
    'name': 'description 3',
    'price': 10,
    'area': 'Area 3'
}, {
    'id': '4',
    'image_url': 'https://images.adsttc.com/media/images/5e1d/02c3/3312/fd58/9c00/06e9/slideshow/NewHouse_SA_Photo_01.jpg?1578959519',
    'name': 'description 4',
    'price': 10,
    'area': 'Area 4'
}]

def ads(request): 
    # Connect to db and parse in a similar schema
    ads = mock_ads
    return render(request, 'webproject/admin/ads.html', {
        'ads': ads
    }) 

def index(request):
    latest_question_list = []
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'webproject/admin/index.html', context)