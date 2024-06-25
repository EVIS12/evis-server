from rest_framework import serializers

from evis.blog.api.serializers import get_youtube_video_id, is_youtube_link
from evis.blog.models import Blog, News, Testimonials


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "title", "photo", "view_count"]


class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ["id", "view_count", "created_at", "updated_at"]


class BlogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["id", "title", "body", "photo", "link"]


class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = ["id", "created_at", "updated_at"]


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class TestimonialsListSerializer(serializers.ModelSerializer):
    video_id = serializers.SerializerMethodField()

    class Meta:
        model = Testimonials
        fields = ["id", "name", "photo", "youtube_link", "video_id"]

    def get_video_id(self, obj):
        youtube_link = obj.youtube_link
        if youtube_link == "":
            return None
        video_id = get_youtube_video_id(youtube_link)
        if video_id:
            return video_id
        return None


class TestimonialsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        exclude = ["id", "created_at", "updated_at"]

    def create(self, validated_data):
        youtube_link = validated_data.get("youtube_link", "")
        if not is_youtube_link(youtube_link):
            raise serializers.ValidationError("It is not a YouTube link.")
        return super().create(validated_data)


class TestimonialsDetailSerializer(serializers.ModelSerializer):
    video_id = serializers.SerializerMethodField()

    class Meta:
        model = Testimonials
        exclude = ["id", "created_at", "updated_at", "press_center"]

    def get_video_id(self, obj):
        youtube_link = obj.youtube_link
        if youtube_link == "":
            return None
        video_id = get_youtube_video_id(youtube_link)
        if video_id:
            return video_id
        return None
