from copy import copy

# Template tag doesn't work with options dictionary. We need to change it.
# Pass dictionary from setting file.

def get_thumbnail_options_from_dict(dictt):
    ret= {}
    for name, options in dictt.items():
        opt = copy(options)
        geometry = opt.pop('geometry')
        new_options = ['%s=%s' % (k, v) for k, v in opt.items()]
        new_options.insert(0, geometry)
        ret[name] = ' '.join(new_options)
    return ret