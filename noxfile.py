# /// script
# requires-python = ">=3.14"
# dependencies = [ "nox", "nox-uv" ]
# ///

import nox

from time import sleep


@nox.session
def extensions(session: nox.Session) -> None:
    """Get the extensions needed for the project."""
    session.run(
        "quarto",
        "add",
        "chrischizinski/quarto-sciposter",
        "--no-prompt",
        *session.posargs,
        external=True,
    )

@nox.session
def render(session: nox.Session) -> None:
    """Render `poster.qmd` into `poster.pdf`."""
    session.run(
        "quarto",
        "render",
        "poster.qmd",
#        "-to",
#        "sciposter-typst",
        *session.posargs,
        external=True,
    )

    sleep(2)  # for running this with entr to look for file modifications


if __name__ == "__main__":
    nox.main()
