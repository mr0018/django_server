from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.exceptions import ValidationError

from .serializers import DepartmentsSerializer, GetDepartmentWithHod
from .validations import custom_validation
from .models import Department

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def department_create(request):
    try:
         # Perform custom data validation
        data = custom_validation(request.data)
        
        # Serialize and validate the data
        serializer = DepartmentsSerializer(data=data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        raise ValidationError({"message": "Bad request", "status_code": status.HTTP_400_BAD_REQUEST})
    except ValidationError as e:
            error_message = dict(e)
            return Response({"message": error_message["message"][0], "status": "failed"}, status=error_message["status_code"][0])
    except Exception as e:
        print(str(e))
        return Response({"message": "Something went wrong", "status": "failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_department(request):
    try:
        department = Department.objects.select_related('hod_id').all()
        serializer = GetDepartmentWithHod(department,many=True)
        return Response(serializer.data)
    except Exception as e:
        print(str(e))
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)