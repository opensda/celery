from rest_framework import serializers

ALLOWED_LINK = ["youtube"]


def video_link_validator(value):
    """Проверяем, загружено ли видео с YouTube или нет"""
    values = value.split(".")
    if values[1].lower() not in ALLOWED_LINK:
        raise serializers.ValidationError(
            "Ссылку можно размещать только на youtube.com"
        )
