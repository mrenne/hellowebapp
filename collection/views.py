from django.shortcuts import render
from collection.models import Tool

# Create your views here.
def index(request):
    tools = Tool.objects.all()

    return render(request, 'index.html', {
       'tools': tools,
    })
def tool_detail(request, slug):
	tool = Tool.objects.get(slug=slug)
	return render(request, 'tools/tool_detail.html', {
       'tool': tool,
	})
