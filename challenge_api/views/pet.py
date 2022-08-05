from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from rest_framework.response import Response
from challenge_api.models import Pet, PetType
from django.contrib.auth.models import User



class PetSerializer(serializers.ModelSerializer):
    """The Pet Serializer - Add your code below this line"""
    class Meta:
        model = Pet
        fields = ('id', 'name', 'age', 'type', 'user', 'favorite_activity')


class PetView(ViewSet):
    """The Pet View class - Add your code below this line"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type"""
        try:
            pet = Pet.objects.get(pk=pk)
            serializer = PetSerializer(pet)
            return Response(serializer.data)
        except Pet.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """_summary_gets all the pets trying to get rid of missing docstring error

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)
    def create(self, request):
        """Handle POST operations"""
        pettype = PetType.objects.get(pk=request.data["type"])
        user = User.objects.get(pk=request.auth.user_id)

        pet = Pet.objects.create(
            name=request.data["name"],
            age=request.data["age"],
            favorite_activity=request.data["favorite_activity"],
            type=pettype,
            user=user
            
        )
        serializer = PetSerializer(pet)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        pet = Pet.objects.get(pk=pk)
        pet.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
