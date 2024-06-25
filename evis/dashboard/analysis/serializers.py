from django.db.models import Sum
from django.utils import timezone
from rest_framework import serializers

from evis.blog.models import Blog
from evis.dashboard.models import AboutViews, RegistrationViews, TotalVisitor
from evis.users.models import RegisterLink


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "title", "photo", "view_count"]
        read_only_fields = ("id", "created_at", "updated_at")


class TotalVisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalVisitor
        fields = ["id", "count"]
        read_only_fields = ("id",)


class TotalVisitorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalVisitor
        fields = ["id", "count"]
        read_only_fields = ("id",)


class AboutViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutViews
        fields = ["id", "count"]
        read_only_fields = ("id",)


class AboutViewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutViews
        fields = ["id", "count"]
        read_only_fields = ("id",)


class RegistrationViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationViews
        fields = ["id", "count"]
        read_only_fields = ("id",)


class RegisterLinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterLink
        fields = ["id", "type", "rank"]
        read_only_fields = ("id",)


class RegisterLinkDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterLink
        fields = ["id", "link", "type", "rank"]


class ActivityChartSerializer(serializers.Serializer):
    total_visitor = serializers.SerializerMethodField()
    about_views = serializers.SerializerMethodField()
    registration_views = serializers.SerializerMethodField()

    def get_total_visitor(self, obj):
        last_seven_days = []
        visitors_list = []
        for i in range(6, -1, -1):
            day = timezone.now() - timezone.timedelta(days=i)
            last_seven_days.append(day)
        for day in last_seven_days:
            visitors = TotalVisitor.objects.filter(created_at__date=day).aggregate(Sum("count"))["count__sum"] or 0
            visitors_list.append(visitors)
        return visitors_list

    def get_about_views(self, obj):
        last_seven_days = []
        visitors_list = []
        for i in range(6, -1, -1):
            day = timezone.now() - timezone.timedelta(days=i)
            last_seven_days.append(day)
        for day in last_seven_days:
            visitors = AboutViews.objects.filter(created_at__date=day).aggregate(Sum("count"))["count__sum"] or 0
            visitors_list.append(visitors)
        return visitors_list

    def get_registration_views(self, obj):
        last_seven_days = []
        visitors_list = []
        for i in range(6, -1, -1):
            day = timezone.now() - timezone.timedelta(days=i)
            last_seven_days.append(day)
        for day in last_seven_days:
            visitors = (
                RegistrationViews.objects.filter(created_at__date=day).aggregate(Sum("count"))["count__sum"] or 0
            )
            visitors_list.append(visitors)
        return visitors_list
