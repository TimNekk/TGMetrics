import plotly.express as px
from plotly.graph_objs import Figure
from pandas import DataFrame

from tgmetrics.repositories import UserRepository
from tgmetrics.repositories.group_by import GroupBy

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def get_users_total(user_repository: UserRepository, group_by: GroupBy) -> Figure:
    hour, day, month, year, y_axis = "Час", "День", "Месяц", "Год", "Количество"
    x_axis, animation_frame, max_x = None, None, None

    match group_by:
        case GroupBy.MONTH:
            x_axis, animation_frame, max_x = month, year, 12
        case GroupBy.DAY:
            x_axis, animation_frame, max_x = day, month, 31
        case GroupBy.HOUR:
            x_axis, animation_frame, max_x = hour, day, 24

    title = f"Всего пользователей за {animation_frame}"

    data_frame = DataFrame.from_records(user_repository.get_count_query(group_by),
                                        columns=[y_axis, x_axis, animation_frame])

    figure = px.bar(data_frame, x=x_axis, y=y_axis,
                    title=title, animation_frame=animation_frame,
                    range_x=[-1, max_x], range_y=[0, data_frame[y_axis].max()])

    return figure
