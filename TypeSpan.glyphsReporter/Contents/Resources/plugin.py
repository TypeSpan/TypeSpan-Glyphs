# encoding: utf-8
import objc
from GlyphsApp.plugins import *
from c2153a8d6c64e0098 import *

class TypeSpan(ReporterPlugin):
    @objc.python_method
    def settings(self):
        self.menuName = t("plugin.menu_name")
        self._version_ok = _fed2075()
        if not self._version_ok:
            return
        _f0de59b()
        self._record_times = {}
        self._prune_frame = 0
        self._f263693()
        self._fa56b6f()

    @objc.python_method
    def start(self):
        if not getattr(self, '_version_ok', False):
            return
        _f9dad0a()
        _f02cbbb(lambda timer: _f496780())
        _f3adbfe()
        _fefb91b()

    @objc.python_method
    def _f263693(self):
        _f0335a4(self)

    @objc.python_method
    def _fa56b6f(self):
        _f90b5f5(self)

    def _s6b9b07_(self, sender):
        _f1940f6(sender, self)

    def _s36a055_(self, sender):
        _f93b41f(sender)

    @objc.python_method
    def conditionalContextMenus(self):
        menu_items = _f6d3d03(self)
        return _f962094(menu_items, self, t("plugin.menu.preferences"))

    def _s63b787_(self, sender):
        _f160c38(self, 'file_display', 'hide')

    def _s58989e_(self, sender):
        _f160c38(self, 'file_display', 'today')

    def _sc7d9d0_(self, sender):
        _f160c38(self, 'file_display', 'all')

    def _se38bd1_(self, sender):
        _f160c38(self, 'master_display', 'today')

    def _se2fef0_(self, sender):
        _f160c38(self, 'master_display', 'all')

    def _s6a4d59_(self, sender):
        _f160c38(self, 'master_display', 'hide')

    def _s2bc7c6_(self, sender):
        _f160c38(self, 'glyph_display', 'this_master_today')

    def _s96ea24_(self, sender):
        _f160c38(self, 'glyph_display', 'this_master_all_time')

    def _s1ac89f_(self, sender):
        _f160c38(self, 'glyph_display', 'all_masters_today')

    def _sa601f7_(self, sender):
        _f160c38(self, 'glyph_display', 'all_masters_all_time')

    def _s7e2610_(self, sender):
        _f160c38(self, 'glyph_display', 'hide')

    def _s208a8f_(self, sender):
        _f160c38(self, 'position', 'upperLeft')

    def _se94029_(self, sender):
        _f160c38(self, 'position', 'upperCenter')

    def _s4e4e95_(self, sender):
        _f160c38(self, 'position', 'upperRight')

    def _s03ca97_(self, sender):
        _f160c38(self, 'position', 'lowerLeft')

    def _s924ded_(self, sender):
        _f160c38(self, 'position', 'lowerRight')

    def _s7d0b40_(self, sender):
        _f160c38(self, 'position', 'hide_all')

    def _s484256_(self, sender):
        _fb502a2(self)

    def _s422fba_(self, sender):
        _f8cd760(self)

    @objc.python_method
    def _f489081(self, key):
        return _f489081(key)

    @objc.python_method
    def _f1e4128(self, key, value):
        _f1e4128(key, value)

    @objc.python_method
    def foregroundInViewCoords(self):
        _f054101(self, self._record_times)
        _f305b72(self, Glyphs.fonts)

    @objc.python_method
    def __file__(self):
        return __file__
