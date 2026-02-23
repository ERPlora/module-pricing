"""
Price Lists & Rules Module Views
"""
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.modules_runtime.navigation import with_module_nav


@login_required
@with_module_nav('pricing', 'dashboard')
@htmx_view('pricing/pages/dashboard.html', 'pricing/partials/dashboard_content.html')
def dashboard(request):
    """Dashboard view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('pricing', 'pricelists')
@htmx_view('pricing/pages/pricelists.html', 'pricing/partials/pricelists_content.html')
def pricelists(request):
    """Price Lists view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('pricing', 'rules')
@htmx_view('pricing/pages/rules.html', 'pricing/partials/rules_content.html')
def rules(request):
    """Rules view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('pricing', 'settings')
@htmx_view('pricing/pages/settings.html', 'pricing/partials/settings_content.html')
def settings(request):
    """Settings view."""
    hub_id = request.session.get('hub_id')
    return {}

