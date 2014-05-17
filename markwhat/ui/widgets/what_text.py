from Tkinter import Text
from markwhat.ui.widgets.mixin import ModifiedMixin


class WhatText(ModifiedMixin, Text):
    def __init__(self, *a, **b):
        Text.__init__(self, *a, **b)
        self._init()
