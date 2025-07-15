from typing import Union, List, Optional

from rich.console import Console
from rich.table import Table


def render_table(
    objects: List[Union[dict, object]],
    keys: Optional[List[str]] = None,
    title: Optional[str] = None,
    header_style: str = "bold magenta",
) -> str:
    """Render a table from a list of dictionaries or objects."""
    table = Table(
        title=title, show_header=True, show_lines=True, header_style=header_style
    )

    # Create table headers based on the keys
    item = objects[0]
    if keys is None:
        if isinstance(item, dict):
            keys = list(item.keys())
        else:
            keys = list(vars(item).keys())

    for key in keys:
        table.add_column(key.replace("_", " ").title(), justify="left")

    # Add rows to the table
    missing_placeholder = "-"
    for obj in objects:
        row = []
        for key in keys:
            if isinstance(obj, dict):
                value = obj.get(key, missing_placeholder)
            else:
                value = getattr(obj, key, missing_placeholder)

            if isinstance(value, list):
                value = (
                    ", ".join(str(v) for v in value) if value else missing_placeholder
                )
            elif value in (None, ""):
                value = missing_placeholder

            row.append(str(value))
        table.add_row(*row)

    # Render the table to a string
    console = Console(record=True)
    console.print()
    console.print(table)
    console.print()
    return console.export_text()
