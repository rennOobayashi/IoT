#include <LedToggle.h>

void setup() {
  LedToggle led(LED_BUILTIN, 1500);

  Serial.begin(9600);
  led.toggle();
  led.toggle();
}

void loop() {
}
