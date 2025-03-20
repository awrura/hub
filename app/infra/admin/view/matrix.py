from matrix.store.entity.matrix import Matrix
from sqladmin import ModelView


class MatrixAdminView(ModelView, model=Matrix):
    column_list = [Matrix.name, Matrix.uuid]
    column_searchable_list = [Matrix.name, Matrix.uuid]

    can_export = False
