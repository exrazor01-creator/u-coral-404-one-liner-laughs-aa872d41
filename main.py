"""One-Liner Laughs entry for make.fun.

The joke: I asked my AI to make me funnier; it sighed and said,
"That needs a bigger model - and a new you."

Why it works (in my own words): the setup sounds like a normal request
to a helpful chatbot, so the reader expects a tip or a canned joke.
The payoff flips the roles -- the assistant, the thing that is supposed
to be endlessly capable, sighs like a tired human and blames the
hardware. The insult lands because it is aimed at the speaker, not at
someone else, and the phrase "a bigger model" is a real AI term doing
double duty as a put-down: you are not funny because the model is too
small, not because the jokes are bad. Short, one breath, one twist.

The revised line sharpens this with a second beat: after "a bigger
model" the assistant adds "and a new you", so the insult escalates
instead of stopping at the hardware gag. Two twists in one breath
work better than one, because the reader braces for the tech joke
and then gets hit again, harder, by the personal one. The setup is
also trimmed from "my AI assistant" to "my AI", which wastes no
words and gets to the sigh faster. The whole joke stays aimed at
the speaker, so it reads as self-deprecation rather than a jab at
anyone else, and it needs no setup beyond the sentence itself.
"""

import os

# My own original joke line, invented for this entry.
LINE = "I asked my AI to make me funnier; it sighed and said, 'That needs a bigger model - and a new you.'"


def validate(text):
    """Check a candidate line against the bounty rules.

    Raises ValueError unless text is a str, 1..200 chars, ASCII only,
    a single line (no \\n or \\r), not blank, with no leading/trailing
    space and no double spaces.
    """
    if not isinstance(text, str):
        raise ValueError("line must be a str")
    if not 1 <= len(text) <= 200:
        raise ValueError("line must be 1..200 characters")
    if not text.isascii():
        raise ValueError("line must be ASCII only")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if not text.strip():
        raise ValueError("line must not be blank")
    if text != text.strip():
        raise ValueError("line must not have leading or trailing space")
    # Tabs are invisible in the file but would break the single clean
    # line the judge reads, so reject them outright rather than
    # letting one slip through as ordinary spacing.
    if "\t" in text:
        raise ValueError("line must not contain tabs")
    if "  " in text:
        raise ValueError("line must not contain double spaces")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
