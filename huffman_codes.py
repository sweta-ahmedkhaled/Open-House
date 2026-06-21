# ── Generate Codes ─────────────────────────────────────────────────────────────
def get_codes(node, prefix="", codes={}):
    if node.char is not None:
        codes[node.char] = prefix
    else:
        get_codes(node.left,  prefix + "0", codes)
        get_codes(node.right, prefix + "1", codes)
    return codes