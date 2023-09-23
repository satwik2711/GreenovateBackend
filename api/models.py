from django.db import models

class Factor(models.Model):
    name = models.CharField(max_length=255)

class SubFactor(models.Model):
    name = models.CharField(max_length=255)
    factor = models.ForeignKey(Factor, on_delete=models.CASCADE)

class SubSubFactor(models.Model):
    name = models.CharField(max_length=255)
    sub_factor = models.ForeignKey(SubFactor, on_delete=models.CASCADE)
    emission_factor = models.FloatField()

class Organisation(models.Model):
    name = models.CharField(max_length=255)

class EmissionRecord(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    sub_sub_factor = models.ForeignKey(SubSubFactor, on_delete=models.CASCADE)
    input_value = models.FloatField()
    record_year = models.IntegerField()

    @property
    def net_emission(self):
        return self.input_value * self.sub_sub_factor.emission_factor
    
class Tips(models.Model):
    factor = models.ForeignKey(Factor, on_delete=models.CASCADE)
    tip = models.TextField()

    def __str__(self):
        return self.tip