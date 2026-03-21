# -*- coding: utf-8 -*-
import pathlib

root = pathlib.Path(__file__).parent
he = root.joinpath("_he_extract.txt").read_text(encoding="utf-8").strip()
he_block = (
    "# Insert HE component before LE= (must not use WE — conflicts with [om,WE]=Zs(\"Toast\") in bundle)\n"
    "HE = (\n    '"
    + he
    + "},\n)\n"
)

dp_path = root / "do_patch.py"
dp = dp_path.read_text(encoding="utf-8")
start = dp.find("# Insert HE component before LE=")
if start < 0:
    raise SystemExit("start marker not found")
end = dp.find("\n\nrepls = [", start)
if end < 0:
    raise SystemExit("end marker not found")
dp_path.write_text(dp[:start] + he_block + dp[end:], encoding="utf-8")
print("OK do_patch.py HE synced")
