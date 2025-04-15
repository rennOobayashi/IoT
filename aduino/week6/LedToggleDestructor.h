#ifndef LEDTOGGLE_H
#define LEDTOGGLE_H

#include "Arduino.h"

class LedToggle {
private:
        long _delay;
        int _pin;
        bool _state;  
public:
       LedToggle(int pin);
       LedToggle(int pin, unsigned long delay);
       ~LedToggle() { Serial.println("end"); }
       void toggle();    
};

#endif
