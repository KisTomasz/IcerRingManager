import ConfigParser


def read_prices_from_config_file():
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read('config.txt')
    price_dict = {}
    price_dict['normalny'] = int(config.get('ceny', 'normalny'))
    price_dict['ulgowy'] = int(config.get('ceny', 'ulgowy'))
    price_dict['boots'] = int(config.get('ceny', 'buty'))
    return price_dict


def read_database_name_from_config_file():
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read('config.txt')
    return config.get('baza_danych', 'nazwa')

# print read_prices_from_config_file()
