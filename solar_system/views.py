from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import FileResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.generic import CreateView

# Let the desktop preview frame the Study Hub; Science pages remain same-origin only.
@xframe_options_exempt
def home(request):
    """Show the Study Hub's subject cards."""
    subjects = [
        {
            'name': 'Science',
            'description': 'Explore the solar system and start learning about space.',
            'url_name': 'solar_system:science',
            'button_label': 'Science Study',
        },
    ]
    return render(request, 'solar_system/home.html', {'subjects': subjects})


def science(request):
    """Show the Science Study page with the existing solar system explorer."""
    return render(request, 'solar_system/science.html')


def playground(request):
    """Serve the original standalone page without changing or copying it."""
    page = settings.BASE_DIR / 'solar_system.html'
    return FileResponse(page.open('rb'), content_type='text/html; charset=utf-8')


class SignUpView(CreateView):
    """Create a student account with Django's built-in user form."""
    form_class = UserCreationForm
    template_name = 'solar_system/signup.html'
    success_url = reverse_lazy('solar_system:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
