from rest_framework.permissions import BasePermission


class IsStudent(BasePermission):
    '''
    Allows access only to users who are students.
    '''
    def has_permission(self, request, view):
        
        return bool(request.user.is_authenticated and request.user.is_student())

class IsProfessor(BasePermission):
    '''
    Allows access only to users who are professors.
    '''
    def has_permission(self, request, view):
        
        return bool(request.user.is_authenticated and request.user.is_professor())