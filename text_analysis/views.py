# Create your views here.
from django.http import HttpResponse
import text_analysis.text_analysis as analysis


def text_analysis(request):
    if request.method == 'GET':
        text = request.GET.get('text')
        method = request.GET.get('method')

        print(method, text)
        if (text is not None) and (method is not None):
            if method == "google":
                value = analysis.get_text_sentiment_values(text)
            else:
                value = analysis.get_error_message("The method specified is not supported")
        else:
            value = analysis.get_error_message("'text' and 'method' were not passed in the argument")

        return HttpResponse(value, content_type="text/json")

