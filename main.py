"""One Word, First Thought.

Writes exactly one word -- the first word that comes to mind -- to
entry.txt in the harness output directory.
"""

import os


def main():
    # vellichor: the strange wistfulness of used bookshops, which are
    # somehow infused with the passage of time. One word, vivid, and
    # not the safe one a reader would guess.
    word = "vellichor"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(word)


if __name__ == "__main__":
    main()
