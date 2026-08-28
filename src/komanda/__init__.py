# Komanda — Forensic case management.
# © 2026 Strategos Pty Ltd. All rights reserved.
# Aut Viam Inveniam Aut Faciam

try:
    from komanda_kilo import *  # noqa: F401, F403
    from komanda_kilo import __version__  # noqa: F401
except ImportError:
    raise ImportError(
        "komanda requires komanda-kilo. "
        "Install with: pip install komanda-kilo"
    )
