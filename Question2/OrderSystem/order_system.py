"""
This is mostly psuedo-code to demonstrate concepts
"""

from sampleApp.models import Customer, Order, Product
from django.db import IntegrityError, transaction


def get_order(order_id: str) -> Order:
    # get order model that matches order_id supplied
    order = [order for order in Order.objects.all() if order_id == order.order_id]
    return order


@transaction.atomic
def create_order(product_ids: list) -> tuple:
    # create new order and save to database
    """
    implement database integrity methods. depending on which database is used (postgreSQL, etc.)
    atomic transactions can be used to handle concurrent database interactions which could desync
    database between user sessions. If the block of code is successfully completed, the changes are committed to the database.
    If there is an exception, the changes are rolled back.
    """
    order_id = create_new_order_object().order_id
    try:
        with transaction.atomic:
            create_relationships()
    except IntegrityError:
        handle_exception()

    add_new_order_to_db()
    return order_id, product_ids


@transaction.atomic
def update_order(order_id: str, product_ids: list) -> tuple:
    # update order and save to database
    """
    implement database integrity methods. depending on which database is used (postgreSQL, etc.)
    atomic transactions can be used to handle concurrent database interactions which could desync
    database between user sessions. If the block of code is successfully completed, the changes are committed to the database.
    If there is an exception, the changes are rolled back.
    """
    try:
        with transaction.atomic:
            update_relationships(order_id=order_id, product_id_list=product_ids)
    except IntegrityError:
        handle_exception()

    update_existing_order_in_db()
    return order.order_id, product_ids


@transaction.atomic
def delete_order(order_id) -> str:
    # delete order and save to database
    """
    implement database integrity methods. depending on which database is used (postgreSQL, etc.)
    atomic transactions can be used to handle concurrent database interactions which could desync
    database between user sessions. If the block of code is successfully completed, the changes are committed to the database.
    If there is an exception, the changes are rolled back.
    """
    order = Order.objects.filter(order_id=order_id)
    try:
        with transaction.atomic:
            delete_relationships(order_id=order_id)
    except IntegrityError:
        handle_exception()

    remove_order_in_db()
    return order.order_id
