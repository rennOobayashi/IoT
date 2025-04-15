#ifndef LEDTOGGLE_H
#define LEDTOGGLE_H

#include "Arduino.h"

class LedToggle {
public:
       LedToggle(int pin);
       LedToggle(int pin, long delay);
       ~LedToggle() {}
       void toggle();
private:
        int _pin;
        long _delay;
        bool _state;      
};

#endif
