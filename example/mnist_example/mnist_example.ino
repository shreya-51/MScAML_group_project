#include <EloquentTinyML.h>

// copy the printed code from tinymlgen into this file
#include "digits_model.h"

#define NUMBER_OF_INPUTS 64
#define NUMBER_OF_OUTPUTS 10
#define TENSOR_ARENA_SIZE 8*1024

Eloquent::TinyML::TfLite<NUMBER_OF_INPUTS, NUMBER_OF_OUTPUTS, TENSOR_ARENA_SIZE> ml;

void setup() {
    Serial.begin(115200);
    ml.begin(digits_model);
}

void loop() {
    // a random sample from the MNIST dataset (precisely the last one)
    float x_test[64] = { 0., 0. , 0.625 , 0.875 , 0.5   , 0.0625, 0. , 0. ,
                    0. , 0.125 , 1. , 0.875 , 0.375 , 0.0625, 0. , 0. ,
                    0. , 0. , 0.9375, 0.9375, 0.5   , 0.9375, 0. , 0. ,
                    0. , 0. , 0.3125, 1. , 1. , 0.625 , 0. , 0. ,
                    0. , 0. , 0.75  , 0.9375, 0.9375, 0.75  , 0. , 0. ,
                    0. , 0.25  , 1. , 0.375 , 0.25  , 1. , 0.375 , 0. ,
                    0. , 0.5   , 1. , 0.625 , 0.5   , 1. , 0.5   , 0. ,
                    0. , 0.0625, 0.5   , 0.75  , 0.875 , 0.75  , 0.0625, 0. };
    // the output vector for the model predictions
    float y_pred[10] = {0};
    // the actual class of the sample
    int y_test = 8;

    // let's see how long it takes to classify the sample
    uint32_t start = micros();

    ml.predict(x_test, y_pred);

    uint32_t timeit = micros() - start;

    Serial.print("It took ");
    Serial.print(timeit);
    Serial.println(" micros to run inference");

    // let's print the raw predictions for all the classes
    // these values are not directly interpretable as probabilities!
    Serial.print("Test output is: ");
    Serial.println(y_test);
    Serial.print("Predicted proba are: ");

    for (int i = 0; i < 10; i++) {
        Serial.print(y_pred[i]);
        Serial.print(i == 9 ? '\n' : ',');
    }

    // let's print the "most probable" class
    // you can either use probaToClass() if you also want to use all the probabilities
    Serial.print("Predicted class is: ");
    Serial.println(ml.probaToClass(y_pred));
    // or you can skip the predict() method and call directly predictClass()
    Serial.print("Sanity check: ");
    Serial.println(ml.predictClass(x_test));

    delay(1000);
}