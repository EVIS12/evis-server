import json

from django.db.models import Sum
from django.utils import timezone
from rest_framework import serializers

from evis.blog.models import Blog
from evis.dashboard.models import ExhibitionViews, HomeViews, Region, RegistrationViews
from evis.users.models import RegisterLink


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["id", "name", "code", "registered_count"]
        read_only_fields = ["id", "registered_count"]


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["id", "name", "registered_count"]
        read_only_fields = ["id", "name", "registered_count"]


class RegionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["code"]

    def create(self, validated_data):
        code = validated_data["code"]
        with open("evis/dashboard/analysis/countries.json") as f:
            countries = json.load(f)
        matched_country = next((country for country in countries if country["code"] == code), None)
        if matched_country:
            region, _ = Region.objects.get_or_create(name=matched_country["name"], code=matched_country["code"])
            region.increment_registered_count()
            return region
        else:
            return None


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "title", "photo", "view_count"]
        read_only_fields = ("id", "created_at", "updated_at")


class HomeViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeViews
        fields = ["count"]

    def create(self, validated_data):
        count = validated_data["count"]
        home_views, _ = HomeViews.objects.get_or_create()
        home_views.increment_count(count)
        return home_views


class ExhibitionViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExhibitionViews
        fields = ["count"]
        read_only_fields = ("id",)

    def create(self, validated_data):
        count = validated_data["count"]
        exhibition_views, _ = ExhibitionViews.objects.get_or_create()
        exhibition_views.increment_count(count)
        return exhibition_views


class RegistrationViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationViews
        fields = ["count"]
        read_only_fields = ("id",)

    def create(self, validated_data):
        count = validated_data["count"]
        registration_views, _ = RegistrationViews.objects.get_or_create()
        registration_views.increment_count(count)
        return registration_views


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
            visitors = HomeViews.objects.filter(created_at__date=day).aggregate(Sum("count"))["count__sum"] or 0
            visitors_list.append(visitors)
        return visitors_list

    def get_about_views(self, obj):
        last_seven_days = []
        visitors_list = []
        for i in range(6, -1, -1):
            day = timezone.now() - timezone.timedelta(days=i)
            last_seven_days.append(day)
        for day in last_seven_days:
            visitors = ExhibitionViews.objects.filter(created_at__date=day).aggregate(Sum("count"))["count__sum"] or 0
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
