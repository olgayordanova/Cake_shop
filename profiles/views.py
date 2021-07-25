from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from profiles.forms import ProfileForm
from profiles.models import Profile


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profiles/details.html', context)