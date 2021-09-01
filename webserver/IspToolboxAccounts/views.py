from django.contrib.auth import login, authenticate
from django.urls.base import reverse
from django.views import View
from IspToolboxAccounts.forms import IspToolboxUserCreationForm
from IspToolboxAccounts.models import User, NewUserExperience
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.conf import settings
from django.utils.http import (
    url_has_allowed_host_and_scheme
)
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, JsonResponse
from workspace.mixnins import SuperuserRequiredMixin


class CreateAccountView(View):
    def post(self, request):
        form = IspToolboxUserCreationForm(request.POST)
        if form.is_valid() and (settings.ENABLE_ACCOUNT_CREATION or (
                form.cleaned_data.get(
                    'registration_code') == 'isptoolbox usability testing'
        )):
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user, backend=settings.AUTHENTICATION_BACKENDS[0])
            next_url = request.POST.get('next', request.GET.get('next', None))
            url_is_safe = url_has_allowed_host_and_scheme(
                url=next_url,
                allowed_hosts=self.request.get_host(),
                require_https=self.request.is_secure()
            )
            if next_url is not None and url_is_safe:
                return redirect(next_url)
            else:
                return redirect(reverse("optional_info"))
        return render(
            request,
            'workspace/pages/login_view.html',
            {
                'showSignUp': True,
                'showEmailSignUp': True,
                'authentication_form': AuthenticationForm,
                'sign_up_form': form,
            }
        )

    def get(self, request):
        return redirect("workspace_dashboard")


@method_decorator(csrf_exempt, name='dispatch')
class IntegrationTestAccountCreationView(View):
    def post(self, request):
        if settings.PROD:
            raise Http404
        else:
            if User.objects.filter(email="test-isp@fb.com").exists():
                User.objects.get(email="test-isp@fb.com").delete()
            if User.objects.filter(email="test-user-isp@fb.com").exists():
                User.objects.get(email="test-user-isp@fb.com").delete()
            login_user = User.objects.create_user(
                email="test-user-isp@fb.com",
                first_name="TestUser",
                last_name="ISPToolbox",
                password="zuuuuccccCCCC1"
            )
            login_user.save()
            return JsonResponse({'success': True})

    def get(self, request):
        raise Http404


class UpdateNuxSettingView(SuperuserRequiredMixin, View):
    def post(self, request):
        try:
            nux = NewUserExperience.objects.get(
                id=request.POST.get('nux')
            )
        except Exception:
            raise Http404
        if request.POST.get('seen'):
            nux.users.add(request.POST.get('user'))
        else:
            nux.users.remove(request.POST.get('user'))
        return redirect(request.POST.get('next'))
