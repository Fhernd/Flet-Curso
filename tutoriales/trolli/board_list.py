from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from board import Board

import itertools
from flet import (
    alignment,
    border,
    border_radius,
    colors,
    icons,
    padding,
    Column,
    Container,
    Draggable,
    DragTarget,
    Icon,
    PopupMenuButton,
    PopupMenuItem,
    Text,
    TextButton,
    TextField,
    UserControl
)


