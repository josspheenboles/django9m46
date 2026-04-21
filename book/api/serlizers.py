from rest_framework import serializers

class BookSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    version = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    publish_date = serializers.DateField()
    # catagory = serializers.ForeignKey(Catagory, on_delete=models.CASCADE)
