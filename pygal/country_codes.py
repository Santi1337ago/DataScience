from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """Возвращает для заданной страны ее код Pygal, состоящий из 2 букв."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # Если страна не найдена, вернуть None.
    return None
