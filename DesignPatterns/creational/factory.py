"""
Delegate a specialized function/method to create instances.
Factory is an object for creating other objects.

The code shows a way to localize words in two languages: English and
Russian. "get_localizer" is the factory function that constructs a
localizer depending on the language chosen. The localizer object will
be an instance from a different class according to the language
localized. However, the main code does not have to worry about which
localizer will be instantiated, since the method "localize" will be called
in the same way independently of the language.

The Factory Method can be seen in the popular web framework Django:
For example, in a contact form of a web page, the subject and the message
fields are created using the same form factory (CharField()), even
though they have different implementations according to their
purposes.
"""
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class RussianLocalizer:
    translations: Dict[str, str] = field(
        default_factory=lambda: {'dog': 'собака', 'cat': 'кот'})

    def localize(self, msg: str) -> str:
        """We'll punt if we don't have a translation"""
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    """Simply echoes the message"""

    def localize(self, msg: str) -> str:
        return msg


def get_localizer(language: str = "English") -> object:

    """Factory"""
    localizers = {
        "English": EnglishLocalizer,
        "Russian": RussianLocalizer,
    }

    return localizers[language]()


if __name__ == '__main__':
    eng, rus = get_localizer(language="English"), get_localizer(language="Russian")

    # Localize some text
    for msg in "dog parrot cat bear".split():
        print(eng.localize(msg), rus.localize(msg))
