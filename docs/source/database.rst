Database Structure and Models
===========================

OC Lettings uses a relational database to store information about properties, addresses, and user profiles.

Database Schema
--------------

.. image:: _static/db_schema.png
   :alt: Database Schema
   :align: center

Models
------

Address Model
~~~~~~~~~~~~

.. code-block:: python

   class Address(models.Model):
       number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
       street = models.CharField(max_length=64)
       city = models.CharField(max_length=64)
       state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
       zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
       country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

       def __str__(self):
           return f'{self.number} {self.street}'

Letting Model
~~~~~~~~~~~~

.. code-block:: python

   class Letting(models.Model):
       title = models.CharField(max_length=256)
       address = models.OneToOneField(Address, on_delete=models.CASCADE)

       def __str__(self):
           return self.title

Profile Model
~~~~~~~~~~~~

.. code-block:: python

   class Profile(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE)
       favorite_city = models.CharField(max_length=64, blank=True)

       def __str__(self):
           return self.user.username

Relationships
------------

- A **Letting** has one **Address** (one-to-one relationship)
- A **Profile** belongs to one **User** (one-to-one relationship)
- Each **User** can have one **Profile**
