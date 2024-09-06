from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer
from django.shortcuts import render

# List all stocks or create a new stock
# This view handles GET requests to list all stocks and POST requests to create a new stock.
@api_view(['GET', 'POST'])
def stock_list(request):
    if request.method == 'GET':
        # Retrieve all stock objects from the database
        stocks = Stock.objects.all()
        # Serialize the stock objects to JSON format
        serializer = StockSerializer(stocks, many=True)
        # Return the serialized data in the response
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # Deserialize the request data into a Stock object
        serializer = StockSerializer(data=request.data)
        # Check if the data is valid
        if serializer.is_valid():
            # Save the new stock to the database
            serializer.save()
            # Return the created stock data and HTTP 201 status
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is invalid, return an error with HTTP 400 status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, update, or delete a specific stock
# This view handles GET, PUT, and DELETE requests for a specific stock by ID.
@api_view(['GET', 'PUT', 'DELETE'])
def stock_detail(request, stock_id):
    try:
        # Attempt to retrieve the stock by its ID
        stock = Stock.objects.get(id=stock_id)
    except Stock.DoesNotExist:
        # If the stock does not exist, return a 404 error
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Serialize the stock object to JSON format
        serializer = StockSerializer(stock)
        # Return the serialized data in the response
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # Deserialize the request data into the existing stock object
        serializer = StockSerializer(stock, data=request.data)
        # Check if the data is valid
        if serializer.is_valid():
            # Save the updated stock to the database
            serializer.save()
            # Return the updated stock data
            return Response(serializer.data)
        # If the data is invalid, return an error with HTTP 400 status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        # Delete the stock from the database
        stock.delete()
        # Return a response with HTTP 204 status (no content)
        return Response(status=status.HTTP_204_NO_CONTENT)

# Render the homepage
# This view renders the index.html template for the frontend.
def home(request):
    return render(request, 'index.html')
