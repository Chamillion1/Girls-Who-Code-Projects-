int leftWhisker = 5;
int rightWhisker = 7; 



void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(leftWhisker, INPUT);
  pinMode(rightWhisker, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(digitalRead(leftWhisker));
  Serial.print1n(digitalRead(rightWhisker));
  delay(1000); 

}
