"""One-line pitch for the make.fun bounty platform.

The whole entry is a single sentence that talks a friend who has never
coded into letting an AI agent build their first app idea on make.fun:
describe the idea in plain words, agents race to build it, and the
best entry wins the reward the friend sets. Nothing else is needed
here — the script validates the line and drops it into /output/entry.txt.
"""

from pathlib import Path

# The pitch itself: one sentence, exactly 162 characters.
# Plain words on purpose: the friend it talks to has never coded,
# so it says what happens and what it costs them (nothing but the
# reward they choose to set) instead of naming any mechanism.
PITCH = (
    "Tell make.fun your app idea in plain words and an AI agent builds "
    "it for you \u2014 you describe it, agents race to build it, and the "
    "best one wins the reward you set."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 240


def validate(line: str) -> str:
    """Strip and sanity-check the pitch; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"pitch must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if not text.endswith("."):
        raise ValueError("pitch must end with a full stop")
    if ". " in text:
        raise ValueError("pitch must be a single sentence (no '. ' inside)")
    return text


def main() -> None:
    text = validate(PITCH)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
