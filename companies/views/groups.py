from .base import Base
from ..utils.exceptions import RequiredFields
from ..utils.permissions import GroupPermission
from ..serializers import GroupsSerializer

from accounts.models import Group, GroupPermissons

from rest_framework.views import Response
from rest_framework.exceptions import APIException

from django.contrib.auth.models import Permission


class Groups(Base):
    permission_classes = [GroupPermission]

    def get(self, request):
        enterprise_id = self.get_enterprise_id(request.user.id)

        groups = Group.objects.filter(enterprise_id=enterprise_id).all()

        serializer = GroupsSerializer(groups, many=True)

        return Response({
            "groups": serializer.data
        })
    
    
    def post(self, request):
        enterprise_id = self.get_enterprise_id(request.user.id)
        
        name = request.data.get('name')
        permissions = request.data.get('permissions')

        if not name:
            raise RequiredFields
        
        group_created = Group.objects.create(
            name=name,
            enterprise_id=enterprise_id,
        )

        if permissions:

            permissions = permissions.split(',')
            
            try:
                for item in permissions:
                    permission = Permission.objects.filter(id=item).exists()

                    if not permission:
                        group_created.delete()
                        raise APIException("This {p} permission is invalid".format(p=item))
                    
                    if not GroupPermissons.objects.filter(group_id=group_created.id, permission_id=item).exists():
                        GroupPermissons.objects.create(
                            group_id=group_created.id,
                            permission_id=item
                        )
            except ValueError:
                group_created.delete()
                raise APIException("Send permissions in correct patterns")
            
        return Response({"success": True})
    

class GroupDetail(Base):
    permission_classes = [GroupPermission]

    def get(self, request, group_id):
        enterprise_id = self.get_enterprise_id(request.user.id)  

        self.get_group(group_id, enterprise_id)

        group = Group.objects.filter(id=group_id).first()

        serializer = GroupsSerializer(group)

        return Response({
            "group": serializer.data
        })
    
    def put(self, request, group_id):
        enterprise_id = self.get_enterprise_id(request.user.id)

        self.get_group(group_id, enterprise_id)
        name = request.data.get('name')
        permissions = request.data.get('permissions')

        if name:
            Group.objects.filter(id=group_id).update(
                name=name
            )

        GroupPermissons.objects.filter(group_id=group_id).delete()

        if permissions:
            try:
                    
                for item in permissions:
                    permission = Permission.objects.filter(id=item).exists()

                    if not permission:
                        
                        raise APIException("This {p} permission is invalid".format(p=item))
                    
                    if not GroupPermissons.objects.filter(group_id=group_id, permission_id=item).exists():
                        GroupPermissons.objects.create(
                            group_id=group_id,
                            permission_id=item
                        )
                    
                return Response({"success": True})

            except ValueError:
                
                raise APIException("Send permissions in correct patterns")


    def delete(self, request, group_id):

        enterprise_id = self.get_enterprise_id(enterprise_id=enterprise_id)

        Group.objects.filter(id=group_id, enterprise_id=enterprise_id).delete()

        return Response({"success": True}) 
    


