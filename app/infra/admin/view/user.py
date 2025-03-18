from sqladmin import ModelView
from user.store.entity.user import User


class UserAdminView(ModelView, model=User):
    column_list = [User.username, User.uuid]
    column_details_exclude_list = [User.password]

    can_create = False
    can_export = False
