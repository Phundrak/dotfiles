# pylint: disable=C0111
from qutebrowser.config.configfiles import ConfigAPI  # noqa: F401
from qutebrowser.config.config import ConfigContainer  # noqa: F401

config: ConfigAPI = config  # noqa: F821 pylint: disable=E0602,C0103
c: ConfigContainer = c  # noqa: F821 pylint: disable=E0602,C0103

# config.bind(',v', 'spawn mpv {url}')
# config.bind(',d', 'spawn ytdl {url}')

# bookmarks
config.bind(",ba", "bookmark-add")
config.bind(",bb", "cmd-set-text -s :bookmark-load")
config.bind(",bl", "bookmark-list")
config.bind(",bj", "bookmark-list --jump")
config.bind(",bt", "cmd-set-text -s :bookmark-load -t")
config.bind(",bw", "cmd-set-text -s :bookmark-load -w")
config.bind(",bql", "cmd-set-text -s :quickmark-load")
config.bind(",bqL", "cmd-set-text -s :quickmark-load -t")
config.bind(",bqs", "quickmark-save")
config.bind(",bqw", "cmd-set-text -s :quickmark-load -w")

# config cycle
config.bind(
    ",cCH",
    "config-cycle -p -u *://*.{url:host}/* content.cookies.accept all no-3rdparty never ;; reload",
)
config.bind(
    ",cCh",
    "config-cycle -p -u *://{url:host}/* content.cookies.accept all no-3rdparty never ;; reload",
)
config.bind(
    ",cCu",
    "config-cycle -p -u {url} content.cookies.accept all no-3rdparty never ;; reload",
)
config.bind(",cIH", "config-cycle -p -u *://*.{url:host}/* content.images ;; reload")
config.bind(",cIh", "config-cycle -p -u *://{url:host}/* content.images ;; reload")
config.bind(",cIu", "config-cycle -p -u {url} content.images ;; reload")
config.bind(",cPH", "config-cycle -p -u *://*.{url:host}/* content.plugins ;; reload")
config.bind(",cPh", "config-cycle -p -u *://{url:host}/* content.plugins ;; reload")
config.bind(",cPu", "config-cycle -p -u {url} content.plugins ;; reload")
config.bind(
    ",cSH", "config-cycle -p -u *://*.{url:host}/* content.javascript.enabled ;; reload"
)
config.bind(
    ",cSh", "config-cycle -p -u *://{url:host}/* content.javascript.enabled ;; reload"
)
config.bind(",cSu", "config-cycle -p -u {url} content.javascript.enabled ;; reload")
config.bind(
    ",ccH",
    "config-cycle -p -t -u *://*.{url:host}/* content.cookies.accept all no-3rdparty never ;; reload",
)
config.bind(
    ",cch",
    "config-cycle -p -t -u *://{url:host}/* content.cookies.accept all no-3rdparty never ;; reload",
)
config.bind(
    ",ccu",
    "config-cycle -p -t -u {url} content.cookies.accept all no-3rdparty never ;; reload",
)
config.bind(",ch", "back -t")
config.bind(",ciH", "config-cycle -p -t -u *://*.{url:host}/* content.images ;; reload")
config.bind(",cih", "config-cycle -p -t -u *://{url:host}/* content.images ;; reload")
config.bind(",ciu", "config-cycle -p -t -u {url} content.images ;; reload")
config.bind(",cl", "forward -t")
config.bind(
    ",cpH", "config-cycle -p -t -u *://*.{url:host}/* content.plugins ;; reload"
)
config.bind(",cph", "config-cycle -p -t -u *://{url:host}/* content.plugins ;; reload")
config.bind(",cpu", "config-cycle -p -t -u {url} content.plugins ;; reload")
config.bind(
    ",csH",
    "config-cycle -p -t -u *://*.{url:host}/* content.javascript.enabled ;; reload",
)
config.bind(
    ",csh",
    "config-cycle -p -t -u *://{url:host}/* content.javascript.enabled ;; reload",
)
config.bind(",csu", "config-cycle -p -t -u {url} content.javascript.enabled ;; reload")

