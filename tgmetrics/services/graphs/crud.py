import plotly.express as px
from plotly.graph_objs import Figure
from pandas import DataFrame

from tgmetrics.repositories import UserRepository
from tgmetrics.repositories.group_by import GroupBy

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def get_users_total(user_repository: UserRepository, group_by: GroupBy) -> Figure:
    title, x_axis, y_axis = "Всего пользователей", "Дата", "Количество"
    data_frame = DataFrame.from_records(user_repository.get_count(group_by),
                                        columns=[y_axis, x_axis])
    return px.bar(data_frame, x=x_axis, y=y_axis, title=title)
