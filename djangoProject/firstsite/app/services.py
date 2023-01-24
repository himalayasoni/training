from app.models import App
from baseService import BaseService
# class Get_message_service(BaseService):
#     @staticmethod
#     def getData():
#         try:
#           dataset=App.objects.all()
#           dictset=BaseService.get_200_response(data=dataset)
#           return dictset
#         except:
#           dictset=BaseService.get_503_response()
#           return dictset 

    # @staticmethod
    # def delData(name):
    #    App.objects.filter(name=name).delete()

    # @staticmethod
    # def createData(data):
    #    App.objects.create(name=data['name'],email=data['email'],phone=data['phone'],desc=data['desc'],message=data['message'])
    #    return BaseService.get_200_response(data=data)
