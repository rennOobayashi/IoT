#include "LedToggle.h"

LedToggle::LedToggle(int pin) {
                         _pin = pin;
                         _state = false;
                         _delay = 0;
                         pinMode(_pin, OUTPUT);
                         digitalWrite(_pin, LOW);
}

LedToggle::LedToggle(int pin, long delay) {
                         _pin = pin;
                         _state = false;
                         _delay = delay;
                         pinMode(_pin, OUTPUT);
                         digitalWrite(_pin, LOW);
}

void LedToggle::toggle() {
     _state = !_state;
     digitalWrite(_pin, _state ? HIGH : LOW);
     delay(_delay);
}
