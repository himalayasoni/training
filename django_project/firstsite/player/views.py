from django.shortcuts import render, HttpResponse
from player.models import Player
from django.db.models import Q
from django.db.models import Subquery, F, Count, Avg, Min, Max, Sum

# Create your views here.


def PlayerDataView(request, *args, **kwargs):
    # to find query associated with a queryset.

    queryset = Player.objects.all()
    # will print sql query
    print(queryset.query)
    # use filter to filter out the results.
    queryset_filter = Player.objects.filter(average__gt=40)
    print(queryset)

    # run 2 queries at a time (OR operation).
    name_filter = Player.objects.filter(
        fname__startswith='R') | Player.objects.filter(lname__startswith='S')
    # run 2 queries at a time using Q. (OR operation)
    name_filter_Q = Player.objects.filter(
        Q(fname__startswith='R') | Q(lname__startswith='S'))

    # run 2 queries at a time (AND operation).
    # 3 ways
    query1 = Player.objects.filter(
        fname__startswith='R') & Player.objects.filter(lname__startswith='S')
    query2 = Player.objects.filter(
        fname__startswith='R', lname__startswith='S')
    query3 = Player.objects.filter(
        Q(fname__startswith='R') & Q(lname__startswith='R'))

    # NOT query
    query_exclude = Player.objects.all().exclude(average__lt=40)
    query_Q = Player.objects.filter(~Q(average__lt=40))

    # UNION operation
    q1 = Player.objects.filter(id__gt=5)
    q2 = Player.objects.filter(id__lt=8)
    q1.union(q2)  # q2.union(q1)

    # Values, value_list and only method.
    # values-give a dictionary, values_list give a list, only also fetches the id.
    query_values = Player.objects.filter(
        fname__startswith='R').values('fname', 'lname', 'average')
    query_values_list = Player.objects.filter(
        fname__startswith='R').values_list('fname', 'lname', 'average')
    query_only = Player.objects.filter(
        fname__startswith='R').only('fname', 'lname', 'average')

    # subqueries
    highest_avg_query = Player.objects.filter(
        team__startswith='I').order_by("-average")
    Player.objects.all().annotate(highest_average=Subquery(
        highest_avg_query.values('fname', 'lname')[:1]))

    # filter comparing field values.
    Player.objects.filter(fname=F("lname"))

    # To find nth record.
    second_highest_average_player = Player.objects.order_by("-average")[1]

    # find duplicates
    duplicates = Player.objects.values("fname", "lname").annotate(
        name_count=Count("fname")).filter(name_count__gt=1)

    # find distinct fields.
    distinct = Player.objects.values("fname", "lname").annotate(
        name_count=Count("fname")).filter(name_count=1)
    records = Player.objects.filter(
        fname__in=[item["fname"] for item in distinct])

    # aggregate functions. (Max, Min, Sum, Count, Avg)
    avg_of_players = Player.objects.all().aggregate(Avg('average'))
    max_avg_of_players = Player.objects.all().aggregate(Max('average'))
    min_avg_of_players = Player.objects.all().aggregate(Min('average'))

    # select a random object from a model.
    random_object = Player.objects.order_by("?").first()

    return HttpResponse("Successful")
