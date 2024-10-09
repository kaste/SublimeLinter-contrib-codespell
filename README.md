SublimeLinter-contrib-codespell
===============================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [codespell](https://github.com/codespell-project/codespell).


## Installation

SublimeLinter must be installed in order to use this plugin.  Install via [Package Control](https://packagecontrol.io) or `git clone` as usual.

Ensure that a `codespell` is actually installed somewhere on your system. Typically, 

```
pip install codespell
``` 

on the command line will do that.


## Notes

This plugin registers *codespell* for all views.  You can restrict that, e.g.
you can set

```
    "codespell": {
        "selector": "-text.plain",
    },
```

in SublimeLinter's main settings (`Preferences: SublimeLinter Settings`) to
ignore plain text files.  This can also be set per project or even per view
under the setting name `SublimeLinter.linters.codespell.selector`.

Esp. for this linter I'm used to show the correct/fixed spelling on the ride
side of the view.  You can enable that via

```
    "codespell": {
        "styles": [
            {
                "scope": "region.redish",  # any color you like
                "annotation": "{msg}",     # configure right hand side annotation
                "phantom": ""              # disable phantoms
            }
        ]
    },
```

There is also a quick-fix available if (and only if) codespell suggests exactly
*one* other spelling.  That means, if you have setup a key-binding, e.g. the one  suggested in the SublimeLinter's README

```jsonc
    // To trigger a quick action
    // { "keys": ["ctrl+k", "ctrl+f"],
    //   "command": "sublime_linter_quick_actions"
    // },
```

you can basically fix a misspelled word on the line of the cursor by typing
`ctrl+k, ctrl+f`.  (You don't need to be *on* the word, btw!  Handy.)

