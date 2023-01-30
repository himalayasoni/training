from app.models import Player
from core.baseservice import BaseService


class service(BaseService):
    @staticmethod
    def object_creation(queryset):
        players = []
        for instance in queryset:
            data = {
                'fname': instance.fname,
                'lname': instance.lname,
                'team': instance.team,
                'role': instance.role,
                'batting_order': instance.batting_order
            }
            players.append(data)
        return players

    def get_data():
        players = Player.objects.all()
        emp_object = service.object_creation(players)
        data = BaseService.get_200_response(data=emp_object)
        return data

    def post_data(data):
        Player.objects.create(
            fname=data["fname"], lname=data["lname"], team=data['team'], role=data['role'], batting_order=data['batting_order'])
        return {"status": "Success"}

    def get_param_data(pk):
        player = Player.objects.filter(id=pk)
        emp_object = service.object_creation(player)
        data = BaseService.get_200_response(data=emp_object)
        return data

    def put_param_data(data, pk):
        player = Player.objects.filter(id=pk)
        player.update(fname=data["fname"], lname=data["lname"],
                      team=data["team"], role=data["role"], batting_order=data['batting_order'])
        data = BaseService.get_200_response(data=player)
        return data

    def delete_param_data(pk):
        player = Player.objects.filter(id=pk)
        player.delete()
        return ({"message": "deleted"})
