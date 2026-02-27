"""
Price Lists & Rules Module Views
"""
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404, render as django_render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST

from apps.accounts.decorators import login_required, permission_required
from apps.core.htmx import htmx_view
from apps.core.services import export_to_csv, export_to_excel
from apps.modules_runtime.navigation import with_module_nav

from .models import PriceList, PriceRule

PER_PAGE_CHOICES = [10, 25, 50, 100]


# ======================================================================
# Dashboard
# ======================================================================

@login_required
@with_module_nav('pricing', 'dashboard')
@htmx_view('pricing/pages/index.html', 'pricing/partials/dashboard_content.html')
def dashboard(request):
    hub_id = request.session.get('hub_id')
    return {
        'total_price_lists': PriceList.objects.filter(hub_id=hub_id, is_deleted=False).count(),
    }


# ======================================================================
# PriceList
# ======================================================================

PRICE_LIST_SORT_FIELDS = {
    'code': 'code',
    'name': 'name',
    'is_active': 'is_active',
    'currency': 'currency',
    'start_date': 'start_date',
    'end_date': 'end_date',
    'created_at': 'created_at',
}

def _build_price_lists_context(hub_id, per_page=10):
    qs = PriceList.objects.filter(hub_id=hub_id, is_deleted=False).order_by('code')
    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(1)
    return {
        'price_lists': page_obj,
        'page_obj': page_obj,
        'search_query': '',
        'sort_field': 'code',
        'sort_dir': 'asc',
        'current_view': 'table',
        'per_page': per_page,
    }

def _render_price_lists_list(request, hub_id, per_page=10):
    ctx = _build_price_lists_context(hub_id, per_page)
    return django_render(request, 'pricing/partials/price_lists_list.html', ctx)

@login_required
@with_module_nav('pricing', 'pricelists')
@htmx_view('pricing/pages/price_lists.html', 'pricing/partials/price_lists_content.html')
def price_lists_list(request):
    hub_id = request.session.get('hub_id')
    search_query = request.GET.get('q', '').strip()
    sort_field = request.GET.get('sort', 'code')
    sort_dir = request.GET.get('dir', 'asc')
    page_number = request.GET.get('page', 1)
    current_view = request.GET.get('view', 'table')
    per_page = int(request.GET.get('per_page', 10))
    if per_page not in PER_PAGE_CHOICES:
        per_page = 10

    qs = PriceList.objects.filter(hub_id=hub_id, is_deleted=False)

    if search_query:
        qs = qs.filter(Q(name__icontains=search_query) | Q(code__icontains=search_query) | Q(currency__icontains=search_query))

    order_by = PRICE_LIST_SORT_FIELDS.get(sort_field, 'code')
    if sort_dir == 'desc':
        order_by = f'-{order_by}'
    qs = qs.order_by(order_by)

    export_format = request.GET.get('export')
    if export_format in ('csv', 'excel'):
        fields = ['code', 'name', 'is_active', 'currency', 'start_date', 'end_date']
        headers = ['Code', 'Name', 'Is Active', 'Currency', 'Start Date', 'End Date']
        if export_format == 'csv':
            return export_to_csv(qs, fields=fields, headers=headers, filename='price_lists.csv')
        return export_to_excel(qs, fields=fields, headers=headers, filename='price_lists.xlsx')

    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(page_number)

    if request.htmx and request.htmx.target == 'datatable-body':
        return django_render(request, 'pricing/partials/price_lists_list.html', {
            'price_lists': page_obj, 'page_obj': page_obj,
            'search_query': search_query, 'sort_field': sort_field,
            'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
        })

    return {
        'price_lists': page_obj, 'page_obj': page_obj,
        'search_query': search_query, 'sort_field': sort_field,
        'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
    }

@login_required
def price_list_add(request):
    hub_id = request.session.get('hub_id')
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        code = request.POST.get('code', '').strip()
        currency = request.POST.get('currency', '').strip()
        is_active = request.POST.get('is_active') == 'on'
        start_date = request.POST.get('start_date') or None
        end_date = request.POST.get('end_date') or None
        obj = PriceList(hub_id=hub_id)
        obj.name = name
        obj.code = code
        obj.currency = currency
        obj.is_active = is_active
        obj.start_date = start_date
        obj.end_date = end_date
        obj.save()
        return _render_price_lists_list(request, hub_id)
    return django_render(request, 'pricing/partials/panel_price_list_add.html', {})

@login_required
def price_list_edit(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(PriceList, pk=pk, hub_id=hub_id, is_deleted=False)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '').strip()
        obj.code = request.POST.get('code', '').strip()
        obj.currency = request.POST.get('currency', '').strip()
        obj.is_active = request.POST.get('is_active') == 'on'
        obj.start_date = request.POST.get('start_date') or None
        obj.end_date = request.POST.get('end_date') or None
        obj.save()
        return _render_price_lists_list(request, hub_id)
    return django_render(request, 'pricing/partials/panel_price_list_edit.html', {'obj': obj})

@login_required
@require_POST
def price_list_delete(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(PriceList, pk=pk, hub_id=hub_id, is_deleted=False)
    obj.is_deleted = True
    obj.deleted_at = timezone.now()
    obj.save(update_fields=['is_deleted', 'deleted_at', 'updated_at'])
    return _render_price_lists_list(request, hub_id)

@login_required
@require_POST
def price_list_toggle_status(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(PriceList, pk=pk, hub_id=hub_id, is_deleted=False)
    obj.is_active = not obj.is_active
    obj.save(update_fields=['is_active', 'updated_at'])
    return _render_price_lists_list(request, hub_id)

@login_required
@require_POST
def price_lists_bulk_action(request):
    hub_id = request.session.get('hub_id')
    ids = [i.strip() for i in request.POST.get('ids', '').split(',') if i.strip()]
    action = request.POST.get('action', '')
    qs = PriceList.objects.filter(hub_id=hub_id, is_deleted=False, id__in=ids)
    if action == 'activate':
        qs.update(is_active=True)
    elif action == 'deactivate':
        qs.update(is_active=False)
    elif action == 'delete':
        qs.update(is_deleted=True, deleted_at=timezone.now())
    return _render_price_lists_list(request, hub_id)


@login_required
@permission_required('pricing.manage_settings')
@with_module_nav('pricing', 'settings')
@htmx_view('pricing/pages/settings.html', 'pricing/partials/settings_content.html')
def settings_view(request):
    return {}

