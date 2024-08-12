# exercises/__init__.py

from .squat import detect_squat
from .push_up import detect_push_up
from .bench_press import detect_bench_press
from .dips import detect_dips
from .pull_up import detect_pull_up
from .crunches import detect_crunches

__all__ = [
    'detect_squat',
    'detect_push_up',
    'detect_bench_press',
    'detect_dips',
    'detect_pull_up',
    'detect_crunches'
]
