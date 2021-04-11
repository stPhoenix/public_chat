import re
from rest_framework import serializers
from api.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields =  '__all__'

    def validate_author(self, value):
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if re.search(regex, value) is False:
            raise serializers.ValidationError("Email is not correct")
        return value


    def validate_text(self, value):
        if len(value) == 0 or len(value) > 100:
            raise serializers.ValidationError(
                "Text can't be empty or has more than 100 characters")
        return value
    

