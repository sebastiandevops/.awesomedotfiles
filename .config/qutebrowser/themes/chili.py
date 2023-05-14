#!/usr/bin/env python3
clr = {
    "bg": "#282828", # bg, gunmetal OK
    "bg-material": "#242424",
    "bg-alt": "#121212", #bg-alt, eerie-black OK
    # "rich-black": "#001021", # rich black FOGRA 29 (extra)
    "smoky-black": "#282828", # smoky black (extra) OK
    "bg-selected": "#242424", #bg-selected OK
    "bg-lightened": "#286983", #bg-lightened OK
    "fg-disabled": "#909090", #fg-disabled OK
    "fg": "#909090", #base05 (white-ish, cadet-blue-crayola) OK

    # "cbc-alt": "#9CAABB", # base08 (white-ish, cadet-blue alt)
    # "fg-alt": "#728ca0", #base06 (bright white, light-slate-gray)
    "maya-blue": "#56949f", # blue OK
    "paradise-pink": "#eb6f92", # red OK
    "pink": "#b4637a",
    "lava-red": "#C81D25", # red (extra)
    "persian-orange": "#ea9d34", # orange OK
    "gold-crayola": "#f6c177", # yellow OK
    "celadon": "#9ccfd8", # green OK
    "dark-cyan": "#008b94", # dark cyan OK
    "cornflower-blue": "#eb6f92", # bright blue OK
    "shimmering-blush": "#eb6f92", # magenta OK
    "maroon-x11": "#9ccfd8", # violet OK
    "electric-blue": "#70E1E8", # cyan (extra) OK
    "midnight-green-eagle": "#114B5F", # unused (extra) OK
    "fg-white": "#e0def4",
    "fg-gray": "#a09eb4",
    "gray": "#BBe0def4",
    "iris": "#575757",
    "deep-iris": "#808080",
    "grey-iris": "#484848",
    "rose": "#d7827e",
    "rose-low": "#ebbcba",
    "bg-pine": "#BB286983",
}

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
# Type: List of QtColor, or QtColor
c.colors.completion.fg = clr["fg"]

# Background color of the completion widget for odd rows.
# Type: QssColor
c.colors.completion.odd.bg = clr["bg-material"]

# Background color of the completion widget for even rows.
# Type: QssColor
c.colors.completion.even.bg = clr["bg"]

# Foreground color of completion widget category headers.
# Type: QtColor
c.colors.completion.category.fg = clr["paradise-pink"]

# Background color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.bg = clr["bg"]

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.top = clr["bg"]

# Bottom border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.bottom = clr["bg"]

# Foreground color of the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.fg = clr["paradise-pink"]

# Background color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.bg = clr["bg-alt"]

# Top border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.top = clr["bg-alt"]

# Bottom border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.bottom = clr["bg-alt"]

# Foreground color of the matched text in the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.match.fg = clr["rose-low"]

# Foreground color of the matched text in the completion.
# Type: QtColor
c.colors.completion.match.fg = clr["fg-white"]

# Color of the scrollbar handle in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.fg = clr["fg"]

# Color of the scrollbar in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.bg = clr["bg"]

# Background color of the context menu. If set to null, the Qt default
# is used.
# Type: QssColor
c.colors.contextmenu.menu.bg = clr["bg"]

# Foreground color of the context menu. If set to null, the Qt default
# is used.
# Type: QssColor
c.colors.contextmenu.menu.fg = clr["fg"]

# Background color of the context menu's selected item. If set to null,
# the Qt default is used.
# Type: QssColor
c.colors.contextmenu.selected.bg = clr["bg-selected"]

# Foreground color of the context menu's selected item. If set to null,
# the Qt default is used.
# Type: QssColor
c.colors.contextmenu.selected.fg = clr["fg"]

# Background color of disabled items in the context menu. If set to
# null, the Qt default is used.
# Type: QssColor
c.colors.contextmenu.disabled.bg = clr["bg-alt"]

# Foreground color of disabled items in the context menu. If set to
# null, the Qt default is used.
# Type: QssColor
c.colors.contextmenu.disabled.fg = clr["fg-disabled"]

# Background color for the download bar.
# Type: QssColor
c.colors.downloads.bar.bg = clr["bg"]

# Color gradient start for download text.
# Type: QtColor
c.colors.downloads.start.fg = clr["bg"]

# Color gradient start for download backgrounds.
# Type: QtColor
c.colors.downloads.start.bg = clr["cornflower-blue"]

# Color gradient end for download text.
# Type: QtColor
c.colors.downloads.stop.fg = clr["bg"]

# Color gradient stop for download backgrounds.
# Type: QtColor
c.colors.downloads.stop.bg = clr["paradise-pink"]

# Foreground color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.fg = clr["paradise-pink"]

c.hints.border = "0px"

# Font color for hints.
# Type: QssColor
c.colors.hints.fg = clr["fg-white"]

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
# Type: QssColor
c.colors.hints.bg = clr["bg-pine"]

# Font color for the matched part of hints.
# Type: QtColor
c.colors.hints.match.fg = clr["paradise-pink"]

# Text color for the keyhint widget.
# Type: QssColor
c.colors.keyhint.fg = clr["fg"]

