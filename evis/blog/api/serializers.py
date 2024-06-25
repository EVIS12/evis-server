import re

from rest_framework import serializers

from evis.blog.models import Blog, News, Testimonials


class BaseSerializerMixin(serializers.ModelSerializer):
    class Meta:
        read_only_fields = ["id", "created_at", "updated_at"]


class BaseBlogSerializer(BaseSerializerMixin):
    class Meta(BaseSerializerMixin.Meta):
        model = Blog
        fields = [
            "id",
            "title",
            "subtitle",
            "body",
            "photo",
            "schedule",
            "status",
            "view_count",
            "date_time",
            "created_at",
            "updated_at",
        ]


class BlogListSerializer(BaseBlogSerializer):
    pass


class BlogDetailSerializer(BaseBlogSerializer):
    pass


class BaseNewsSerializer(BaseSerializerMixin):
    class Meta(BaseSerializerMixin.Meta):
        model = News
        fields = ["id", "title", "body", "photo", "link", "created_at", "updated_at"]


class NewsListSerializer(BaseNewsSerializer):
    pass


class NewsDetailSerializer(BaseNewsSerializer):
    pass


def get_youtube_video_id(link):
    regex = r"(?<=v=)[\w-]+|(?<=youtu.be/)[\w-]+"
    match = re.search(regex, link)
    if match:
        return match.group(0)
    return None


def is_youtube_link(link):
    return re.match(r"(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.*", link)


class TestimonialsSerializer(serializers.ModelSerializer):
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

    # def create(self, validated_data):
    #     # check if youtube link is valid or not before creating
    #     youtube_link = validated_data.get("youtube_link", "")
    #     if not is_youtube_link(youtube_link):
    #         raise serializers.ValidationError("It is not a YouTube link.")
    #     return super().create(validated_data)
