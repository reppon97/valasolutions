import json

from django.http import JsonResponse

from users.models import Person, Company


def create_user(request):
    """
    Creates a person if request method is POST
    Otherwise return all person as JSON
    :param request:
    :return:
    """
    if request.method == "POST":
        data = json.loads(request.body)
        company = Company.objects.get(pk=data['company'])
        person = Person(
            first_name=data['first_name'],
            last_name=data['last_name'],
            company=company
        )
        person.save()

        return JsonResponse({"message": "201 CREATED"})

    data = list(Person.objects.values())  # wrap in list(), because QuerySet is not JSON serializable
    return JsonResponse(data, safe=False)


def create_company(request):
    """
    Creates a company if request method is POST
    Otherwise return all persons working in certain company (expects company id as a request GET parameter)
    :param request:
    :return:
    """
    if request.method == "POST":
        data = json.loads(request.body)
        company = Company(name=data['name'])
        company.save()

        return JsonResponse({"message": "201 CREATED"})

    persons = Person.objects.filter(company_id=request.GET.get("id", None))
    data = list(persons.values())

    return JsonResponse(data, safe=False)
