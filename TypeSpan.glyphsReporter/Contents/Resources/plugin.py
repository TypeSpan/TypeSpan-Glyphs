# encoding: utf-8
import objc
from GlyphsApp.plugins import *
from c0618b96572807b9f import *

class TypeSpan(ReporterPlugin):
    @objc.python_method
    def settings(self):
        self.menuName = t("plugin.menu_name")
        if not _f6b67de():
            return
        _fe2ee48()
        self._record_times = {}
        self._v559d1e = {}
        self._prune_frame = 0
        self._f689fa2()
        self._f6219ab()

    @objc.python_method
    def start(self):
        _f9b5616()

    @objc.python_method
    def _f689fa2(self):
        _f9f9328(self)

    @objc.python_method
    def _f6219ab(self):
        _f9e82f5(self)

    def _se9772a_(self, sender):
        _f5c1566(sender, self)

    def _s2a13d5_(self, sender):
        _f265dcc(sender)

    @objc.python_method
    def conditionalContextMenus(self):
        dot_indicator = _f9ea8e7(__file__)
        menu_items = _fb471bf(self, dot_indicator)
        return _f18c907(menu_items, self, t("window.menu_item"))

    def _s4f75ec_(self, sender):
        _fb50531(self)

    def _s269054_(self, sender):
        _f945f15(self)

    def _s95cea2_(self, sender):
        _fad660b(self)

    def _s1f312c_(self, sender):
        _f660e9e(self)

    def _sa2c022_(self, sender):
        _f47a398(self)

    def _sea510c_(self, sender):
        _f5b39bf(self)

    def _sc97e33_(self, sender):
        _fd2813a(self)

    def _s548d28_(self, sender):
        _fe8558b(self)

    def _sa8b7d0_(self, sender):
        _f02ca74(self)

    def _s27b177_(self, sender):
        _fa81259(self)

    def _seda449_(self, sender):
        _f671162(self)

    def _s0aea79_(self, sender):
        _f419857(self)

    def _sca5032_(self, sender):
        _f749d82(self)

    def _seda4e6_(self, sender):
        _f060b91(self)

    def _sc9d09f_(self, sender):
        _f6b2709(self)

    def _s1f95a9_(self, sender):
        _fe0e746(self)

    def _scf4b08_(self, sender):
        _f6856a6(self)

    def _s94d3a2_(self, sender):
        _fa54fe2(self)

    def _s1fa2dd_(self, sender):
        _f211614(self)

    @objc.python_method
    def _fbce15a(self, key):
        if key not in self._v559d1e:
            self._v559d1e[key] = _fbce15a(key)
        return self._v559d1e[key]

    @objc.python_method
    def _f9807cd(self, key, value):
        _f9807cd(key, value)
        self._v559d1e[key] = value

    @objc.python_method
    def foregroundInViewCoords(self):
        _fe2d0e2(self, self._record_times)
        _fe28316(self, Glyphs.fonts)

    @objc.python_method
    def __file__(self):
        return __file__
