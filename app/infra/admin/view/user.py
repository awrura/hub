from sqladmin import ModelView
from user.store.entity.user import User


class UserAdminView(ModelView, model=User):
    column_list = [User.username, User.uuid]
    column_details_exclude_list = [User.password]
    column_searchable_list = [User.username, User.uuid]

    can_create = False
    can_export = False
