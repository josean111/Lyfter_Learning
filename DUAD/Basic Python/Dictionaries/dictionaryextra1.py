# # Dada una lista de ventas con la siguiente información:
# # date
# # customer_email
# # items
# # Y cada item teniendo la siguiente información:
# # name
# # upc
# # unit_price
# # Cree un diccionario que guarde el total de ventas de cada UPC.
# # Ejemplos:
# # Entrada: sales = [
# 	{
# 		'date': '27/02/23',
# 		'customer_email': 'joe@gmail.com',
# 		'items': [
# 			{
# 				'name': 'Lava Lamp',
# 				'upc': 'ITEM-453',
# 				'unit_price': 65.76,
# 			},
# 			{
# 				'name': 'Iron',
# 				'upc': 'ITEM-324',
# 				'unit_price': 32.45,
# 			},
# 			{
# 				'name': 'Basketball',
# 				'upc': 'ITEM-432',
# 				'unit_price': 12.54,
# 			},
# 		],
# 	},
# 	{
# 		'date': '27/02/23',
# 		'customer_email': 'david@gmail.com',
# 		'items': [
# 			{
# 				'name': 'Lava Lamp',
# 				'upc': 'ITEM-453',
# 				'unit_price': 65.76,
# 			},
# 			{
# 				'name': 'Key Holder',
# 				'upc': 'ITEM-23',
# 				'unit_price': 5.42,
# 			},
# 		],
# 	},
# 	{
# 		'date': '26/02/23',
# 		'customer_email': 'amanda@gmail.com',
# 		'items': [
# 			{
# 				'name': 'Key Holder',
# 				'upc': 'ITEM-23',
# 				'unit_price': 3.42,
# 			},
# 			{
# 				'name': 'Basketball',
# 				'upc': 'ITEM-432',
# 				'unit_price': 17.54,
# 			},
# 		],
# 	},
# ]

# Salida result = {
# 	'ITEM-453': 131.52,
# 	'ITEM-324': 32.45,
# 	'ITEM-432': 30.08,
# 	'ITEM-23': 8.84,
# }

print ("---- Dada una lista de ventas con la siguiente información, Cree un diccionario que guarde el total de ventas de cada UPC. ----")
sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]
# print(sales[0].items())
# print(sales[0])
# sales_items = sales[0].values()
# print(sales_items)
# print(sales[0].get("items")[0].get("upc"))
# print(sales[0].get("items")[0])
# print(type((sales)) == list)
# print(len(sales[0].get("items")[0]))
# print(len(sales[1].get("items")[0]))
# print(len(sales[2].get("items")[0]))
#print(len(sales)[0][0])
sales_total = {}
for x in sales:
    # print(f"X - {x} ++++++++++++++++++++++++ type {type(x)}")
    for y in x.items():
        #  print(f"Y - {y} ++++++++++++++++++++++++ type {type(y)}")11
        for z in y:
            # print(f"Z - {z} ++++++++++++++++++++++++ type {type(z)}")
            if type(z) == list:
                for a in z:
                    # print(f"a - {a} ++++++++++++++++++++++++ type {type(a)}")
                    if sales_total.get(a.get("upc")) is None:
                        sales_total[a.get("upc")] =  a.get("unit_price")
                    else:
                        sales_total[a.get("upc")] +=  a.get("unit_price")
print(f"Lista de Precios: {sales_total}")                        



#v2
sales_total2 = {}

for sale in sales:
    for item in sale["items"]:

        if item["upc"] not in sales_total2:
            sales_total2[item["upc"]] = item["unit_price"]
        else:
            sales_total2[item["upc"]] += item["unit_price"]
print("Lista de Precios:")   
for upc, price in sales_total2.items():
    print(f"{upc}: ${price:.2f}")
