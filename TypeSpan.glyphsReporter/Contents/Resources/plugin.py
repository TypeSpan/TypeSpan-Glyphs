# encoding: utf-8
import objc
from GlyphsApp.plugins import *
from c6869cdc63313ba43 import *

class TypeSpan(ReporterPlugin):
    @objc.python_method
    def settings(self):
        self.menuName = t("plugin.menu_name")
        if not _f36c34e():
            return
        _f752de5()
        self._record_times = {}
        self._v755a0e = {}
        self._prune_frame = 0
        self._f4df2cb()
        self._f5fdb1f()

    @objc.python_method
    def start(self):
        _f5db011()

    @objc.python_method
    def _f4df2cb(self):
        _ff8c485(self)

    @objc.python_method
    def _f5fdb1f(self):
        _faff820(self)

    def _s897890_(self, sender):
        _f11df34(sender, self)

    def _s7c85da_(self, sender):
        _fc71b2f(sender)

    @objc.python_method
    def conditionalContextMenus(self):
        dot_indicator = _f9cfc70(__file__)
        menu_items = _fdbd51e(self, dot_indicator)
        return _f26a441(menu_items, self, t("window.menu_item"))

    def _sf685ba_(self, sender):
        _f2f8840(self, 'file_display', 'hide')

    def _sf105fb_(self, sender):
        _f2f8840(self, 'file_display', 'today')

    def _s046781_(self, sender):
        _f2f8840(self, 'file_display', 'all')

    def _sf11860_(self, sender):
        _f2f8840(self, 'master_display', 'today')

    def _s0a9430_(self, sender):
        _f2f8840(self, 'master_display', 'all')

    def _s6f37aa_(self, sender):
        _f2f8840(self, 'master_display', 'hide')

    def _s980f2d_(self, sender):
        _f2f8840(self, 'glyph_display', 'this_master_today')

    def _s6b2f61_(self, sender):
        _f2f8840(self, 'glyph_display', 'this_master_all_time')

    def _se79e2e_(self, sender):
        _f2f8840(self, 'glyph_display', 'all_masters_today')

    def _s7a8752_(self, sender):
        _f2f8840(self, 'glyph_display', 'all_masters_all_time')

    def _s20d56d_(self, sender):
        _f2f8840(self, 'glyph_display', 'hide')

    def _s49f286_(self, sender):
        _f2f8840(self, 'position', 'upperLeft')

    def _s5f7808_(self, sender):
        _f2f8840(self, 'position', 'upperCenter')

    def _sdc70f5_(self, sender):
        _f2f8840(self, 'position', 'upperRight')

    def _sacd821_(self, sender):
        _f2f8840(self, 'position', 'lowerLeft')

    def _s1c8b85_(self, sender):
        _f2f8840(self, 'position', 'lowerRight')

    def _s0de76e_(self, sender):
        _f2f8840(self, 'position', 'hide_all')

    def _s6cb5b3_(self, sender):
        _f115403(self)

    def _s4b155c_(self, sender):
        _f1c1527(self)

    @objc.python_method
    def _f291295(self, key):
        if key not in self._v755a0e:
            self._v755a0e[key] = _f291295(key)
        return self._v755a0e[key]

    @objc.python_method
    def _f8cce9a(self, key, value):
        _f8cce9a(key, value)
        self._v755a0e[key] = value

    @objc.python_method
    def foregroundInViewCoords(self):
        _f6268fb(self, self._record_times)
        _f77e999(self, Glyphs.fonts)

    @objc.python_method
    def __file__(self):
        return __file__
