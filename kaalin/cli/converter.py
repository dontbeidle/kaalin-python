from kaalin.converter.latin_cyrillic_converter import latin2cyrillic, cyrillic2latin
import sys
import os

def cyr2lat():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Use:\n  cyr2lat <input_file> [output_file]")
        sys.exit(1)

    input_file = sys.argv[1]

    if len(sys.argv) == 3:
        output_file = sys.argv[2]
    else:
        base, ext = os.path.splitext(input_file)
        output_file = f"{base}-lat{ext}"

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
        converted = cyrillic2latin(text)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(converted)
        print(f"✅ Converted text written to: {output_file}")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


def lat2cyr():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Use:\n  lat2cyr <input_file> [output_file]")
        sys.exit(1)

    input_file = sys.argv[1]

    if len(sys.argv) == 3:
        output_file = sys.argv[2]
    else:
        base, ext = os.path.splitext(input_file)
        output_file = f"{base}-cyr{ext}"

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
        converted = latin2cyrillic(text)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(converted)
        print(f"✅ Converted text written to: {output_file}")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
