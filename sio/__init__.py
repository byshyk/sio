import shortio
from .__version__ import __version__

__all__ = []
for name in dir(shortio):
    name_parts = name.split('_')

    if name_parts[0] in ('read', 'write'):
        if len(name_parts) > 1:
            prefix_letters = ''.join([part[0] for part in name_parts[:-1]])
            frmt = name_parts[-1].translate({ord(c): None for c in 'aeiou'})
            new_name = f'{prefix_letters}{frmt}'
        else:
            new_name = name_parts[0][0]

        exec(f'{new_name} = shortio.{name}')
        __all__.append(new_name)
