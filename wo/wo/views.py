from django.http import HttpResponse

def article_list(request):
	return HttpResponse("Worked from another server? Congoo")
