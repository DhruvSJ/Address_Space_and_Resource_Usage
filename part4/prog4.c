#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "check.h"
#include <sys/time.h>
#include <sys/resource.h>


int x[5] = {1,2,3,4,5};
//double c = 10.0;

void allocate()
{
    int i;
    int *p;
    for(i =1 ; i<1000000 ; i++)
    {
      p = malloc(500 * sizeof(int));
      if(func(i)) { free (p);}
    }
}

void allocate1()
{
  int i;
  int *p;
  for (i=1 ; i<10000 ; i++)
  {
    p = malloc(1000 * sizeof(int));
    if(i & 1)
      free (p);
  }
}

void allocate2()
{
  int i;
  int *p;
  for (i=1 ; i<300000 ; i++)
  {
    p = malloc(10000 * sizeof(int));
    free (p);
  }
}

int main(int argc, char const *argv[]) {
  
  struct rusage usage;
  struct timeval sys_end;
  struct timeval user_end;
  long int end_res_size;
  long int end_signal;
  long int end_switch;
  long int end_in_switch;
  int i;
  int *p;
  printf("Executing the code ......\n");
  
  allocate();

  for (i=0 ; i<10000 ; i++)
  {
    p = malloc(1000 * sizeof(int));
    free (p);
  }
  printf("Program execution successfull\n");
  
  getrusage(RUSAGE_SELF, &usage);

  sys_end=usage.ru_stime;
  user_end=usage.ru_utime;
  end_res_size=usage.ru_maxrss;
  end_signal=usage.ru_nsignals;
  end_switch=usage.ru_nvcsw;
  end_in_switch=usage.ru_nivcsw;
 
  printf("\n\nsystem time: %ld.%09lds,\nuser time: %ld.%09lds,  \nsize: %ld,\nsignals: %ld,\nvoluntary switch: %ld,\ninvoluntary switch: %ld\n",sys_end.tv_sec,sys_end.tv_usec, user_end.tv_sec,user_end.tv_usec,end_res_size,end_signal,end_switch,end_in_switch);

  return 0;
}
