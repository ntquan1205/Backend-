from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Session

SESSIONS_DB = []
COUNTER = 1

class HealthCheckView(APIView):
    def get(self, request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)

class SessionListCreateView(APIView):
    def get(self, request):
        sessions = Session.objects.all()
        data = [
            {
                "id": s.id,
                "movie": s.movie,
                "hall": s.hall,
                "date_time": s.date_time,
                "seats": s.seats
            }
            for s in sessions
        ]
        return Response(SESSIONS_DB, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        
        movie = data.get("movie")
        if not movie or not isinstance(movie, str) or movie.strip() == "":
            return Response({"error": "Field 'movie' is required and cannot be empty."}, status=status.HTTP_400_BAD_REQUEST)

        session = Session.objects.create(
            movie=movie,
            hall=data.get("hall", "Основной зал"),
            date_time=data.get("date_time", "2026-06-01T18:00:00Z"),
            seats=data.get("seats", 50)
        )

        return Response({
            "id": session.id,
            "movie": session.movie,
            "hall": session.hall,
            "date_time": session.date_time,
            "seats": session.seats
        }, status=status.HTTP_201_CREATED)

class SessionDetailView(APIView):
    def get_object(self, pk):
        try:
            return Session.objects.get(pk=pk)
        except Session.DoesNotExist:
            return None

    def get(self, request, pk):
        session = self.get_object(pk)
        if not session:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({
            "id": session.id,
            "movie": session.movie,
            "hall": session.hall,
            "date_time": session.date_time,
            "seats": session.seats
        }, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        session = self.get_object(pk)
        if not session:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        if "movie" in data:
            movie = data.get("movie")
            if not movie or not isinstance(movie, str) or movie.strip() == "":
                return Response({"error": "Field 'movie' cannot be empty."}, status=status.HTTP_400_BAD_REQUEST)
            session.movie = movie
            
        if "hall" in data:
            session.hall = data.get("hall")
        if "date_time" in data:
            session.date_time = data.get("date_time")
        if "seats" in data:
            session.seats = data.get("seats")

        session.save()
            
        return Response({
            "id": session.id,
            "movie": session.movie,
            "hall": session.hall,
            "date_time": session.date_time,
            "seats": session.seats
        }, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        session = self.get_object(pk)
        if not session:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)