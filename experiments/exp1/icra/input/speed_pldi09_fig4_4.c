#include <assert.h>

void start(int i0){
    int i = i0;
    while(i > 0){
        if(i < 1000000){
            i = i - 1;
        } else {
            i = i - 1000000;
        }
    }
    assert(i == {1});
}

int main(){
    int i = {0};
    start(i);
    return 0;
}