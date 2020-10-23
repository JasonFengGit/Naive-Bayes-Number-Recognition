# Naive-Bayes-Number-Recognition
A [Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_classifier) hand-written number classifier implemented in Python using only built-in libraries. (MNIST dataset)

## Dataset
I used MNIST dataset to train the model.
The files are too large. You may download them [here](https://www.kaggle.com/oddrationale/mnist-in-csv). <br/>
***You should REMOVE the first row to avoid errors.***

- Training: 50000
- Validation: 10000
- Testing: 10000

## Model
- Input Layer: Size 784 (28 * 28 representing each pixel in an image)
- Output Layer: Size 10 (representing 10 digits)

## Features
- performs approximately 85% correct on test data.
- supports terminal "graphics" for user to view the image through ACSII arts.
- uses about 30 seconds to train

## Sample Run

#### Testing, Graphics On:
```
NO.0
predict: 7
actual: 7
accumulative precision: 1.0







      -#*+:.
      %@@@@@########*:
      :=:=*%@%@@@@%@@+
            : :::: @@=
                  -@%
                  %@-
                 =@@.
                :@@:
                +@#
                #@:
               =@#
              :@@:
              %@*
             #@%.
            .@@:
           .%@=
           +@@:
          :@@@:
          =@@%.
          =@#

press Enter to continue
NO.1
predict: 2
actual: 2
accumulative precision: 1.0



          ==*@@+-
         *@@@@@@%.
        *@@@%+*@@=
       :@@%.   #@+
       :@%    =@@:
        .     %@@:
             =@@#
            :@@%:
            =@@+
           *@@*
           @@%.
          #@@+
         -@@#
         #@@+
        +@@*
        @@@
        @@@.         .++++
        @@@@@@@@*+*@@@@@@@=
        *@@@@@@@@@@@@@@*==:
         ====*@@@+==.





press Enter to continue
NO.2
predict: 1
actual: 1
accumulative precision: 1.0




                .@=
                -@-
                +@
               .@+
               -@:
               #%
              .@%
              -@#
              +@:
             :@#
             =@*
             *@-
             %%
            =@*
            +@+
            %@:
           :@@:
           +@#
           %@=
           #*




press Enter to continue
NO.3
predict: 0
actual: 0
accumulative precision: 1.0




             +@#.
            .@@@=
            #@@@=
          =#@@@@*=:
          @@@@@@@@%.
         #@@@@@@%@@@
        :%@@@@+::=@@=
       .%@@@%+   .%@@=
       .@@@#      =@@@.
       .@@#.      .#@@.
       .@@        .#@@*
       +@@        =@@@.
       %@@       :%@@%.
       %@@      +@@@%:
       %@@     #%@@@*
       %@@::%@@@@@@@
       =@@@@@@@@@@@+
       .%@@@@@@@%#.
        :+@@@@@@=
          :*@*::.




press Enter to continue
NO.4
predict: 4
actual: 4
accumulative precision: 1.0





          .%       :.
          =%       +*
          #%       -%
         :@+       =@
        .@%        #@
        *@:        @@
       -@%        +@#
       *@=       .%@:
       %@        +@%
       @*        *@*
       #%        @@=
       *@#----=*#@@=
       .*@@@@@%%@@@
         .----  *@@
                =@@.
                =@@
                =@@
                +@@
                %@=
                *:



press Enter to continue
NO.5
predict: 1
actual: 1
accumulative precision: 1.0





                :@=
                %@@
               -@@*
               #@@:
              :@@@
              +@@*
              #@@.
             :@@@
             =@@+
             *@@.
            :@@%
            -@@+
            *@@:
           .@@%
           -@@+
           =@@
           *@#
           %@#
           *@*
           .*=



press Enter to continue
NO.6
predict: 4
actual: 4
accumulative precision: 1.0





          #+.         :
         @@*         %@.
        #@+         +@-
       :@@         .@*
       +@-        .%@-
      *@#         =@*
      *@*        +@@
      *@@#*::::+#@@*
      .%@@@@@@@@@@%.
        :+@%+++.@@*
               .@#
               *@:
              -@@.
              *@*
              %@.
             =@%
             %@*  .
             %@+-#*
             %@@@+.
             :#=



press Enter to continue
NO.7
predict: 9
actual: 9
accumulative precision: 1.0






            +#
          -%@@
         .@@@@*
         +@@@@@@=
        .@@%#@@@%
        -@#  -%@@#
        -@-   #@@#
        *@+   @@@+
        -@%.-*@@@@.
         @@@@@#.%@+
         :@@@+  +@%.
          :*+    *@*
                 -@%
                  *@=
                  .@@.
                   =@*
                    %@.
                    .@*
                     #@.
                      %-


press Enter to continue
NO.8
predict: 4
actual: 5
accumulative precision: 0.8888888888888888




                  ... =-.
               :+%@@@%@@@
            .+@@@@@@@@@@@
            :@@@@@@@%****
         +: :@%@*=:
        #@-  . .
       *@+
      +@%
     -@%.
     +@*
     @@@=.
     @@@@@+-=-..-.
     +@@@@@@@@@@@%*
      :%%@@@@@@@@@@=
         ::#@@@@@@@*
           =@@+.*@@*
           .@@@#@@@+
            *@@@@@*
             *%@%=
              -+




press Enter to continue
NO.9
predict: 9
actual: 9
accumulative precision: 0.9







             .:+##-.
           .+@@@@@@@%+
         .+@@@%*+@#@%%=
        +@@@#+   #.#@%@
       =@@%=     %.:@@@
      :@@%:     .=%@@@*
      :@@%=+***%@%@@@%.
       *@@@@@@@@@@@@*
         +#*++#@@@@+
              *@@@-
             =@@@-
            -@@@%
           :@@@@:
           +@@@:
           @@@+
          %@@%
         -@@@:
         %@@+
         %@%
         =@=

press Enter to continue

...
```

#### Testing, Graphics Off:
```
.
.
.

NO.9995
predict: 2
actual: 2
accumulative precision: 0.8414365746298519
NO.9996
predict: 3
actual: 3
accumulative precision: 0.8414524357307193
NO.9997
predict: 9
actual: 4
accumulative precision: 0.841368273654731
NO.9998
predict: 5
actual: 5
accumulative precision: 0.8413841384138414
NO.9999
predict: 6
actual: 6
accumulative precision: 0.8414
```

## Run Locally
```
py naive_bayes_mnist.py
```

