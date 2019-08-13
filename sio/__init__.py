import shortio
from .__version__ import __version__

__all__ = []
for name in dir(shortio):
    if name.startswith(('read_', 'write_')):
        name_parts = name.split('_')
        prefix_letters = ''.join([part[0] for part in name_parts[:-1]])

        frmt = name_parts[-1].translate({ord(c): None for c in 'aeiou'})

        new_name = f'{prefix_letters}{frmt}'
        exec(f'{new_name} = shortio.{name}')
        __all__.append(new_name)