# downloads
config.bind(",da", "download-cancel")
config.bind(",dd", "download")
config.bind(",dc", "download-clear")
config.bind(",dy", "spawn ytdl {url}")

# dev tools
config.bind(",Dd", "devtools")
config.bind(",Df", "devtools-focus")
config.bind(",Dc", "devtools left")
config.bind(",Dt", "devtools bottom")
config.bind(",Ds", "devtools top")
config.bind(",Dr", "devtools right")
config.bind(",Dw", "devtools window")

# save
config.bind("fs", "save")

# hints
config.bind(",hd", "hint links download")
config.bind(",hh", "hint")
config.bind(",hH", "hint all hover")
config.bind(",hii", "hint images")
config.bind(",hiI", "hint images tab")
config.bind(",hIi", "hint inputs")
config.bind(",hIf", "hint inputs --first")
config.bind(",hO", "hint links fill :open -t -r {hint-url}")
config.bind(",ho", "hint links fill :open {hint-url}")
config.bind(",hR", "hint --rapid links window")
config.bind(",hr", "hint --rapid links tab-bg")
config.bind(",htb", "hint all tab-bg")
config.bind(",htf", "hint all tab-fg")
config.bind(",htt", "hint all tab")
config.bind(",hw", "hint all window")
config.bind(",hy", "hint links yank")
config.bind(",hY", "hint links yank-primary")
# Bindings for hint mode
config.bind("<Ctrl-B>", "hint all tab-bg", mode="hint")
config.bind("<Ctrl-F>", "hint links", mode="hint")
config.bind("<Ctrl-R>", "hint --rapid links tab-bg", mode="hint")
config.bind("<Escape>", "mode-leave", mode="hint")
config.bind("<Return>", "hint-follow", mode="hint")

# Move
config.bind("<Ctrl-PgDown>", "tab-next")
config.bind("<Ctrl-C>", "back -w")
config.bind("<Ctrl-R>", "forward -w")
config.bind("<Ctrl-h>", "home")
config.bind("T", "tab-next")
config.bind("S", "tab-prev")
config.bind("C", "back")
config.bind("R", "forward")

# cmd
config.bind(",sb", "cmd-set-text -s :bind")
config.bind(",st", "cmd-set-text -s :set -t")
config.bind(",ss", "set")
config.bind(",sS", "cmd-set-text -s :set")

# open
config.bind("<Ctrl-N>", "open -w")
config.bind("<Ctrl-Shift-N>", "open -p")
config.bind("<Ctrl-T>", "open -t")
config.bind(",ob", "cmd-set-text -s :open -b")
config.bind(",oB", "cmd-set-text :open -b -r {url:pretty}")
config.bind(",oP", "cmd-set-text :open -t -r {url:pretty}")
config.bind(",ott", "open -t")
config.bind(",otT", "cmd-set-text -s :open -t")
config.bind(",ow", "cmd-set-text -s :open -w")
config.bind(",oW", "cmd-set-text :open -w {url:pretty}")
config.bind(",occ", "open -- {clipboard}")
config.bind(",ocC", "open -t -- {clipboard}")
config.bind(",ocp", "open -- {primary}")
config.bind(",ocP", "open -t -- {primary}")
config.bind(",ocw", "open -w -- {clipboard}")
config.bind(",ocW", "open -w -- {primary}")
config.bind("o", "cmd-set-text -s :open")
config.bind("O", "cmd-set-text :open {url:pretty}")

