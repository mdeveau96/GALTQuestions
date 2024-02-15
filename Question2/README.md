# Question 2: Order Processing System

I've attached a sample django rest API project only with files that are edited to demonstrate how system structure would look.

## API Endpoints:

### 1. Placing an order:

**Endpoint:** `POST /orders`

**Request Body:**

```
{
    "products": [
        {
            "product_id": "string",
            "item_count": int
        },
        {
            ...
        }
    ]
}

```

- The user's token/authorization code would be passed in the header of the request

**200 Response:**

```
{
    "message": Success! Order placed,
    "order_id": "string",
    "products": [
        {
            "product_id": "string",
            "product_count": int
        },
        {
            ...
        }
    ]
}
```

- Successful response returns success message, order ID for user to reference later, and a list of what they previously ordered. This would then update the inventory service (via a database call) to update the product_count of each product that is in the previous order to ensure the correct number of available products is displayed for future sessions.

**400 Response:**

```
{
    "error": "Invalid request. Please review your request and ensure everything is correct.",
    "documentation": "https://helpful.link/"
}
```

- API returns 400 error code due to incorrectly formed request

**404 Response:**

```
{
    "error": "Product out of stock.",
    "documentation": "https://helpful.link/"
}
```

- API returns 404 and error message is displayed indicting product is out of stock. Order system checks the inventory system to check is product is in stock using the product_count attribute. If product is out-of-stock order is refused.

**Possible Edge Cases and Error Scenarios with POST Requests:**

1. Simultaneous Orders:
   - Users who submit orders for a product that is limited in stock will cause synchronization issues with inventory database system and website. To mitigate this, database locking mechanisms or Optimistic concurrency control can be used to ensure integrity of data. OCC is able to validate that the data has or has not been modified. If a conflict occurs then a method to resolve the conflict will occur.
2. Some Products are out of stock in an order:
   - In some orders an item may be out-of-stock causing the API to return a 404 to the user and cancel order. To mitigate this the system will record the products that are out of stock via the product_count attribute, continue to fulfill the products that are in stock, and then inform the user which products were out of stock. Lastly, update inventory status for out-of-stock products.
3. Invalid Requests:
   - Possible Request errors can occur and malformed requests can cause instability and system issues. Validation checks can be applied to API to ensure requests are correctly structured and security vulnerabilities are mitigated.
4. Inventory Service unreachable:
   - There may be an occurrence where the inventory system will be unreachable and data is not able to be read by order system. Retry methods can be implemented and timeouts in the event that service is reachable. An alert system would also notify admins to issue.

## 2. Viewing order status:

**Endpoint:** `GET /orders/{order_id}`

- The user's token/authorization code would be passed in the header of the request

**200 Response:**

```
{
    "order_id": "String",
    "order_status": "String",
    "products": [
        {
            "product_id": "string",
            "item_count": int
        },
        {
            ...
        }
    ]
}
```

- Successful response returns 200 Response code, order_id, order_statue, and the products that are in the order.

**400 Response:**

```
{
    "error": "Invalid request. Please review your request and ensure everything is correct.",
    "documentation": "https://helpful.link/"
}
```

- API returns 400 error code due to incorrectly formed request

**404 Response:**

```
{
    "error": "Order not found. Ensure supplied order_id is correct."
    "documentation": "https://helpful.link/"
}
```

- API returns 404 error cude due to order_id not being found

**Possible Edge Cases and Error Scenarios with GET Requests:**

1. Incorrect order_id supplied:
   - User sends incorrect order_id in GET request. Efficient error handles and documentation links on how to correctly order system can be supplied in response.

## 3. Canceling an order:

**Endpoint:** `DELETE /orders/{order_id}`

**200 Response:**

```
{
    "message": "Order successfully cancelled"
}
```

- API returns success message to user and inventory system is update to reflect new product_count for cancelled order.

**400 Response:**

```
{
    "error": "Invalid request. Please review your request and ensure everything is correct.",
    "documentation": "https://helpful.link/"
}
```

- API returns 400 error code due to incorrectly formed request

**404 Response:**

```
{
    "error": "Order not found. Ensure supplied order_id is correct."
    "documentation": "https://helpful.link/"
}
```

- API returns 404 error cude due to order_id not being found

**Possible Edge Cases and Error Scenarios with DELETE Requests:**

1. 1. Simultaneous Orders deletion:
   - Users who delete orders for a product that is limited in stock will cause synchronization issues with inventory database system and order system. To mitigate this, database locking mechanisms or Optimistic concurrency control can be used to ensure integrity of data. OCC is able to validate that the data has or has not been modified. If a conflict occurs then a method to resolve the conflict will occur.

## 4. Updating an order:

**Endpoint:** `PATCH /orders/{order_id}`

**200 Response:**

```
{
    "message": "Order successfully updated",
    "order_id": "String",
    "order_status": "String",
    "products": [
        {
            "product_id": "string",
            "item_count": int
        },
        {
            ...
        }
    ]
}
```

- API returns success message, order_id of updated order, current order_status, and products that have either been added or removed. The inventory system is then updated to reflect new item stock values.

**400 Response:**

```
{
    "error": "Invalid request. Please review your request and ensure everything is correct.",
    "documentation": "https://helpful.link/"
}
```

- API returns 400 error code due to incorrectly formed request

**404 Response:**

```
{
    "error": "Order not found. Ensure supplied order_id is correct."
    "documentation": "https://helpful.link/"
}
```

- API returns 404 error cude due to order_id not being found

**Possible Edge Cases and Error Scenarios with PATCH Requests:**

1. 1. Simultaneous Orders update:
   - Users who update orders for a product that is limited in stock will cause synchronization issues with inventory database system and order system. To mitigate this, database locking mechanisms or Optimistic concurrency control can be used to ensure integrity of data. OCC is able to validate that the data has or has not been modified. If a conflict occurs then a method to resolve the conflict will occur.
