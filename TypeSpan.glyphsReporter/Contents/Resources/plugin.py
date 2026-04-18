# encoding: utf-8
import objc
from GlyphsApp.plugins import *
from c76f531ff2740d5cb import *

class TypeSpan(ReporterPlugin):
    @objc.python_method
    def settings(self):
        self.menuName = t("plugin.menu_name")
        if not _fc4ad8c():
            return
        _f314f66()
        self._record_times = {}
        self._v77c7ec = {}
        self._prune_frame = 0
        self._f836eed()
        self._ffd72c5()

    @objc.python_method
    def start(self):
        _f838534()

    @objc.python_method
    def _f836eed(self):
        _f5f6f8f(self)

    @objc.python_method
    def _ffd72c5(self):
        _fba667b(self)

    def _sf15e2f_(self, sender):
        _fbf2322(sender, self)

    def _s921a67_(self, sender):
        _f06b61f(sender)

    @objc.python_method
    def conditionalContextMenus(self):
        dot_indicator = _fb9df86(__file__)
        menu_items = _f54229a(self, dot_indicator)
        return _f8bdb1d(menu_items, self, t("window.menu_item"))

    def _s00d069_(self, sender):
        _fc6a5ec(self)

    def _sd3db67_(self, sender):
        _f1df2b2(self)

    def _saf4911_(self, sender):
        _fcfa6dc(self)

    def _s57f57b_(self, sender):
        _fc628f7(self)

    def _sa30953_(self, sender):
        _ff8b6d0(self)

    def _s4a3de6_(self, sender):
        _f7013fb(self)

    def _s180007_(self, sender):
        _f3293f8(self)

    def _sb570ec_(self, sender):
        _f66b177(self)

    def _s941238_(self, sender):
        _f3ff1ec(self)

    def _s532a63_(self, sender):
        _f6be315(self)

    def _s147e2b_(self, sender):
        _fc740b2(self)

    def _sa93965_(self, sender):
        _fd8e66c(self)

    def _s5f4a2b_(self, sender):
        _f3385c9(self)

    def _sd961be_(self, sender):
        _f5d09c9(self)

    def _s655fe5_(self, sender):
        _f55a6ff(self)

    def _sff0b09_(self, sender):
        _f79e394(self)

    def _sa8ec43_(self, sender):
        _f421bd2(self)

    def _sb5476b_(self, sender):
        _fd4860f(self)

    def _s4e65f6_(self, sender):
        _f3c1824(self)

    @objc.python_method
    def _f38b454(self, key):
        if key not in self._v77c7ec:
            self._v77c7ec[key] = _f38b454(key)
        return self._v77c7ec[key]

    @objc.python_method
    def _f4d76cc(self, key, value):
        _f4d76cc(key, value)
        self._v77c7ec[key] = value

    @objc.python_method
    def foregroundInViewCoords(self):
        _f7d93e8(self, self._record_times)
        _f43289c(self, Glyphs.fonts)

    @objc.python_method
    def __file__(self):
        return __file__
