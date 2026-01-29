#!/usr/bin/env python3

import fontforge

hgtw = fontforge.open("HGTW.sfdir")

hgtw.selection.all()
hgtw.stroke("circular", 50)
hgtw.autoHint()
hgtw.autoInstr()

hgtw.generate("HGTW.ttf")
hgtw.generate("HGTW.otf")
hgtw.generate("HGTW.woff2", flags=("opentype",))

hgtw.close()
