# How to use the api

## Through Postman:
### 1. Invoice API = 127.0.0.1:8000/invoice/
#### For GET request add a parameter invoice_no and set its value to an invoice number that already exists in the database. Make sure the data is already there
<p align="center">
    <img src =https://github.com/Ayush19-01/Digital-Marketing-Lane/blob/main/Screenshot%202023-03-18%20202152.png>
</p>

#### For POST request, add body in raw and json format use the given format in the image to parse the data.
<p align="center">
    <img src =https://github.com/Ayush19-01/Digital-Marketing-Lane/blob/main/Screenshot%202023-03-18%20202338.png>
</p>

### 2. Invoice Detail API = 127.0.0.1:8000/invoice_detail/
#### For GET request add a parameter invoice_no and set its value to an invoice number that already exists in the database. Make sure the data is already there
<p align="center">
    <img src =https://github.com/Ayush19-01/Digital-Marketing-Lane/blob/main/Screenshot%202023-03-18%20202104.png>
</p>

#### For POST request, add body in raw and json format use the given format in the image to parse the data.
<p align="center">
    <img src =https://github.com/Ayush19-01/Digital-Marketing-Lane/blob/main/Screenshot%202023-03-18%20202247.png>
</p>
## Through browser(django apiview)
### 1. Invoice API = 127.0.0.1:8000/invoice/
#### Type the following link for GET request: 

```python
127.0.0.1:8000/invoice/?invoice_no=x
```
#### Here replace x with the invoice number that already exists in the database

#### For POST request, open the following link:

```python
127.0.0.1:8000/invoice/
```

#### and add the payload in the following format:

```json
{ 
  "invoice_no" : 1,
  "cust_name" : "y",
}
  ```
  ### Here replace 1 with the invoice number and x with the customer name and click post
  
### 2. Invoice Detail API = 127.0.0.1:8000/invoice_detail/
#### Type the following link for GET request: 

```python
127.0.0.1:8000/invoice_detail/?invoice_no=x
```
#### Here replace x with the invoice number that already exists in the database

#### For POST request, open the following link:

```python
127.0.0.1:8000/invoice_detail/
```

#### scroll down and add the payload in the following format:

```json
{ 
  "invoice_no" : 1,
  "desc" : "",
  "quantity": 2,
  "unit_price": 20,
}
  ```
  ### Here replace 1 with the invoice number, write the description, set quantity and add unit price then click post.
