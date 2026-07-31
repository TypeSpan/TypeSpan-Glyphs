# encoding: utf-8
import objc
from GlyphsApp.plugins import *
from c4c53fff7fe62f4b5 import *

class TypeSpan(ReporterPlugin):
    @objc.python_method
    def settings(self):
        self.menuName = t("plugin.menu_name")
        self._version_ok = _f913605()
        if not self._version_ok:
            return
        _f0c8c27()
        self._record_times = {}
        self._va0ff07 = {}
        self._prune_frame = 0
        self._f7b40c3()
        self._feef624()

    @objc.python_method
    def start(self):
        if not getattr(self, '_version_ok', False):
            return
        _f067056()
        _f9cd204()

    @objc.python_method
    def _f7b40c3(self):
        _fc63d44(self)

    @objc.python_method
    def _feef624(self):
        _f0a0bf0(self)

    def _s9457b4_(self, sender):
        _fc17f14(sender, self)

    def _sf7cbcc_(self, sender):
        _f1fc32e(sender)

    @objc.python_method
    def conditionalContextMenus(self):
        menu_items = _ff5f90d(self)
        return _fc4456e(menu_items, self, t("plugin.menu.preferences"))

    def _sc94ded_(self, sender):
        _f67478d(self, 'file_display', 'hide')

    def _s92de91_(self, sender):
        _f67478d(self, 'file_display', 'today')

    def _sba3fd7_(self, sender):
        _f67478d(self, 'file_display', 'all')

    def _s46d649_(self, sender):
        _f67478d(self, 'master_display', 'today')

    def _s30c6be_(self, sender):
        _f67478d(self, 'master_display', 'all')

    def _s492db2_(self, sender):
        _f67478d(self, 'master_display', 'hide')

    def _s071c97_(self, sender):
        _f67478d(self, 'glyph_display', 'this_master_today')

    def _sea83c2_(self, sender):
        _f67478d(self, 'glyph_display', 'this_master_all_time')

    def _s79f229_(self, sender):
        _f67478d(self, 'glyph_display', 'all_masters_today')

    def _s75c2e0_(self, sender):
        _f67478d(self, 'glyph_display', 'all_masters_all_time')

    def _s7cae1a_(self, sender):
        _f67478d(self, 'glyph_display', 'hide')

    def _se7f0d2_(self, sender):
        _f67478d(self, 'position', 'upperLeft')

    def _s9c50e3_(self, sender):
        _f67478d(self, 'position', 'upperCenter')

    def _s039320_(self, sender):
        _f67478d(self, 'position', 'upperRight')

    def _s7b2a21_(self, sender):
        _f67478d(self, 'position', 'lowerLeft')

    def _s86517f_(self, sender):
        _f67478d(self, 'position', 'lowerRight')

    def _s980828_(self, sender):
        _f67478d(self, 'position', 'hide_all')

    def _sd8fd6d_(self, sender):
        _f8d2333(self)

    def _sfde636_(self, sender):
        _f25e5dc(self)

    @objc.python_method
    def _f93a573(self, key):
        if key not in self._va0ff07:
            self._va0ff07[key] = _f93a573(key)
        return self._va0ff07[key]

    @objc.python_method
    def _f606aa6(self, key, value):
        _f606aa6(key, value)
        self._va0ff07[key] = value

    @objc.python_method
    def foregroundInViewCoords(self):
        _fef688d(self, self._record_times)
        _faa9fa9(self, Glyphs.fonts)

    @objc.python_method
    def __file__(self):
        return __file__
