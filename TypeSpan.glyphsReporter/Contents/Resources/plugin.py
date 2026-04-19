# encoding: utf-8
import objc
from GlyphsApp.plugins import *
from cb7d98855700a7735 import *

class TypeSpan(ReporterPlugin):
    @objc.python_method
    def settings(self):
        self.menuName = t("plugin.menu_name")
        if not _fac6cf5():
            return
        _f7f0898()
        self._record_times = {}
        self._v6a344c = {}
        self._prune_frame = 0
        self._f93299d()
        self._f9521dc()

    @objc.python_method
    def start(self):
        _f1900d2()

    @objc.python_method
    def _f93299d(self):
        _fdc808c(self)

    @objc.python_method
    def _f9521dc(self):
        _febcae2(self)

    def _s916eec_(self, sender):
        _f1d0b8d(sender, self)

    def _sfe8b27_(self, sender):
        _fb0de05(sender)

    @objc.python_method
    def conditionalContextMenus(self):
        dot_indicator = _fad85cd(__file__)
        menu_items = _fad5293(self, dot_indicator)
        return _fb7260d(menu_items, self, t("window.menu_item"))

    def _s62457d_(self, sender):
        _ff3e0a5(self)

    def _sd3778d_(self, sender):
        _f13129f(self)

    def _s95a4ba_(self, sender):
        _fa2b760(self)

    def _sda184d_(self, sender):
        _faf5038(self)

    def _s91ce21_(self, sender):
        _f89a06d(self)

    def _sb5f7c1_(self, sender):
        _fe08064(self)

    def _s80a659_(self, sender):
        _f15d42d(self)

    def _sdea22f_(self, sender):
        _f639dab(self)

    def _s06adee_(self, sender):
        _fc7848d(self)

    def _s34cf04_(self, sender):
        _fb2c1bb(self)

    def _sbb292d_(self, sender):
        _f7f453d(self)

    def _sb04ced_(self, sender):
        _f275244(self)

    def _sc1e70e_(self, sender):
        _f5465dd(self)

    def _s423e68_(self, sender):
        _f07145e(self)

    def _sa8706c_(self, sender):
        _fea131d(self)

    def _s0f42ae_(self, sender):
        _f650d78(self)

    def _s481cd6_(self, sender):
        _fef284c(self)

    def _s69b2d8_(self, sender):
        _f19d1c8(self)

    def _s97a903_(self, sender):
        _f2804d2(self)

    @objc.python_method
    def _fb846cb(self, key):
        if key not in self._v6a344c:
            self._v6a344c[key] = _fb846cb(key)
        return self._v6a344c[key]

    @objc.python_method
    def _f0b577c(self, key, value):
        _f0b577c(key, value)
        self._v6a344c[key] = value

    @objc.python_method
    def foregroundInViewCoords(self):
        _fff7f29(self, self._record_times)
        _f548061(self, Glyphs.fonts)

    @objc.python_method
    def __file__(self):
        return __file__
