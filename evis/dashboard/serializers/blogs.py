from rest_framework import serializers

from evis.blog.api.serializers import get_youtube_video_id, is_youtube_link
from evis.blog.models import Blog, News, Testimonials


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "title", "photo", "view_count", "status", "press_center", "home_page"]


class BlogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

    def validate(self, attrs):
        if attrs["home_page"] and Blog.objects.filter(home_page=True).count() >= 3:
            raise serializers.ValidationError("Home Page has the maximum limit of Blog.")
        elif attrs["press_center"] and Blog.objects.filter(press_center=True).count() >= 3:
            raise serializers.ValidationError("Press Center Page has the maximum limit of Blog.")
        return attrs


class BlogUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

    def validate(self, attrs):
        try:
            if attrs["home_page"] and Blog.objects.filter(home_page=True).count() >= 3:
                raise serializers.ValidationError("Home Page has the maximum limit of Blogs.")
        except KeyError:
            pass
        try:
            if attrs["press_center"] and Blog.objects.filter(press_center=True).count() >= 3:
                raise serializers.ValidationError("Press Center Page has the maximum limit of Blogs.")
        except KeyError:
            pass
        return attrs


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["id", "title", "body", "photo", "link", "press_center"]


class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = ["created_at", "updated_at"]

    def validate(self, attrs):
        if attrs["press_center"] and News.objects.filter(press_center=True).count() >= 3:
            raise serializers.ValidationError("Press Center Page has the maximum limit of News.")
        return attrs


class NewsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = ["created_at", "updated_at"]

    def validate(self, attrs):
        try:
            if attrs["press_center"] and News.objects.filter(press_center=True).count() >= 3:
                raise serializers.ValidationError("Press Center Page has the maximum limit of News.")
        except KeyError:
            pass
        return attrs


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class TestimonialsListSerializer(serializers.ModelSerializer):
    video_id = serializers.SerializerMethodField()

    class Meta:
        model = Testimonials
        fields = ["id", "name", "photo", "youtube_link", "video_id", "press_center", "company"]

    def get_video_id(self, obj):
        youtube_link = obj.youtube_link
        if youtube_link == "":
            return None
        video_id = get_youtube_video_id(youtube_link)
        if video_id:
            return video_id
        return None


class TestimonialsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        exclude = ["created_at", "updated_at"]

    def validate(self, attrs):
        try:
            if attrs["press_center"] and Testimonials.objects.filter(press_center=True).count() >= 3:
                raise serializers.ValidationError("Press Center Page has the maximum limit of Testimonials.")
        except KeyError:
            pass
        return attrs

    def update(self, instance, validated_data):
        youtube_link = validated_data.get("youtube_link", "")
        if not is_youtube_link(youtube_link):
            raise serializers.ValidationError("It is not a YouTube link.")
        return super().update(instance, validated_data)


class TestimonialsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        exclude = ["created_at", "updated_at"]

    def validate(self, attrs):
        if attrs["press_center"] and Testimonials.objects.filter(press_center=True).count() >= 3:
            raise serializers.ValidationError("Press Center Page has the maximum limit of Testimonials.")
        return attrs

    def create(self, validated_data):
        youtube_link = validated_data.get("youtube_link", "")
        if not is_youtube_link(youtube_link):
            raise serializers.ValidationError("It is not a YouTube link.")
        return super().create(validated_data)


class TestimonialsDetailSerializer(serializers.ModelSerializer):
    video_id = serializers.SerializerMethodField()

    class Meta:
        model = Testimonials
        fields = "__all__"

    def get_video_id(self, obj):
        youtube_link = obj.youtube_link
        if youtube_link == "":
            return None
        video_id = get_youtube_video_id(youtube_link)
        if video_id:
            return video_id
        return None
