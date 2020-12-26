from django.shortcuts import render
from django.apps import apps
from django.utils import timezone
from django.db.models import Q

Story = apps.get_model('main', 'Story')


# Create your views here.


def home(request):
    return render(request, "main\\home.html")


def problems(request):
    problems = Story.objects.filter(story_type="P").order_by("-date_added")
    data = {
        'problems': problems
    }
    return render(request, 'stories\\problems.html', data)


def consequences(request):
    consequences = Story.objects.filter(story_type="C").order_by("-date_added")
    data = {
        'consequences': consequences
    }
    return render(request, 'stories\\consequences.html', data)


def opportunities(request):
    opportunities = Story.objects.filter(story_type="O").order_by("-date_added")
    data = {
        'opportunities': opportunities
    }
    return render(request, 'stories\\opportunitites.html', data)


def career_goals(request):
    goals = Story.objects.filter(story_type="CG").order_by("-date_added")
    data = {
        'goals': goals
    }
    return render(request, 'stories\\career-goals.html', data)


def get_by_id(request, id):
    story = Story.objects.get(id=id)
    data = {
        "story": story
    }
    return render(request, "each-story.html", data)


def write_stories(request):
    if request.method == "POST":
        story_type = request.POST["story_type"]
        title = request.POST["title"]
        subtitle = request.POST["subtitle"]
        content = request.POST["content"]
        date_added = timezone.now()

        data = {
            'title': title,
            'subtitle': subtitle,
            'content': content,
        }

        Story.objects.create(
            story_type=story_type,
            title=title,
            subtitle=subtitle,
            content=content,
            date_added=date_added
        )
        return render(request, "stories\\story-written.html", data)

    else:
        return render(request, "stories\\write-stories.html")


def how_to_write_stories(request):
    return render(request, 'stories\\how-to-write-stories.html')
