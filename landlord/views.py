from django.shortcuts import render

mock_ads = [{
    'id': '1',
    'image_url': 'https://images.adsttc.com/media/images/5e1d/02c3/3312/fd58/9c00/06e9/slideshow/NewHouse_SA_Photo_01.jpg?1578959519',
    'name': 'Name 1',
    'description': 'Description 1...',
    'location': 'Locatin 1...',
    'payment_mode': 'Cash',
    'price': 10,
    'area': 'Area 1'
}, {
    'id': '2',
    'image_url': 'https://images.adsttc.com/media/images/5e1d/02c3/3312/fd58/9c00/06e9/slideshow/NewHouse_SA_Photo_01.jpg?1578959519',
    'name': 'Name 2',
    'description': 'Description 2...',
    'location': 'Locatin 2...',
    'payment_mode': 'Cash',
    'price': 10,
    'area': 'Area 2'
}, {
    'id': '3',
    'image_url': 'https://images.adsttc.com/media/images/5e1d/02c3/3312/fd58/9c00/06e9/slideshow/NewHouse_SA_Photo_01.jpg?1578959519',
    'name': 'Name 3',
    'description': 'Description 3...',
    'location': 'Locatin 3...',
    'payment_mode': 'Cash',
    'price': 10,
    'area': 'Area 3'
}, {
    'id': '4',
    'image_url': 'https://images.adsttc.com/media/images/5e1d/02c3/3312/fd58/9c00/06e9/slideshow/NewHouse_SA_Photo_01.jpg?1578959519',
    'name': 'Name 4',
    'description': 'Description 4...',
    'location': 'Locatin 4...',
    'payment_mode': 'Cash',
    'price': 10,
    'area': 'Area 4'
}]

mock_profile = {
    'name': 'moderator',
    'email': 'admin@roomgenie.com'
}

def ads(request, id = None): 
    # Connect to db and parse in a similar schema
    ads = mock_ads
    
    print(id)

    if id:
        ad = list(filter(lambda x: x['id'] == str(id), ads))

        if len(ad) > 0:
            return render(request, 'webproject/admin/ad.html', {
                'ad': ad[0]
            }) 

    return render(request, 'webproject/admin/ads.html', {
        'ads': ads
    }) 

def index(request):
    context = {}
    return render(request, 'webproject/admin/index.html', context)

def profile(request):
    profile = mock_profile
    return render(request, 'webproject/admin/profile.html', {
        'user': mock_profile
    })