# tabs
config.bind("<Alt-1>", "tab-focus 1")
config.bind("<Alt-2>", "tab-focus 2")
config.bind("<Alt-3>", "tab-focus 3")
config.bind("<Alt-4>", "tab-focus 4")
config.bind("<Alt-5>", "tab-focus 5")
config.bind("<Alt-6>", "tab-focus 6")
config.bind("<Alt-7>", "tab-focus 7")
config.bind("<Alt-8>", "tab-focus 8")
config.bind("<Alt-9>", "tab-focus -1")
config.bind("<Alt-m>", "tab-mute")
config.bind("<Ctrl-Tab>", "tab-focus last")
config.bind("<Ctrl-W>", "tab-close")
config.bind(",tT", "tab-move +")
config.bind(",tS", "tab-move -")
config.bind(",tn", "tab-next")
config.bind(",tp", "tab-prev")
config.bind(",t«", "tab-focus -1")
config.bind(",t»", "tab-focus 1")
config.bind(",tC", "tab-clone")
config.bind(",tD", "tab-only")
config.bind(",td", "tab-close")
config.bind(",tf", "cmd-set-text -sr :tab-focus")
config.bind(",tg", "tab-give")
config.bind(",tl", "tab-focus last")
config.bind(",tm", "tab-move")
config.bind(",tP", "tab-pin")
config.bind(",ts", "cmd-set-text -s :tab-select")

# scoll
config.bind("G", "scroll-to-perc")
config.bind("gg", "scroll-to-perc 0")
config.bind("c", "scroll left")
config.bind("t", "scroll down")
config.bind("s", "scroll up")
config.bind("r", "scroll right")
config.bind("<Ctrl-F>", "scroll-page 0 1")
config.bind("<Ctrl-B>", "scroll-page 0 -1")
config.bind("<Ctrl-D>", "scroll-page 0 0.5")
config.bind("<Ctrl-U>", "scroll-page 0 -0.5")

# navigate
config.bind(",nd", "navigate decrement")
config.bind(",ni", "navigate increment")
config.bind(",nn", "navigate prev")
config.bind(",nN", "navigate next -t")
config.bind(",np", "navigate next")
config.bind(",nP", "navigate prev -t")
config.bind(",nu", "navigate up")
config.bind(",nU", "navigate up -t")

# search
config.bind("n", "search-next")
config.bind("N", "search-prev")

# print
config.bind("<Ctrl-Alt-p>", "print")

config.bind(",qq", "quit")
config.bind(",qs", "quit --save")
config.bind(",qw", "close")
config.bind("<Ctrl-Q>", "quit")

# reload
config.bind(",rr", "reload")
config.bind(",rR", "reload -f")
config.bind("<F5>", "reload")
config.bind("<Ctrl-F5>", "reload -f")

# view
config.bind(",vh", "history")
config.bind(",vs", "view-source")
config.bind(",vm", "spawn mpv {url}")

# yank
config.bind("yd", "yank domain")
config.bind("yD", "yank domain -s")
config.bind("yi", "yank inline [{title}]({url})")
config.bind("yI", "yank inline [{title}]({url}) -s")
config.bind("yp", "yank pretty-url")
config.bind("yP", "yank pretty-url -s")
config.bind("yt", "yank title")
config.bind("yT", "yank title -s")
config.bind("yy", "yank")
config.bind("yY", "yank -s")

config.bind("<Escape>", "clear-keychain ;; search ;; fullscreen --leave")

config.bind("+", "zoom-in")
config.bind("-", "zoom-out")
config.bind("=", "zoom")

config.bind("?", "cmd-set-text ?")
config.bind("/", "cmd-set-text /")
config.bind(":", "cmd-set-text :")
config.bind(".", "repeat-command")

config.bind("<Ctrl-Shift-Tab>", "nop")
config.bind("<Ctrl-s>", "stop")
config.bind("<F11>", "fullscreen")

config.bind("<Return>", "selection-follow")
config.bind("<Ctrl-Return>", "selection-follow -t")

config.bind("<back>", "back")
config.bind("<forward>", "forward")


