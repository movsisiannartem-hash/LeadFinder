def build_query(tag, value, south, west, north, east):
    return f"""
[out:json];
nwr["{tag}"="{value}"]({south},{west},{north},{east});
out;
"""