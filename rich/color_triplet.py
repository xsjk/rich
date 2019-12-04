from typing import NamedTuple, Tuple


class ColorTriplet(NamedTuple):
    """The red, green, and blue components of a color."""

    red: int
    green: int
    blue: int

    @property
    def css(self) -> str:
        """get the color triplet in CSS style."""
        red, green, blue = self
        return f"#{red:02x}{green:02x}{blue:02x}"

    def normalize(self) -> Tuple[float, float, float]:
        """Covert components in to floats between 0 and 1."""
        red, green, blue = self
        return red / 255.0, green / 255.0, blue / 255.0
