from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    founded = models.CharField(max_length=150)
    financial_information = models.TextField(default='')
    partners_and_investors = models.TextField()
    

    class Meta():
        verbose_name = "Company"
        verbose_name_plural = "Companies"
    
    def __str__(self):
        return f"name: {self.name}, description: {self.description}, founded: {self.founded}, financial_information: {self.financial_information}, partners_and_investors: {self.partners_and_investors}"
    
    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "founded": self.founded,
            "financial_information": self.financial_information,
            "partners_and_investors": self.partners_and_investors
        }
    
class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    platforms = models.CharField(max_length=100)
    relase_date = models.DateField()
    reviews_and_ratings = models.CharField(max_length=150)
    sales = models.FloatField()
    financial_results = models.CharField(max_length=150)
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta():
        verbose_name = "Game"
        verbose_name_plural = "Games"
    
    def __str__(self):
        return f"name: {self.name}, description: {self.description}, genre: {self.genre}, platforms: {self.platforms}, relase_date: {self.relase_date}, reviews_and_ratings: {self.reviews_and_ratings}, sales: {self.sales}, financial_results: {self.financial_results}, company: {self.company}"
    
    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "genre": self.genre,
            "platforms": self.platforms,
            "relase_date": self.relase_date,
            "reviews_and_ratings": self.reviews_and_ratings,
            "sales": self.sales,
            "financial_results": self.financial_results,
            "company": self.company.to_json()
        }
