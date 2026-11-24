"""Validate the icon catalog and the standalone SVGs using Python stdlib."""
from pathlib import Path
import json
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
catalog = json.loads((root / "icons.json").read_text(encoding="utf-8"))
assert len(catalog) == len(set(catalog)), "duplicate icon names"
assert set(catalog) == {p.stem for p in (root / "icons").glob("*.svg")}, "catalog and SVG files differ"
for name, labels in catalog.items():
    assert labels.get("en") and labels.get("ar"), f"missing translation: {name}"
    svg = ET.parse(root / "icons" / f"{name}.svg").getroot()
    assert svg.attrib.get("viewBox") == "0 0 24 24", f"wrong viewBox: {name}"
    assert svg.attrib.get("fill") == "none", f"unexpected fill: {name}"
    assert svg.attrib.get("stroke") == "currentColor", f"unexpected stroke: {name}"
    assert len(list(svg)), f"empty icon: {name}"
    for element in svg.iter():
        assert element.tag.rsplit("}", 1)[-1] in {"svg", "path", "circle", "rect", "polyline", "line"}, f"unsupported element: {name}"
        assert not any(k.rsplit("}", 1)[-1] in {"href", "onload", "style"} for k in element.attrib), f"unsafe attribute: {name}"
print(f"Validated {len(catalog)} icons")
