from django.forms import ValidationError
from django.http import JsonResponse 
from event_service import EventRatingService 

def rate_event_view(request):
    if request.method == 'POST':
        data = request.POST 
        event_id = data.get('event_id')
        user_id = data.get('user_id')
        rating = int(data.get('rating'))

        try: 
            service = EventRatingService()
            event_rating = service.create_event_rating(
                event_id = event_id,
                user_id = user_id,
                rating = rating,
            )
            return JsonResponse({'status': 'success', 'rating_id': event_rating.id})
        except ValidationError as e: 
            return JsonResponse({'status':'error', 'message': str(e)}, status=400)
        
