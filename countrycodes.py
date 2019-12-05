from pygal_maps_world import i18n

def get_country_code(country_name):
    """Return a 2-digit country code for given country"""
    countries = i18n.COUNTRIES

    for code, name in countries.items():
        if name == country_name:
            return code
    # If the country was not found, return none
    return None


