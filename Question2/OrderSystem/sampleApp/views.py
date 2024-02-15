from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from order_system import get_order, create_order, update_order, delete_order


# Create your views here.
@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def orders(request):
    if request.method == 'GET':
        # Checks to ensure request headers and body are correct
        order_id = request.build_absolute_uri().split("/")[4]
        if request.headers.authorization:
            return Response({"message": "success", "products": get_order(order_id)})
        else:
            return Response({"error": "reason"}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        # Checks to ensure request headers and body are correct
        if request.headers.authorization:
            product_ids = request.body.get('products')
            order_id, product_id_list = create_order(product_ids=product_ids)
            return Response({"message": "success", "order_id": order_id, "products": product_id_list})
        else:
            return Response({"error": "reason"}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PATCH':
        # Checks to ensure request headers and body are correct
        if request.headers.authorization and request.body.get('order_id'):
            order_id, product_id_list = update_order(order_id=order_id, product_ids=product_ids)
            return Response({"message": "success"}, "")
        else:
            return Response({"error": "reason"}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        # Checks to ensure request headers and body are correct
        order_id = request.build_absolute_uri().split("/")[4]
        if request.headers.authorization:
            try:
                delete_order(order_id=order_id)
                return Response({"message": "success"})
            except Exception:
                return Response({"error": "reason"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "reason"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"error": "reason"}, status=status.HTTP_400_BAD_REQUEST)
    
# Other endpoints can be added here for customer profiles and product endpoints