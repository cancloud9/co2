#define lightSensor A0

void setup()
{
  pinMode (lightSensor, INPUT);
  Serial.begin(9600);
}

void loop()
{
  Serial.println(filterFirstOrderDelay());
  delay(100);
}

int filterAvg(int K)
{
  int data=0;
  for (int i=0;i<K;i++)
  {
    data+=analogRead(lightSensor);
  }
  return data/K;
}

int filterFirstOrderDelay()
{
  const static float F=0.1;
  static int preData;
  int data=analogRead(lightSensor);
  preData=(int)((float)data*F+(1.0-F)*(float)preData);
  return preData;
}

