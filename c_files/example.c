/*****************************************/
//CPU Access to memory.
/*****************************************/

int wordsize(int a){
    a += 1;
    return a;
}

//halfsize
int halfsize(unsigned short a){
    a += 1;
    return a;
}

int bytesize(char a){
    a += 1;
    return a; //cast to int ?
}


/*****************************************/
//CPU Access to memory cont.
/*****************************************/

struct NotAGoodOne {
    char one;
    short two;
    char three;
    int four;
};

struct NotAGoodOne NAGO;



/*****************************************/
//How to write memory friendly code
/*****************************************/

int func1(int a, int b, int c, int d) {
    return a+b+c+d;
}
int caller1(void) {
    return func1(1, 2, 3, 4);
}


int func2(int a, int b, int c, int d, int e, int f) {
    return a+b+c+d+e+f;
}

int caller2(void) {
return func2(1, 2, 3, 4, 5, 6);
}


/*****************************************/
//Fun with code optimization
/*****************************************/

int f(int*p)
{
    return (*p == *p);
}

int f2(volatile int*p)
{
    return (*p == *p);
}



static inline int bar(int a)
{
    a=a*(a+1);
    return a;
}
int foo(int i)
{
    i=bar(i);
    i=i-2;
    i=bar(i);
    i++;
    return i;
}



int Ffunc1 (int param_1a, int param_1b)
{
    struct NotAGoodOne localNAGO[50] = {0};
    
    for(int i=0; i<50; i++){
        localNAGO[i].one = i;
        localNAGO[i].four = param_1a++  * param_1b + i;
    }
    return (int)(localNAGO[0].four + localNAGO[10].one);
}
int Fcaller1(void) {

    int  local_var = Ffunc1(1, 2);
    return local_var+1;
}