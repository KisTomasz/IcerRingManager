import ConfigParser

def read_prices_from_config_file():
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.read('config.txt')
    price_dict = {}
    price_dict['normalny'] = config.get('ceny', 'normalny')
    price_dict['ulgowy'] = config.get('ceny', 'ulgowy')
    price_dict['boots'] = config.get('ceny', 'buty')
    return price_dict



#print read_prices_from_config_file()

