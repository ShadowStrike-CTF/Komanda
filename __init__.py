# © 2026 Strategos. All rights reserved.
# komanda — stub package. Redirects to komanda-kilo.
# See: https://github.com/ShadowStrike-CTF/shadowstrike-suite

try:
    from komanda_kilo import *  # noqa: F401, F403
    from komanda_kilo import __version__  # noqa: F401
except ImportError:
    raise ImportError(
        "komanda requires komanda-kilo. "
        "Install with: pip install komanda-kilo"
    )
