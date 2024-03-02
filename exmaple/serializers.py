from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# class SnippeSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language =  serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')


#     def create(self, validated_data):
#         """
#         Créez et renvoyez une nouvelle instance `Snippet`, compte tenu des données validées.
#         """
#         return Snippet.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """
#         Mettez à jour et renvoyez une instance 'Snippet' existante, compte tenu des données validées.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance


# Raccourci avec ModelSerializer qui implemente déjà les méthodes create et update
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']


class UserSerialiser(serializers.ModelSerializer):
    """
    - Points de terminaison pour nos modèles user
    - Ajout de répresentant de ces users à notre API
    """
    snippets = serializers.PrimaryKeyRelatedField(many=True,
                                        queryset=Snippet.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
