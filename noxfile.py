# /// script
# requires-python = ">=3.14"
# dependencies = [ "nox", "nox-uv" ]
# ///

import nox


@nox.session
def extensions(session: nox.Session) -> None:
    """Get the extensions needed for the project."""
    session.run(
        "quarto",
        "add",
        "chrischizinski/quarto-sciposter",
        "--no-prompt",
        external=True,
    )

@nox.session
def render(session: nox.Session) -> None:
    """Render `poster.qmd` into `poster.pdf`."""
    session.run(
        "quarto",
        "render",
        "poster.qmd",
        external=True,
    )


if __name__ == "__main__":
    nox.main()
