#include <LiquidCrystal.h> 
 
 const int lowled = 9;
int highled = 13;
int buzz = 8;
int ldrTop = A5;
int ldrFront = A1;
int valueTop = 900;
int valueFront = 850;
int iceCream = 6;
int i = 0;
int a = 0;
int b = 0;
int lightFront;
int lightTop;
int STATE;
int hazard = 7;
int potTop = A3;

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  lcd.begin(16, 2);
  pinMode(lowled, OUTPUT);
  pinMode(buzz, OUTPUT);
  pinMode(highled, OUTPUT);
  pinMode(iceCream, INPUT);
  digitalWrite(iceCream, HIGH);
  pinMode(ldrTop, INPUT);
  pinMode(ldrFront, INPUT);
  Serial.begin(9600);
  Serial.println("READY...");
  Serial.println("SET CASE...");
  digitalWrite(lowled, HIGH);
  digitalWrite(highled, LOW);
  pinMode(hazard, OUTPUT);
  pinMode(potTop, INPUT);
}

void loop(){
  lightTop = analogRead (ldrTop);
  lightFront = analogRead (ldrFront);
  STATE = digitalRead(iceCream);
  Serial.println(lightTop);
  if(b > 100){
    lcd.clear();
  lcd.setCursor(0,0);
  lcd.print(lightTop);
  lcd.setCursor(4,0);
  lcd.print("|");
  lcd.setCursor(6,0);
  lcd.print(valueTop);
  b = 0;
  }

  else{
    b ++;
  }
  
  if(lightTop > valueTop){
    while(lightTop > valueTop){

      delay(10);
      i ++;
      
      if(i > 100){
        Serial.println("Case 3");
        lightTop = analogRead (ldrTop);
      lightFront = analogRead (ldrFront);
         STATE = digitalRead(iceCream);
       do{
        if(STATE != LOW){
          Serial.println("off");
          lcd.clear();
          lcd.setCursor(0,0);
          lcd.print("off");
           STATE = digitalRead(iceCream);
          a++;
          digitalWrite(highled, LOW);
          digitalWrite(lowled, HIGH);
          digitalWrite(buzz, LOW);
        }
        else{
          Serial.println("on");
          lcd.clear();
          lcd.setCursor(0,0);
          lcd.print("on");
          lightTop = analogRead (ldrTop);
      lightFront = analogRead (ldrFront);
      
          if(lightTop < valueTop){
            
            lightTop = analogRead (ldrTop);
      lightFront = analogRead (ldrFront);
      
            a++;
            digitalWrite(buzz,LOW);
          digitalWrite(highled, HIGH);
          digitalWrite(lowled, HIGH);
            
          }
          else{
            while(lightTop > valueTop){
               lightTop = analogRead (ldrTop);
      lightFront = analogRead (ldrFront);
      STATE = digitalRead(iceCream);
          digitalWrite(highled, HIGH);
          digitalWrite(lowled, HIGH);
          digitalWrite(buzz, HIGH);
          if(STATE != LOW){
            a++;
            lightTop = 0;
            Serial.println("Problem1");
            lcd.clear();
            lcd.setCursor(0,0);
            lcd.print("Problem1");
          }
          else{
            Serial.println("Problem2"); 
            lcd.clear();
            lcd.setCursor(0,0);
            lcd.print("Problem2"); 
          }
            }
          }
        }
       }while(a = 0);
       digitalWrite(buzz, LOW);
       Serial.println("Case 2");
       lcd.clear();
       lcd.setCursor(0,0);
       lcd.print("Case2");
          do{
            lightTop = analogRead (ldrTop);
          lightFront = analogRead (ldrFront);
          STATE = digitalRead(iceCream);
          if (STATE == LOW){
            STATE = digitalRead(iceCream);
            Serial.println("y");
            lcd.clear();
            lcd.setCursor(0,0);
            lcd.print("y");
            digitalWrite(highled, HIGH);
            digitalWrite(lowled, HIGH);
            delay(1000);
            Serial.println("n");
            lcd.clear();
            lcd.setCursor(0,0);
            lcd.print("n");
            while(STATE == LOW){
            STATE = digitalRead(iceCream); 
            digitalWrite(highled, LOW);
            digitalWrite(lowled, HIGH); 
            }
          }
          else if (lightFront > valueFront){
            Serial.println("Case 4");
            lcd.clear();
            lcd.setCursor(0,0);
            lcd.print("Case4");
         while(lightFront > valueFront){
          lightTop = analogRead (ldrTop);
  lightFront = analogRead (ldrFront);
          digitalWrite(highled, HIGH);
          digitalWrite(lowled, HIGH);   
         }
         delay(2000);
         digitalWrite(highled, LOW);
         digitalWrite(lowled, HIGH);
         digitalWrite(buzz, LOW); 
          }
          else {
            STATE = digitalRead(iceCream);
            Serial.println("n");
            lcd.clear();
            lcd.setCursor(0,0);
            lcd.print("n");
            digitalWrite(highled, LOW);
            digitalWrite(lowled, HIGH); 
          }
          }while(lightTop > valueTop);
      }
      else{
        if(STATE == LOW){
       digitalWrite(highled, HIGH);
       digitalWrite(lowled, HIGH);
      }
      else{
       digitalWrite(highled, LOW);
       digitalWrite(lowled, HIGH);
      }
    }
    }  
  }
  else{
    Serial.println("Case 1");
    digitalWrite(buzz, LOW);
      i = 0;
      lightTop = analogRead (ldrTop);
      lightFront = analogRead (ldrFront);
      STATE = digitalRead(iceCream);
      
      if(STATE == LOW){
       digitalWrite(highled, HIGH);
       digitalWrite(lowled, HIGH);
      }
      else{
       digitalWrite(highled, LOW);
       digitalWrite(lowled, HIGH);
      }
  }
}