# Highlight color for keys to complete the current keychain.
# Type: QssColor
c.colors.keyhint.suffix.fg = clr["gold-crayola"]

# Background color of the keyhint widget.
# Type: QssColor
c.colors.keyhint.bg = clr["bg"]

# Foreground color of an error message.
# Type: QssColor
c.colors.messages.error.fg = clr["paradise-pink"]

# Background color of an error message.
# Type: QssColor
c.colors.messages.error.bg = clr["bg"]

# Border color of an error message.
# Type: QssColor
c.colors.messages.error.border = clr["paradise-pink"]

# Foreground color of a warning message.
# Type: QssColor
c.colors.messages.warning.fg = clr["persian-orange"]

# Background color of a warning message.
# Type: QssColor
c.colors.messages.warning.bg = clr["bg"]

# Border color of a warning message.
# Type: QssColor
c.colors.messages.warning.border = clr["persian-orange"]

# Foreground color of an info message.
# Type: QssColor
c.colors.messages.info.fg = clr["electric-blue"]

# Background color of an info message.
# Type: QssColor
c.colors.messages.info.bg = clr["bg"]

# Border color of an info message.
# Type: QssColor
c.colors.messages.info.border = clr["electric-blue"]

# Foreground color for prompts.
# Type: QssColor
c.colors.prompts.fg = clr["fg"]

# Border used around UI elements in prompts.
# Type: String
c.colors.prompts.border = clr["bg"]

# Background color for prompts.
# Type: QssColor
c.colors.prompts.bg = clr["bg"]

# Foreground color for the selected item in filename prompts.
# Type: QssColor
c.colors.prompts.selected.fg = clr["fg"]

# Background color for the selected item in filename prompts.
# Type: QssColor
c.colors.prompts.selected.bg = clr["bg-selected"]

# Foreground color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.fg = clr["paradise-pink"]

# Background color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.bg = clr["bg"]

# Foreground color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.fg = clr["bg"]

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.bg = clr["pink"]

# Foreground color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.fg = clr["bg"]

# Background color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.bg = clr["bg-lightened"]

# Foreground color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.fg = clr["bg"]

# Background color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.bg = clr["bg-alt"]

# Foreground color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.fg = clr["fg-white"]

# Background color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.bg = clr["bg"]

# Foreground color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.fg = clr["fg"]

# Background color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.bg = clr["bg"]

# Foreground color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.fg = clr["bg"]

# Background color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.bg = clr["rose"]

# Foreground color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.fg = clr["fg-white"]

# Background color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.bg = clr["bg-lightened"]

# Background color of the progress bar.
# Type: QssColor
c.colors.statusbar.progress.bg = clr["paradise-pink"]

# Default foreground color of the URL in the statusbar.
# Type: QssColor
c.colors.statusbar.url.fg = clr["fg"]

# Foreground color of the URL in the statusbar on error.
# Type: QssColor
c.colors.statusbar.url.error.fg = clr["paradise-pink"]

# Foreground color of the URL in the statusbar for hovered links.
# Type: QssColor
c.colors.statusbar.url.hover.fg = clr["electric-blue"]

# Foreground color of the URL in the statusbar on successful load
# (http).
# Type: QssColor
c.colors.statusbar.url.success.http.fg = clr["fg"]

# Foreground color of the URL in the statusbar on successful load
# (https).
# Type: QssColor
c.colors.statusbar.url.success.https.fg = clr["fg-white"]

# Foreground color of the URL in the statusbar when there's a warning.
# Type: QssColor
c.colors.statusbar.url.warn.fg = clr["shimmering-blush"]

# Background color of the tab bar.
# Type: QssColor
c.colors.tabs.bar.bg = clr["bg"]

# Color gradient start for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.start = clr["pink"]

# Color gradient end for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.stop = clr["pink"]

# Color for the tab indicator on errors.
# Type: QtColor
c.colors.tabs.indicator.error = clr["lava-red"]

# Foreground color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.fg = clr["fg-gray"]

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = clr["bg"]

# Foreground color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.fg = clr["fg-gray"]

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = clr["bg"]

# Foreground color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.fg = clr["fg-white"]

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = clr["bg-alt"]

# Foreground color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.fg = clr["fg-white"]

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = clr["bg-alt"]

# Foreground color of pinned unselected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.odd.fg = clr["fg-gray"]

# Background color of pinned unselected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.odd.bg = clr["smoky-black"]

# Foreground color of pinned unselected even tabs.
# Type: QtColor
c.colors.tabs.pinned.even.fg = clr["fg-gray"]

# Background color of pinned unselected even tabs.
# Type: QtColor
c.colors.tabs.pinned.even.bg = clr["smoky-black"]

# Foreground color of pinned selected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.odd.fg = clr["fg-white"]

# Background color of pinned selected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.odd.bg = clr["bg-alt"]

# Foreground color of pinned selected even tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.even.fg = clr["fg-white"]

# Background color of pinned selected even tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.even.bg = clr["bg-alt"]

# Background color for webpages if unset (or empty to use the theme's
# color).
# Type: QtColor
c.colors.webpage.bg = clr["bg"]
