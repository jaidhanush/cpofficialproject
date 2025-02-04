from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car, Booking
from .serializers import BookingSerializer

@api_view(['POST'])  # ✅ Only allows POST requests
def book_car(request):
    serializer = BookingSerializer(data=request.data)

    if serializer.is_valid():
        car = Car.objects.get(id=request.data['car_id'])

        if car.availability:
            booking = serializer.save()
            car.availability = False
            car.save()
            return Response({'message': 'Booking successful', 'booking': BookingSerializer(booking).data})

        return Response({'message': 'Car not available'}, status=400)

    return Response(serializer.errors, status=400)


@api_view(['POST'])
def cancel_booking(request):
    try:
        booking = Booking.objects.get(id=request.data['booking_id'])
        booking.status = 'Cancelled'
        booking.car.availability = True
        booking.car.save()
        booking.save()
        return Response({'message': 'Booking cancelled successfully'})
    except Booking.DoesNotExist:
        return Response({'message': 'Invalid Booking ID'}, status=400)

@api_view(['POST'])
def check_availability(request):
    available_cars = Car.objects.filter(availability=True)
    serializer = CarSerializer(available_cars, many=True)
    
    return Response({'available': bool(available_cars), 'cars': serializer.data})



from .serializers import ReservationSerializer

@api_view(['POST'])
def reserve_car(request):
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Reservation successful', 'reservation': serializer.data})
    return Response(serializer.errors, status=400)
