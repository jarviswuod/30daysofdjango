from accounts.models import *

# ***(1) Returns all customer table
customers = Customer.objects.all()

# (2) Returns first customer in table
firstCustomer = Customer.objects.first()

# (3) Returns last customer in table
lastCustomers = Customer.objects.last()

# ***(4) Returns single customer by name
customersByName = Customer.objects.get(name='Peter Piper')

# ***(5) Returns all customer table
customersById = Customer.objects.get(id=4)

# ***(6) Returns all orders related to customer (firstCustomer variable set above)
firstCustomer.order_set.all()

# ***(7) Returns orders customer name (Query parent model values)
order = Order.objects.first()
parentName = order.customer.name

# ***(8) Returns products from products table with value of "Out Door" in category attribute
products = Products.objects.filter(category="Out Door")

# ***(9) Order/ Sort Objects by id
leastToGreatest = Products.objects.all().order_by('id')
greatestToLeast = Products.objects.all().order_by('-id')

# ***(10) Returns all products wih tag of "Sports": (Query Many to Many Fields)
productsFiltered = Products.objects.filter(tags__name="Sports")

'''
(11) Bonus
Q: If the customer has more than 1 ball, how would you reflect it in the database

A: Because there are many different products and this value changes constantly you would  most
likely not want to store the value in the database but rather just make this a function we can 
run each time we load the customers profile
'''

# Returns the total count for number of time a "Ball was ordered by the first customer
ballOrders = firstCustomer.order_set.filter(product__name="Ball").count()

# Returns total count for each product ordered
allOrders = {}

for order in firstCustomer.order_set.all():
    if order.products.name in allOrders:
        allOrders[order.products.name] += 1
    else:
        allOrders[order.products.name] = 1


# Returns: allOrders: {'Ball':2, 'BBQ Grill':1}


# RELATED SET EXAMPLE
class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)


class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200, null=True)


parent = ParentModel.objects.first()
# Returns all child models related to parent
parent.childmodel_set.all()
