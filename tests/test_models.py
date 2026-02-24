"""Tests for pricing models."""
import pytest
from django.utils import timezone

from pricing.models import PriceList


@pytest.mark.django_db
class TestPriceList:
    """PriceList model tests."""

    def test_create(self, price_list):
        """Test PriceList creation."""
        assert price_list.pk is not None
        assert price_list.is_deleted is False

    def test_str(self, price_list):
        """Test string representation."""
        assert str(price_list) is not None
        assert len(str(price_list)) > 0

    def test_soft_delete(self, price_list):
        """Test soft delete."""
        pk = price_list.pk
        price_list.is_deleted = True
        price_list.deleted_at = timezone.now()
        price_list.save()
        assert not PriceList.objects.filter(pk=pk).exists()
        assert PriceList.all_objects.filter(pk=pk).exists()

    def test_queryset_excludes_deleted(self, hub_id, price_list):
        """Test default queryset excludes deleted."""
        price_list.is_deleted = True
        price_list.deleted_at = timezone.now()
        price_list.save()
        assert PriceList.objects.filter(hub_id=hub_id).count() == 0

    def test_toggle_active(self, price_list):
        """Test toggling is_active."""
        original = price_list.is_active
        price_list.is_active = not original
        price_list.save()
        price_list.refresh_from_db()
        assert price_list.is_active != original


