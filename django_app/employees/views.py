from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from datetime import datetime
from django.db import transaction

from django.core.exceptions import ValidationError
from .models import Employees
from .serializers import EmployeesSerializer
from .validations import custom_validation

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def employees_list(request):
    try:
        # Get the page number from the query parameter (default: 1)
        page_number = request.query_params.get('page_number', 1)
        # Get the desired page size from the query parameter (default: 10)
        page_size = request.query_params.get('page_size', 10)

        first_name = request.query_params.get('first_name', '')
        last_name = request.query_params.get('last_name', '')
        email = request.query_params.get('email', '')
        gender = request.query_params.get('gender')
        # Get the date filter from the query parameter (e.g., 'yyyy-mm-dd')
        dob = request.query_params.get('dob', '')
        employees = Employees.objects.all()

        # Apply the "ilike" filter if a search term is provided for the following field
        if first_name:
            employees = employees.filter(first_name__icontains = first_name)

        if last_name:
            employees = employees.filter(last_name__icontains = last_name)

        if email:
            employees = employees.filter(first_name__icontains = email)

        if gender:
            employees = employees.filter(gender = gender)
        if dob:
            # Parse the date string to a datetime object
            date = datetime.strptime(dob, '%Y-%m-%d').date()
                
            # Use Q objects to filter by date of birth
            employees = employees.filter(Q(dob=date))
         # Create a PageNumberPagination instance and paginate the queryset
        paginator = PageNumberPagination()
        paginator.page = page_number
        paginator.page_size = page_size
        paginated_employees = paginator.paginate_queryset(employees, request)

        serializer = EmployeesSerializer(paginated_employees , many=True)
        # Build the response with paginated data and metadata
        response_data = {
            'total_pages': paginator.page.paginator.num_pages,
            'total_items': paginator.page.paginator.count,
            'data': serializer.data,
        }
        return Response(response_data)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def employee_create(request):
    with transaction.atomic():
        try:
            # Perform custom data validation
            data = custom_validation(request.data)
            
            # Serialize and validate the data
            serializer = EmployeesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                # Send a welcome email
                try:
                    send_welcome_mail('manoj@zogato.com')
                except:
                    raise Exception("Error in sending mail")
                
                # Return a success response
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            # If data is not valid, raise a validation error
            raise ValidationError({"message": "Bad request", "status_code": status.HTTP_400_BAD_REQUEST})
    
        except ValidationError as e:
            # Rollback the transaction and handle the validation error
            transaction.set_rollback(True)
            error_message = dict(e)
            return Response({"message": error_message["message"][0], "status": "failed"}, status=error_message["status_code"][0])
        
        except Exception as e:
            # Rollback the transaction and handle other exceptions
            transaction.set_rollback(True)
            print(str(e))
            return Response({"message": "Something went wrong", "status": "failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def send_welcome_mail(data):
    
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    message = Mail(
        from_email='manoj@zogato.com',
        to_emails='manoj@zogato.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient('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')
        sg.send(message)
    except Exception as e:
        print(str(e))
        raise Exception(e)