from rest_framework import serializers

from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

    MAX_FILE_SIZE_MB = 100
    ALLOWED_FILE_TYPES = ['videos/mp4', 'videos/avi', 'videos/mov']

    def validate_video_file(self, value):
        if value.content_type not in self.ALLOWED_FILE_TYPES:
            raise serializers.ValidationError(f"Ruxsat berilgan fayl turlari: {', '.join(self.ALLOWED_FILE_TYPES)}")
        if value.size > self.MAX_FILE_SIZE_MB:
            raise serializers.ValidationError(f"Fayl hajmi {self.MAX_FILE_SIZE_MB} MB'dan oshmasligi kerak.")
