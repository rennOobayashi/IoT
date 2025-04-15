#ifndef LEDTOGGLE_H
#define LEDTOGGLE_H

#include "Arduino.h"

class LedToggle {
public:
       LedToggle(int pin);
       ~LedToggle() {}
       void toggle();
private:
        int _pin;
        bool _state;      
};

#endif
