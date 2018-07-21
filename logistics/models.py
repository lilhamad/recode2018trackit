from django.db import models

class Shipment(models.Model):
	shipment_comp = models.CharField(max_length = 200)
	pur_date = models.DateTimeField('date purchased')

class Transaction(models.Model):
	shipment_id = models.ForeignKey(Shipment, on_delete = models.CASCADE)
	product_price =IntegerField(default= 0)
	weight = models.IntegerField(default= 0)	
	dilivery_price = models.IntegerField(default= 0)

class Step(models.Model):
	name = models.CharField(max_length = 200)
	status = models.CharField(max_length= 200)


class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)		

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

class invoice(models.Model):
	invoice_date = modles.DateTimeField('document date')
	step_id = models.ForeignKey(Step, on_delete= models.CASCADE)

									