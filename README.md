<div align="center">

# TypeSpan

▶ [TypeSpan Official Website](https://typespan.com) ◀

The time tracking and workflow reporting plugin for [Glyphs.app](https://glyphsapp.com/).

![TypeSpan overlay displayed in Glyphs.app edit view](images/cover.png)

TypeSpan runs quietly in the background while you design. It measures how long you spend on each glyph and master, then renders detailed reports in a web dashboard. Helping you understand your workflow, estimate future projects, and share with others.

</div>


## Requirements

- macOS
- Glyphs 3 or later
- Python 3 and [Vanilla](https://vanilla.robotools.dev/) installed via the Glyphs Plugin Manager

## Installation

**Via Plugin Manager (recommended)**


1. Open Glyphs.app and go to **Window > Plugin Manager**
2. In the **Modules** tab, install **Python** and **Vanilla**
3. In the **Plugins** tab, search for **TypeSpan** and click **Install**
4. Restart Glyphs.app


![Installing TypeSpan via the Glyphs Plugin Manager and restarting](https://typespan.com/guide/install-restart-glyphs.gif)


**Manual**

1. In the **Modules** tab of Plugin Manager, install **Python** and **Vanilla**
2. Download `TypeSpan.glyphsReporter` from this repository
3. Double-click the file. Glyphs.app will install it automatically
4. Restart Glyphs.app

## Getting Started

![Enabling TypeSpan from the View menu in Glyphs.app](https://typespan.com/guide/enable-typespan-view-menu.gif)


1. After restarting, go to **View > Show TypeSpan** to activate the plugin
2. Open any glyph in Edit view. TypeSpan starts tracking automatically.
3. When you switch to another app, tracking pauses. When you return, it resumes seamlessly.
4. All tracking data is stored locally inside your Glyphs font files. Nothing leaves your machine until you choose to export.

![TypeSpan automatically pausing and resuming tracking when switching apps](https://typespan.com/guide/auto-pause-resume-tracking.gif)

## Preferences

1. Right-click anywhere in Edit view and select **TypeSpan Preferences** from the context menu

![Opening TypeSpan Preferences from the right-click context menu](https://typespan.com/guide/context-menu-settings.gif)

1. For the full settings panel, go to **Window > TypeSpan Preferences**

![TypeSpan Preferences window](https://typespan.com/guide/preferences-window.gif)

## Exporting Reports

TypeSpan can generate web-based reports showing time spent per glyph, per master, and across your entire project.

1. Go to **File > Export TypeSpan Report...**
2. Review the data you'd like to include and click **Export**
3. Your report will be uploaded and a shareable link will be generated

![Export TypeSpan Report dialog with data options](https://typespan.com/guide/export-options-dialog.gif)


TypeSpan only collects time-tracking data and the minimal font metadata you explicitly permit. It never accesses or transmits your glyph outline data.

## Support

- Guide: [Getting Started | TypeSpan](https://typespan.com/guide)
- FAQ: [Frequently Asked Questions | TypeSpan](https://typespan.com/faq)
- Contact: [hello@typespan.com](mailto:hello@typespan.com)

## License

Copyright (c) 2026 TypeSpan. All rights reserved.
