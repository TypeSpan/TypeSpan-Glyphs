# encoding: utf-8
import objc
from GlyphsApp.plugins import *
from c158e7fd7e93a852a import *

class TypeSpan(ReporterPlugin):
    @objc.python_method
    def settings(self):
        self.menuName = t("plugin.menu_name")
        if not _f6c23b8():
            return
        _f3b14ff()
        self._record_times = {}
        self._v3c50ae = {}
        self._prune_frame = 0
        self._f327d15()
        self._fad799d()

    @objc.python_method
    def start(self):
        _f1580f8()
        _f974fe8()

    @objc.python_method
    def _f327d15(self):
        _f906cb5(self)

    @objc.python_method
    def _fad799d(self):
        _fb3cb03(self)

    def _s5f58c1_(self, sender):
        _ff83050(sender, self)

    def _s6a00da_(self, sender):
        _f1d4525(sender)

    @objc.python_method
    def conditionalContextMenus(self):
        menu_items = _fca5d1c(self)
        return _ff906dc(menu_items, self, t("plugin.menu.preferences"))

    def _s141b70_(self, sender):
        _f762773(self, 'file_display', 'hide')

    def _s5ad8da_(self, sender):
        _f762773(self, 'file_display', 'today')

    def _sda22f3_(self, sender):
        _f762773(self, 'file_display', 'all')

    def _sdc969c_(self, sender):
        _f762773(self, 'master_display', 'today')

    def _sc5b3aa_(self, sender):
        _f762773(self, 'master_display', 'all')

    def _sbbc166_(self, sender):
        _f762773(self, 'master_display', 'hide')

    def _s9e8e18_(self, sender):
        _f762773(self, 'glyph_display', 'this_master_today')

    def _s9842ee_(self, sender):
        _f762773(self, 'glyph_display', 'this_master_all_time')

    def _sc47ec6_(self, sender):
        _f762773(self, 'glyph_display', 'all_masters_today')

    def _sb1c3e6_(self, sender):
        _f762773(self, 'glyph_display', 'all_masters_all_time')

    def _sc65de8_(self, sender):
        _f762773(self, 'glyph_display', 'hide')

    def _s580416_(self, sender):
        _f762773(self, 'position', 'upperLeft')

    def _sdea035_(self, sender):
        _f762773(self, 'position', 'upperCenter')

    def _s4ca208_(self, sender):
        _f762773(self, 'position', 'upperRight')

    def _s8b910a_(self, sender):
        _f762773(self, 'position', 'lowerLeft')

    def _s5a2796_(self, sender):
        _f762773(self, 'position', 'lowerRight')

    def _s754646_(self, sender):
        _f762773(self, 'position', 'hide_all')

    def _s49971e_(self, sender):
        _f84230e(self)

    def _sf08e7c_(self, sender):
        _f278e89(self)

    @objc.python_method
    def _f1a29f0(self, key):
        if key not in self._v3c50ae:
            self._v3c50ae[key] = _f1a29f0(key)
        return self._v3c50ae[key]

    @objc.python_method
    def _fe53034(self, key, value):
        _fe53034(key, value)
        self._v3c50ae[key] = value

    @objc.python_method
    def foregroundInViewCoords(self):
        _fc92524(self, self._record_times)
        _f2023c0(self, Glyphs.fonts)

    @objc.python_method
    def __file__(self):
        return __file__
