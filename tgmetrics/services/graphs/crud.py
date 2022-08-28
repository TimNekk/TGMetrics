import plotly.express as px
from plotly.graph_objs import Figure
from pandas import DataFrame

from tgmetrics.repositories import UserRepository


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def get_users_total(user_repository: UserRepository) -> Figure:
    title, x_axis, y_axis = "Всего пользователей", "Дата", "Количество"
    data_frame = DataFrame.from_records(user_repository.get_count_by_month(),
                                        columns=[y_axis, x_axis])
    return px.bar(data_frame, x=x_axis, y=y_axis, title=title)
