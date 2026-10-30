# encoding: utf-8
import objc
from GlyphsApp.plugins import *
from ce29ac5e2c8a0c2c5 import *

class TypeSpan(ReporterPlugin):
    @objc.python_method
    def settings(self):
        self.menuName = t("plugin.menu_name")
        self._version_ok = _fe28199()
        if not self._version_ok:
            return
        _f7b15cb()
        self._record_times = {}
        self._prune_frame = 0
        self._f8ccb94()
        self._fb11df8()

    @objc.python_method
    def start(self):
        if not getattr(self, '_version_ok', False):
            return
        _f783fdf()
        _f83100a(lambda timer: _f400574())
        _f93b5a6()
        _f7cb069()

    @objc.python_method
    def _f8ccb94(self):
        _fc81ac2(self)

    @objc.python_method
    def _fb11df8(self):
        _f56a379(self)

    def _s6aff5a_(self, sender):
        _fe315cf(sender, self)

    def _s6f1ae8_(self, sender):
        _f343387(sender)

    @objc.python_method
    def conditionalContextMenus(self):
        menu_items = _f0849fa(self)
        return _f1ef2e6(menu_items, self, t("plugin.menu.preferences"))

    def _s4afccd_(self, sender):
        _f65e551(self, 'file_display', 'hide')

    def _s12ccd2_(self, sender):
        _f65e551(self, 'file_display', 'today')

    def _s2cb5a9_(self, sender):
        _f65e551(self, 'file_display', 'all')

    def _s188ba1_(self, sender):
        _f65e551(self, 'master_display', 'today')

    def _s3e7122_(self, sender):
        _f65e551(self, 'master_display', 'all')

    def _sfaf53e_(self, sender):
        _f65e551(self, 'master_display', 'hide')

    def _sc68f83_(self, sender):
        _f65e551(self, 'glyph_display', 'this_master_today')

    def _sf590b3_(self, sender):
        _f65e551(self, 'glyph_display', 'this_master_all_time')

    def _s1a174c_(self, sender):
        _f65e551(self, 'glyph_display', 'all_masters_today')

    def _sf65c77_(self, sender):
        _f65e551(self, 'glyph_display', 'all_masters_all_time')

    def _sc386a6_(self, sender):
        _f65e551(self, 'glyph_display', 'hide')

    def _s0e7520_(self, sender):
        _f65e551(self, 'position', 'upperLeft')

    def _s1cf188_(self, sender):
        _f65e551(self, 'position', 'upperCenter')

    def _s5ef62e_(self, sender):
        _f65e551(self, 'position', 'upperRight')

    def _sd3f720_(self, sender):
        _f65e551(self, 'position', 'lowerLeft')

    def _s45fcd7_(self, sender):
        _f65e551(self, 'position', 'lowerRight')

    def _s3e81b3_(self, sender):
        _f65e551(self, 'position', 'hide_all')

    def _s6ccfb8_(self, sender):
        _fa77049(self)

    def _se3b95c_(self, sender):
        _ffcae55(self)

    @objc.python_method
    def _fab4f3b(self, key):
        return _fab4f3b(key)

    @objc.python_method
    def _f1ded59(self, key, value):
        _f1ded59(key, value)

    @objc.python_method
    def foregroundInViewCoords(self):
        _f673810(self, self._record_times)
        _fb22a47(self, Glyphs.fonts)

    @objc.python_method
    def __file__(self):
        return __file__