config.bind("<Ctrl-V>", "mode-enter passthrough")
config.bind("'", "mode-enter jump_mark")
config.bind("v", "mode-enter caret")
config.bind("V", "mode-enter caret ;; selection-toggle --line")
config.bind("`", "mode-enter set_mark")
config.bind("i", "mode-enter insert")

config.bind("q", "macro-record")
config.bind("@", "macro-run")

config.bind("U", "undo -w")
config.bind("<Ctrl-Shift-T>", "undo")
config.bind("u", "undo")

# Bindings for caret mode
config.bind("C", "scroll left", mode="caret")
config.bind("T", "scroll down", mode="caret")
config.bind("S", "scroll up", mode="caret")
config.bind("R", "scroll right", mode="caret")
config.bind("c", "move-to-prev-char", mode="caret")
config.bind("t", "move-to-next-line", mode="caret")
config.bind("s", "move-to-prev-line", mode="caret")
config.bind("r", "move-to-next-char", mode="caret")

config.bind("$", "move-to-end-of-line", mode="caret")
config.bind("0", "move-to-start-of-line", mode="caret")
config.bind("<Ctrl-Space>", "selection-drop", mode="caret")
config.bind("<Escape>", "mode-leave", mode="caret")
config.bind("<Return>", "yank selection", mode="caret")
config.bind("<Space>", "selection-toggle", mode="caret")
config.bind("v", "selection-toggle", mode="caret")
config.bind("V", "selection-toggle --line", mode="caret")
config.bind("y", "yank selection", mode="caret")
config.bind("Y", "yank selection -s", mode="caret")
config.bind("[", "move-to-start-of-prev-block", mode="caret")
config.bind("]", "move-to-start-of-next-block", mode="caret")
config.bind("{", "move-to-end-of-prev-block", mode="caret")
config.bind("}", "move-to-end-of-next-block", mode="caret")
config.bind("b", "move-to-prev-word", mode="caret")
config.bind("e", "move-to-end-of-word", mode="caret")
config.bind("gg", "move-to-start-of-document", mode="caret")
config.bind("G", "move-to-end-of-document", mode="caret")
config.bind("n", "mode-enter normal", mode="caret")
config.bind("o", "selection-reverse", mode="caret")
config.bind("w", "move-to-next-word", mode="caret")

# Bindings for command mode
config.bind("<Alt-B>", "rl-backward-word", mode="command")
config.bind("<Alt-Backspace>", "rl-backward-kill-word", mode="command")
config.bind("<Alt-D>", "rl-kill-word", mode="command")
config.bind("<Alt-F>", "rl-forward-word", mode="command")
config.bind("<Ctrl-?>", "rl-delete-char", mode="command")
config.bind("<Ctrl-A>", "rl-beginning-of-line", mode="command")
config.bind("<Ctrl-B>", "rl-backward-char", mode="command")
config.bind("<Ctrl-C>", "completion-item-yank", mode="command")
config.bind("<Ctrl-D>", "completion-item-del", mode="command")
config.bind("<Ctrl-E>", "rl-end-of-line", mode="command")
config.bind("<Ctrl-F>", "rl-forward-char", mode="command")
config.bind("<Ctrl-H>", "rl-backward-delete-char", mode="command")
config.bind("<Ctrl-K>", "rl-kill-line", mode="command")
config.bind("<Ctrl-N>", "command-history-next", mode="command")
config.bind("<Ctrl-P>", "command-history-prev", mode="command")
config.bind("<Ctrl-Return>", "command-accept --rapid", mode="command")
config.bind("<Ctrl-Shift-C>", "completion-item-yank --sel", mode="command")
config.bind("<Ctrl-Shift-Tab>", "completion-item-focus prev-category", mode="command")
config.bind("<Ctrl-Tab>", "completion-item-focus next-category", mode="command")
config.bind("<Ctrl-U>", "rl-unix-line-discard", mode="command")
config.bind("<Ctrl-W>", "rl-unix-word-rubout", mode="command")
config.bind("<Ctrl-Y>", "rl-yank", mode="command")
config.bind("<Down>", "completion-item-focus --history next", mode="command")
config.bind("<Escape>", "mode-leave", mode="command")
config.bind("<PgDown>", "completion-item-focus next-page", mode="command")
config.bind("<PgUp>", "completion-item-focus prev-page", mode="command")
config.bind("<Return>", "command-accept", mode="command")
config.bind("<Shift-Delete>", "completion-item-del", mode="command")
config.bind("<Shift-Tab>", "completion-item-focus prev", mode="command")
config.bind("<Tab>", "completion-item-focus next", mode="command")
config.bind("<Up>", "completion-item-focus --history prev", mode="command")

