"""Apply a Guizang template palette to explicitly mapped DrawingML RGB colors."""
import argparse
import os
import re
import tempfile
from pathlib import Path
from zipfile import ZipFile
from lxml import etree

DRAWING = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
PARTS = re.compile(r"^ppt/(?:slides/slide|slideLayouts/slideLayout|slideMasters/slideMaster|theme/theme|charts/chart)\d+\.xml$")

def get_palette(theme):
    assets = Path(__file__).resolve().parents[2] / "guizang-ppt-skill" / "assets"
    for filename in ("template.html", "template-swiss.html"):
        css = (assets / filename).read_text(encoding="utf-8")
        match = re.search(r'\[data-theme="' + re.escape(theme) + r'"\]\s*\{([^}]+)\}', css)
        if match:
            return dict(re.findall(r'--([\w-]+)\s*:\s*#([0-9a-fA-F]{6})\s*;', match[1]))
    raise ValueError(f"Unknown theme: {theme}")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--theme", required=True)
    parser.add_argument("--map", action="append", required=True, metavar="RRGGBB=token")
    args = parser.parse_args()
    if args.source.resolve() == args.output.resolve() or args.output.exists():
        parser.error("Choose an unused output path.")
    palette = get_palette(args.theme)
    mapping = {}
    for item in args.map:
        key, sep, role = item.partition("=")
        if not sep or not re.fullmatch(r"[0-9a-fA-F]{6}", key) or role not in palette:
            parser.error(f"Invalid color or theme role: {item}")
        mapping[key.upper()] = palette[role].upper()
    changed = 0
    with tempfile.TemporaryDirectory(dir=args.output.parent) as tmp:
        staged = Path(tmp) / "result.pptx"
        with ZipFile(args.source) as old, ZipFile(staged, "w") as new:
            for item in old.infolist():
                data = old.read(item)
                if PARTS.fullmatch(item.filename):
                    root = etree.fromstring(data)
                    dirty = False
                    for el in root.iter(DRAWING + "srgbClr"):
                        color = el.get("val", "").upper()
                        if color in mapping and color != mapping[color]:
                            el.set("val", mapping[color])
                            dirty = True
                            changed += 1
                    if dirty:
                        data = etree.tostring(root, encoding="utf-8", xml_declaration=True, standalone=True)
                new.writestr(item, data)
        if not changed:
            parser.error("No mapped colors changed; check the source palette.")
        with ZipFile(staged) as result:
            if result.testzip():
                raise ValueError("Invalid output archive")
        os.link(staged, args.output)
    print(f"Updated {changed} colors using {args.theme}.")
if __name__ == "__main__":
    main()
