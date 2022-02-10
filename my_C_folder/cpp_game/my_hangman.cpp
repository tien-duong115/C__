#include<iostream>

#include<cstdlib>

#include<ctime>

#include <string>

using namespace std;

string RandomSecretWord(){
            
    string animals[] = {"dog", "cat","hippo", "monkey", "alligator","lion","chimpanzee", "raccoon", "rabbit", "chicken"};

    srand(time(NULL));

    int word_length = *(&animals +1) - animals;
    
    int random_index = (rand() % 10);
    
    string word = animals[random_index];
    
    return word;
}

void replaceDashes(char guessWord[], int length) {
    // your code goes here
    for (int i = 0 ; i < length ; i++)
        guessWord[i] = '-';
    guessWord[length] = '\0';
}

void displayword(string word, int length){
    for ( int i = 0; i < length; i++) {
        cout << word[i] ;
    }
    cout << endl;
}

void GameDetail(int maxTries) {
        cout << "\n"
"        .-------------------------------------------------------------------------------.\n"
"        |      _      _                                                                  |\n"
"        |     | |    | |   __ _    _ __      __ _        /\\/\\      __ _    _ __          |\n"
"        |     | |----| |  / _  |  |  _ \\    / _` |      /    \\    / _  |  |  _  \\        |\n"
"        |     | |----| | | (_| |  | | | |  | (_| |     / /\\/\\ |  | (_| |  | | | |        |\n"
"        |     |_|    |_|  \\_ _ |  |_| |_|   \\__, |     \\/    \\/   \\_ _ |  |_| |_|        |\n"
"        |                                    |___/                                       |\n"
"        .--------------------------------------------------------------------------------.\n";

cout << "The purpose of this game is to guess an animal name, secretly chosen by the application\n\n";
cout << "You have to guess one letter at a time and you can have " << maxTries << " wrong attempts\n\n";
cout << "Enter a lower-case letter and don't forget to enter key after each guess\n\n";
cout << "Let's play the game!\n\n";
}

int isGuessTrue(string secretWord, char guessWord[], char letter) {
    int flag = 0;
    for (int i = 0; i < secretWord.length(); i++) {
        if (secretWord[i] == letter) {
            if (guessWord[i] == secretWord[i]) {
                flag = 2;
            } else {
                guessWord[i] = secretWord[i];
                flag = 1;
            }
        }
    }
    return flag;
}



void displayMan(int remainingGuess) {

    string part[4];
    switch (remainingGuess) {
    case 0:
        part[3] = "|";
    case 1:
        part[2] = "/|\\";
    case 2:
        part[1] = "/|\\";
    case 3:
        part[0] = "( )";
        break;
    }

    cout << "--------------\n";
    cout << "  |       " << part[3] << endl;
    cout << "  |       " << part[3] << endl;
    cout << "  |      " << part[0] << endl;
    cout << "  |      " << part[1] << endl;
    cout << "  |      " << part[2] << endl;
    cout << "  |\n";
    cout << "  |\n";
    cout << "--------------\n";
}


int main(){
int maxTries = 5;
int RemainingTries = 5;
char guessLetter;
string secretword;
int secretwordlength;

GameDetail(maxTries);

secretword = RandomSecretWord();
secretwordlength = secretword.length();
char guessword[secretwordlength];
replaceDashes(guessword, secretwordlength);
displayword(guessword, secretwordlength);


while (RemainingTries != 0){
    cout << "Enter your guess letter:" << endl;
    cin >> guessLetter;

    int guess = isGuessTrue(secretword, guessword, guessLetter);

    if (guess == 0) {
        RemainingTries--;
        cout << "\nWhoops! that letter is not present in the word" << endl;
        displayMan(RemainingTries);
    }
    if (guess == 1) {
        cout << "\nYay! You have found the letter" << endl;
    }
    if (guess == 2) {
        cout << "\nYou have already guessed this letter. Try something else!" << endl;
    }
    cout << "You can have " << RemainingTries << " more wrong attempts" << endl;
    cout << "Your guess word is:";

    displayword(guessword, secretwordlength);
    cout << endl;
    if (secretword == guessword) {
        cout << "\nCongratulation! You won." << endl;
        return 0;
        }


    }

return 0;}