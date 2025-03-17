from matrix.store.entity.matrix import Matrix
from sqladmin import ModelView


class MatrixAdminView(ModelView, model=Matrix):
    column_list = [Matrix.uuid, Matrix.name]
