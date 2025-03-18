from matrix.store.entity.user_matrix import UserMatrix
from sqladmin import ModelView


class UserMatrixAdminView(ModelView, model=UserMatrix):
    column_list = [UserMatrix.matrix_uuid, UserMatrix.user_uuid]
    column_details_list = [UserMatrix.matrix_uuid, UserMatrix.user_uuid]

    can_edit = False
    can_create = False
    can_export = False
