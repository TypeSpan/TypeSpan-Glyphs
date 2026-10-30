# encoding: utf-8
import objc
from GlyphsApp.plugins import *
from ca7fdbbecab7f959a import *

class TypeSpan(ReporterPlugin):
    @objc.python_method
    def settings(self):
        self.menuName = t("plugin.menu_name")
        self._version_ok = _f96131a()
        if not self._version_ok:
            return
        _f2c3724()
        self._record_times = {}
        self._prune_frame = 0
        self._fbca76a()
        self._fc9a726()

    @objc.python_method
    def start(self):
        if not getattr(self, '_version_ok', False):
            return
        _f22c9bb()
        _fa2c401(lambda timer: _f8cb12a())
        _fb1966a()
        _fe9826d()

    @objc.python_method
    def _fbca76a(self):
        _f362095(self)

    @objc.python_method
    def _fc9a726(self):
        _f06d80c(self)

    def _s2538b8_(self, sender):
        _f5ded5b(sender, self)

    def _s0274ec_(self, sender):
        _ffa36a5(sender)

    @objc.python_method
    def conditionalContextMenus(self):
        menu_items = _fd381e3(self)
        return _f943fb8(menu_items, self, t("plugin.menu.preferences"))

    def _s4388c3_(self, sender):
        _fd35541(self, 'file_display', 'hide')

    def _sa062c3_(self, sender):
        _fd35541(self, 'file_display', 'today')

    def _s650d83_(self, sender):
        _fd35541(self, 'file_display', 'all')

    def _s5f20d0_(self, sender):
        _fd35541(self, 'master_display', 'today')

    def _saf9650_(self, sender):
        _fd35541(self, 'master_display', 'all')

    def _s7756cb_(self, sender):
        _fd35541(self, 'master_display', 'hide')

    def _s0d5eed_(self, sender):
        _fd35541(self, 'glyph_display', 'this_master_today')

    def _s0e4ca8_(self, sender):
        _fd35541(self, 'glyph_display', 'this_master_all_time')

    def _sbdb8c8_(self, sender):
        _fd35541(self, 'glyph_display', 'all_masters_today')

    def _s943561_(self, sender):
        _fd35541(self, 'glyph_display', 'all_masters_all_time')

    def _seb48bd_(self, sender):
        _fd35541(self, 'glyph_display', 'hide')

    def _sf688fc_(self, sender):
        _fd35541(self, 'position', 'upperLeft')

    def _s1f978b_(self, sender):
        _fd35541(self, 'position', 'upperCenter')

    def _sc2ee1d_(self, sender):
        _fd35541(self, 'position', 'upperRight')

    def _s1163e7_(self, sender):
        _fd35541(self, 'position', 'lowerLeft')

    def _s457b2f_(self, sender):
        _fd35541(self, 'position', 'lowerRight')

    def _sd5eb23_(self, sender):
        _fd35541(self, 'position', 'hide_all')

    def _s5f41db_(self, sender):
        _f67393f(self)

    def _sc98e56_(self, sender):
        _fbc8693(self)

    @objc.python_method
    def _f4a3ffe(self, key):
        return _f4a3ffe(key)

    @objc.python_method
    def _f4bae3f(self, key, value):
        _f4bae3f(key, value)

    @objc.python_method
    def foregroundInViewCoords(self):
        _fe40762(self, self._record_times)
        _f7694c1(self, Glyphs.fonts)

    @objc.python_method
    def __file__(self):
        return __file__
