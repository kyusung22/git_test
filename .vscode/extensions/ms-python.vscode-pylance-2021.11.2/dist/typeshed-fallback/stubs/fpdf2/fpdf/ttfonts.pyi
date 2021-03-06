from typing import Any

GF_WORDS: Any
GF_SCALE: Any
GF_MORE: Any
GF_XYSCALE: Any
GF_TWOBYTWO: Any

def sub32(x, y): ...
def calcChecksum(data): ...

class TTFontFile:
    maxStrLenRead: int
    def __init__(self) -> None: ...
    filename: Any
    charWidths: Any
    glyphPos: Any
    charToGlyph: Any
    tables: Any
    otables: Any
    ascent: int
    descent: int
    version: Any
    def getMetrics(self, file) -> None: ...
    numTables: Any
    searchRange: Any
    entrySelector: Any
    rangeShift: Any
    def readTableDirectory(self) -> None: ...
    def get_table_pos(self, tag): ...
    def seek(self, pos) -> None: ...
    def skip(self, delta) -> None: ...
    def seek_table(self, tag, offset_in_table: int = ...): ...
    def read_tag(self): ...
    def read_short(self): ...
    def read_ushort(self): ...
    def read_ulong(self): ...
    def get_ushort(self, pos): ...
    @staticmethod
    def splice(stream, offset, value): ...
    def get_chunk(self, pos, length): ...
    def get_table(self, tag): ...
    def add(self, tag, data) -> None: ...
    sFamilyClass: int
    sFamilySubClass: int
    name: Any
    familyName: Any
    styleName: Any
    fullName: Any
    uniqueFontID: Any
    unitsPerEm: Any
    bbox: Any
    capHeight: Any
    stemV: Any
    italicAngle: Any
    underlinePosition: Any
    underlineThickness: Any
    flags: int
    def extractInfo(self) -> None: ...
    maxUni: int
    codeToGlyph: Any
    glyphdata: Any
    def makeSubset(self, file, subset): ...
    def getGlyphs(self, originalGlyphIdx, nonlocals) -> None: ...
    defaultWidth: Any
    def getHMTX(self, numberOfHMetrics, numGlyphs, glyphToChar, scale) -> None: ...
    def getHMetric(self, numberOfHMetrics, gid): ...
    def getLOCA(self, indexToLocFormat, numGlyphs) -> None: ...
    maxUniChar: int
    def getCMAP4(self, unicode_cmap_offset, glyphToChar, charToGlyph) -> None: ...
    def getCMAP12(self, unicode_cmap_offset, glyphToChar, charToGlyph) -> None: ...
    def endTTFile(self, stm): ...
