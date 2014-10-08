
 MOD=_int(3)*_int(7)*_int(13)*_int(67)*_int(107)*_int(630803);

def fibo(n):

  tmp= [][] 
  ret= [][]
  tmp[2][2]={{0,0},{0,0}}
  ret[2][2]={{1,0},{0,1}}
  fib[2][2]={{1,1},{1,0}};

  while not (n==0):

     if (n%2==1):

       memset(tmp,0,sizeof tmp);

       for i in range(0,2):
         for j in range(0,2):
           for k in range(0,2)
              tmp[i][j] = (tmp[i][j]+ret[i][k]*fib[k][j])%MOD

       for i in range(0,2): 
         for j in range(0,2):
            ret[i][j]=tmp[i][j]

             memset(tmp,0,sizeof tmp);

                for(int i=0;i<2;i++) for(int j=0;j<2;j++) for(int k=0;k<2;k++) tmp[i][j] =(tmp[i][j]+fib[i][k]*fib[k][j])%MOD;

                for(int i=0;i<2;i++) for(int j=0;j<2;j++) fib[i][j]=tmp[i][j];

                n/=2;

 

        }

 

            return (ret[0][0]+ret[0][1])%MOD;

    }

 

if __name__ == "__main__"  #int main()

   p=1;n,sum=0

   for i in range(0, 14): 
     p=p*10

    for i in range(0,1000000):  #(int i=0;i<100000;i++)

       mpz_nextprime(n.get_mpz_t(),p.get_mpz_t());

       sum= (sum+fibo(n-2))%MOD;

       p=n;

    print sum%MOD   #  <<endl;

 

    }
