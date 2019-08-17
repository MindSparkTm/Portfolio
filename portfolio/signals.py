from django.dispatch import Signal

create_profile = Signal(providing_args=['user'])
save_profile = Signal(providing_args=['user'])
test_signal = Signal(providing_args=['user'])