void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}

void loop() {
  String buff;
  while(Serial.available() > 0);
  buff = Serial.readString();
  if(buff == "ON")
  {
    digitalWrite(13,HIGH);
  }
  else if(buff == "OFF")
  {
    digitalWrite(13,LOW);
  }
}
