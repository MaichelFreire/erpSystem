from rest_framework.exceptions import APIException


class NotFoundEmployee(APIException):
    status_code = 404
    default_detail = 'Employee not found'
    default_code = 'employee_not_found'


class NotFoundGroup(APIException):
    status_code = 404
    default_detail = 'Group not found'
    default_code = 'group_not_found'


class RequiredFields(APIException):
    status_code = 400
    default_detail = 'The fields patterns is incorrect'
    default_code = 'fields_error'


class NotFoundTaskStatus(APIException):
    status_code = 404
    default_detail = 'Task not found'
    default_code = 'task_not_found'
    

class NotFoundTask(APIException):
    status_code = 404
    default_detail = 'Task not found'
    default_code = 'task_not_found'