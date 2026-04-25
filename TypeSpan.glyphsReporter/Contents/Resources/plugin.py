# encoding: utf-8
import objc
from GlyphsApp.plugins import *
from c737cf261ebaba33c import *

class TypeSpan(ReporterPlugin):
    @objc.python_method
    def settings(self):
        self.menuName = t("plugin.menu_name")
        if not _f137681():
            return
        _f227446()
        self._record_times = {}
        self._v988e01 = {}
        self._prune_frame = 0
        self._f5f6fed()
        self._ff430bc()

    @objc.python_method
    def start(self):
        _fa6db93()

    @objc.python_method
    def _f5f6fed(self):
        _f7c34f0(self)

    @objc.python_method
    def _ff430bc(self):
        _fb7f04c(self)

    def _scd351e_(self, sender):
        _fbe39d0(sender, self)

    def _s5ae8f6_(self, sender):
        _ff302d1(sender)

    @objc.python_method
    def conditionalContextMenus(self):
        menu_items = _ff30a63(self)
        return _f125894(menu_items, self, t("plugin.menu.preferences"))

    def _s7ad28d_(self, sender):
        _fffd879(self, 'file_display', 'hide')

    def _sec4d70_(self, sender):
        _fffd879(self, 'file_display', 'today')

    def _sae6435_(self, sender):
        _fffd879(self, 'file_display', 'all')

    def _s598e5e_(self, sender):
        _fffd879(self, 'master_display', 'today')

    def _s9fbe09_(self, sender):
        _fffd879(self, 'master_display', 'all')

    def _s2e15a7_(self, sender):
        _fffd879(self, 'master_display', 'hide')

    def _sb400dd_(self, sender):
        _fffd879(self, 'glyph_display', 'this_master_today')

    def _s7802f9_(self, sender):
        _fffd879(self, 'glyph_display', 'this_master_all_time')

    def _sa0091a_(self, sender):
        _fffd879(self, 'glyph_display', 'all_masters_today')

    def _se03341_(self, sender):
        _fffd879(self, 'glyph_display', 'all_masters_all_time')

    def _seddd19_(self, sender):
        _fffd879(self, 'glyph_display', 'hide')

    def _s2a8406_(self, sender):
        _fffd879(self, 'position', 'upperLeft')

    def _s2be444_(self, sender):
        _fffd879(self, 'position', 'upperCenter')

    def _s8e3926_(self, sender):
        _fffd879(self, 'position', 'upperRight')

    def _s85f732_(self, sender):
        _fffd879(self, 'position', 'lowerLeft')

    def _s29f8e4_(self, sender):
        _fffd879(self, 'position', 'lowerRight')

    def _s966abb_(self, sender):
        _fffd879(self, 'position', 'hide_all')

    def _s4d66d2_(self, sender):
        _fd4d405(self)

    def _s61a1d3_(self, sender):
        _ff40152(self)

    @objc.python_method
    def _f0e0fc6(self, key):
        if key not in self._v988e01:
            self._v988e01[key] = _f0e0fc6(key)
        return self._v988e01[key]

    @objc.python_method
    def _f8f11c7(self, key, value):
        _f8f11c7(key, value)
        self._v988e01[key] = value

    @objc.python_method
    def foregroundInViewCoords(self):
        _f7f008b(self, self._record_times)
        _f235a70(self, Glyphs.fonts)

    @objc.python_method
    def __file__(self):
        return __file__
