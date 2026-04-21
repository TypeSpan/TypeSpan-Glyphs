# encoding: utf-8
import objc
from GlyphsApp.plugins import *
from cf5e2228563da9044 import *

class TypeSpan(ReporterPlugin):
    @objc.python_method
    def settings(self):
        self.menuName = t("plugin.menu_name")
        if not _f3d6b90():
            return
        _f54baf6()
        self._record_times = {}
        self._v27ccfa = {}
        self._prune_frame = 0
        self._fc4b69b()
        self._fc2f8ec()

    @objc.python_method
    def start(self):
        _fb419e2()

    @objc.python_method
    def _fc4b69b(self):
        _f758b52(self)

    @objc.python_method
    def _fc2f8ec(self):
        _fbe85c6(self)

    def _sc644df_(self, sender):
        _f6e1494(sender, self)

    def _s5abd4b_(self, sender):
        _f608c9e(sender)

    @objc.python_method
    def conditionalContextMenus(self):
        dot_indicator = _f4810c0(__file__)
        menu_items = _fe4fbb2(self, dot_indicator)
        return _fe3d9bf(menu_items, self, t("window.menu_item"))

    def _sdaf60b_(self, sender):
        _f5b682a(self)

    def _s8ae60a_(self, sender):
        _fecaf5f(self)

    def _s52a7ac_(self, sender):
        _f6c0668(self)

    def _s6eb4cd_(self, sender):
        _fe2b4ee(self)

    def _s7adc2c_(self, sender):
        _fb5109d(self)

    def _s7db1a1_(self, sender):
        _faa6a10(self)

    def _sc68d7a_(self, sender):
        _fb10faa(self)

    def _sec2db2_(self, sender):
        _f277276(self)

    def _s67d7c3_(self, sender):
        _f897f4a(self)

    def _sde3b1f_(self, sender):
        _fd4b03f(self)

    def _s896c6d_(self, sender):
        _f637e94(self)

    def _s6d8d2a_(self, sender):
        _f731105(self)

    def _s0a8247_(self, sender):
        _fa023d3(self)

    def _s24a18c_(self, sender):
        _f87f618(self)

    def _s04c578_(self, sender):
        _f1d94db(self)

    def _seeb0b6_(self, sender):
        _f2a5661(self)

    def _scf8be8_(self, sender):
        _f5313c6(self)

    def _s4f7389_(self, sender):
        _fcdce3a(self)

    def _sd7940a_(self, sender):
        _f9ed69b(self)

    @objc.python_method
    def _f7fba53(self, key):
        if key not in self._v27ccfa:
            self._v27ccfa[key] = _f7fba53(key)
        return self._v27ccfa[key]

    @objc.python_method
    def _f92f8f4(self, key, value):
        _f92f8f4(key, value)
        self._v27ccfa[key] = value

    @objc.python_method
    def foregroundInViewCoords(self):
        _ffc099b(self, self._record_times)
        _f0800d2(self, Glyphs.fonts)

    @objc.python_method
    def __file__(self):
        return __file__
