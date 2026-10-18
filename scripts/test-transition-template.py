#!/usr/bin/env python3
"""Check that the legacy Unraid entry is a safe ChaptarrNG handoff."""

from pathlib import Path
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "bookshelfng.xml"


def main() -> None:
    container = ET.parse(TEMPLATE).getroot()

    def value(name: str) -> str:
        node = container.find(name)
        assert node is not None, f"Missing {name}"
        return (node.text or "").strip()

    assert value("Name") == "BookshelfNG", "Keep the legacy Unraid app identity for in-place updates"
    assert value("Repository") == "ghcr.io/snapetech-org/chaptarrng:latest"
    assert value("TemplateURL").endswith("bookshelfng-unraid/main/templates/bookshelfng.xml")
    assert value("WebUI") == "http://[IP]:[PORT:8787]/"

    configs = {node.get("Name"): node for node in container.findall("Config")}
    expected = {
        "Web UI Port": ("8787", "8787", "8787"),
        "Appdata": ("/config", "/mnt/user/appdata/bookshelfng", "/mnt/user/appdata/bookshelfng"),
        "Media": ("/data", "/mnt/user/media", "/mnt/user/media"),
        "Downloads": ("/download", "/mnt/user/downloads", "/mnt/user/downloads"),
        "PUID": ("PUID", "99", "99"),
        "PGID": ("PGID", "100", "100"),
        "TZ": ("TZ", "Etc/UTC", "Etc/UTC"),
        "HARDCOVER": ("HARDCOVER", "true", "true"),
        "HARDCOVER_NATIVE": ("HARDCOVER_NATIVE", "true", "true"),
        "HARDCOVER_AUTH": ("HARDCOVER_AUTH", "", ""),
    }
    for name, (target, default, text) in expected.items():
        node = configs.get(name)
        assert node is not None, f"Missing legacy setting {name}"
        assert node.get("Target") == target, f"Changed target for {name}"
        assert node.get("Default") == default, f"Changed default for {name}"
        assert (node.text or "").strip() == text, f"Changed stored template value for {name}"

    for name in ("HARDCOVER_API_KEY", "HARDCOVER_API_URL", "BOOKSHELF_M4B_MERGE",
                 "BOOKSHELF_M4B_AAC_BITRATE_KBPS", "BOOKSHELF_FFMPEG_PATH"):
        assert name in configs, f"Missing compatibility setting {name}"

    description = value("Description").lower()
    for required in ("independent backup", "rollback", "unsupported databases fail closed"):
        assert required in description, f"Missing operator guidance: {required}"

    print("Legacy Unraid transition template checks passed.")


if __name__ == "__main__":
    main()