# Bindings for insert mode
config.bind("<Ctrl-E>", "edit-text", mode="insert")
config.bind("<Escape>", "mode-leave", mode="insert")
config.bind("<Shift-Escape>", "fake-key <Escape>", mode="insert")
config.bind("<Shift-Ins>", "insert-text -- {primary}", mode="insert")

# Bindings for passthrough mode
config.bind("<Shift-Escape>", "mode-leave", mode="passthrough")

# Bindings for prompt mode
config.bind("<Alt-B>", "rl-backward-word", mode="prompt")
config.bind("<Alt-Backspace>", "rl-backward-kill-word", mode="prompt")
config.bind("<Alt-D>", "rl-kill-word", mode="prompt")
config.bind("<Alt-F>", "rl-forward-word", mode="prompt")
config.bind("<Alt-Shift-Y>", "prompt-yank --sel", mode="prompt")
config.bind("<Alt-Y>", "prompt-yank", mode="prompt")
config.bind("<Ctrl-?>", "rl-delete-char", mode="prompt")
config.bind("<Ctrl-A>", "rl-beginning-of-line", mode="prompt")
config.bind("<Ctrl-B>", "rl-backward-char", mode="prompt")
config.bind("<Ctrl-E>", "rl-end-of-line", mode="prompt")
config.bind("<Ctrl-F>", "rl-forward-char", mode="prompt")
config.bind("<Ctrl-H>", "rl-backward-delete-char", mode="prompt")
config.bind("<Ctrl-K>", "rl-kill-line", mode="prompt")
config.bind("<Ctrl-P>", "prompt-open-download --pdfjs", mode="prompt")
config.bind("<Ctrl-U>", "rl-unix-line-discard", mode="prompt")
config.bind("<Ctrl-W>", "rl-unix-word-rubout", mode="prompt")
config.bind("<Ctrl-X>", "prompt-open-download", mode="prompt")
config.bind("<Ctrl-Y>", "rl-yank", mode="prompt")
config.bind("<Down>", "prompt-item-focus next", mode="prompt")
config.bind("<Escape>", "mode-leave", mode="prompt")
config.bind("<Return>", "prompt-accept", mode="prompt")
config.bind("<Shift-Tab>", "prompt-item-focus prev", mode="prompt")
config.bind("<Tab>", "prompt-item-focus next", mode="prompt")
config.bind("<Up>", "prompt-item-focus prev", mode="prompt")

# Bindings for register mode
config.bind("<Escape>", "mode-leave", mode="register")

# Bindings for yesno mode
config.bind("<Alt-Shift-Y>", "prompt-yank --sel", mode="yesno")
config.bind("<Alt-Y>", "prompt-yank", mode="yesno")
config.bind("<Escape>", "mode-leave", mode="yesno")
config.bind("<Return>", "prompt-accept", mode="yesno")
config.bind("N", "prompt-accept --save no", mode="yesno")
config.bind("Y", "prompt-accept --save yes", mode="yesno")
config.bind("n", "prompt-accept no", mode="yesno")
config.bind("y", "prompt-accept yes", mode="yesno")
